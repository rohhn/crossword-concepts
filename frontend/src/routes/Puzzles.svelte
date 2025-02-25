<script lang="ts">
  import { toast } from "svelte-sonner";
  import FileUI from "$lib/components/subUI/FileUI.svelte";
  import GameUI from "$lib/components/subUI/gameUI.svelte";
  import UploadingUI from "$lib/components/subUI/UploadingUI.svelte";
  import type { GameType } from "$lib/components/subUI/gameUI.svelte";
  import { fade, slide } from "svelte/transition";

  let uploadComplete: boolean = false;
  let gameData: GameType | null = null;
  let isUploading = false;
  const ENDPOINT = "http://127.0.0.1:8000";

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

{#if uploadComplete && gameData}
  <div in:slide={{ duration: 300 }} out:slide={{ duration: 400 }}>
    <GameUI {gameData} />
  </div>
{:else if isUploading}
  <div in:slide={{ duration: 300 }} out:slide={{ duration: 400 }}>
    <UploadingUI />
  </div>
{:else}
  <div in:slide={{ duration: 300 }} out:slide={{ duration: 400 }}>
    <FileUI fileHandler={resolveUpload} />
  </div>
{/if}
