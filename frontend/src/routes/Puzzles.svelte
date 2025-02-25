<script lang="ts">
  import { toast } from "svelte-sonner";
  import FileUI from "$lib/components/subUI/FileUI.svelte";
  import GameUI from "$lib/components/subUI/gameUI.svelte";
  import type { CrosswordData } from "$lib/components/crossword/Crossword.svelte";

  let uploadComplete: boolean = false;
  let crosswordData: CrosswordData | null = null;
  const ENDPOINT = "http://127.0.0.1:8000";

  async function resolveUpload(files: FileList) {
    const file: File | null = files.item(0);
    if (!file) return;

    toast.info(`Got file: ${file.name}`);

    const formData = new FormData();
    formData.append("file", file);
    uploadComplete = true;

    const uploadPromise = fetch(`${ENDPOINT}/upload`, {
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
        const gameData = data.game;
        crosswordData = {
          legend: gameData.legend,
          solution: gameData.solution,
        };
        return crosswordData;
      });

    toast.promise(uploadPromise, {
      loading: "Uploading file...",
      success: (_) => "Upload complete, game ready!",
      error: (_) => `Error`,
    });

    try {
      await uploadPromise;
    } catch (error: any) {
      console.error("Upload error:", error);
    }
  }
</script>

{#if uploadComplete && crosswordData}
  <GameUI {crosswordData} />
{:else}
  <FileUI fileHandler={resolveUpload} />
{/if}
