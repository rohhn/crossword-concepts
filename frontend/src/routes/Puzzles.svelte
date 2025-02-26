<script module lang="ts">
</script>

<script lang="ts">
  import { toast } from "svelte-sonner";
  import FileUI from "$lib/components/subUI/FileUI.svelte";
  import GameUI from "$lib/components/subUI/gameUI.svelte";
  import UploadingUI from "$lib/components/subUI/UploadingUI.svelte";
  import type { GameType } from "$lib/components/subUI/gameUI.svelte";
  import { fade, slide } from "svelte/transition";

  let selectedFiles: FileList | null = null;
  let uploadComplete: boolean = false;
  let gameData: GameType | null = null;
  let isUploading = false;
  const ENDPOINT = ${import.meta.env.VITE_FLASK_API_URL};

  async function resolveUpload(files: FileList) {
    const file: File | null = files.item(0);
    if (!file) return;

    toast.info(`Got file: ${file.name}`);

    isUploading = true;
    const formData = new FormData();
    formData.append("file", file);
    uploadComplete = true;

    const uploadPromise = fetch(`${ENDPOINT}/play`, {
      method: "POST",
      body: formData,
    })
      .then((response) => {
        if (!response.ok) {
          throw new Error(`API error: ${response.statusText}`);
        }
        return response.json();
      })
      .then((data) => {
        gameData = data;
        return gameData;
      });

    toast.promise(uploadPromise, {
      loading: "Building 🔧",
      success: (_) => "Upload complete, game ready!",
      error: (_) => `Error`,
    });

    try {
      await uploadPromise;
    } catch (error: any) {
      console.error("Upload error:", error);
    } finally {
      isUploading = false;
    }
  }
</script>

<div class="h-full w-full flex justify-center items-center">
  {#if uploadComplete && gameData}
    <div
      class="h-full w-full flex items-center justify-center"
      in:slide={{ duration: 300 }}
      out:slide={{ duration: 400 }}
    >
      <GameUI {gameData} bind:selectedFiles />
    </div>
  {:else if isUploading}
    <div
      class="h-full w-full flex items-center justify-center"
      in:slide={{ duration: 300 }}
      out:slide={{ duration: 400 }}
    >
      <UploadingUI />
    </div>
  {:else}
    <div
      class="h-full w-full flex items-center justify-center"
      in:slide={{ duration: 300 }}
      out:slide={{ duration: 400 }}
    >
      <FileUI bind:selectedFiles fileHandler={resolveUpload} />
    </div>
  {/if}
</div>
