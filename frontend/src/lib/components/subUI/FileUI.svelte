<script lang="ts">
  import { toast } from "svelte-sonner";
  import type { CrosswordData } from "$lib/components/crossword/Crossword.svelte";
  import Button from "$lib/components/ui/button/button.svelte";
  import Badge from "$lib/components/ui/badge/badge.svelte";
  import FileDrop from "$lib/components/ui/input/filedropzone.svelte";
  import Label from "$lib/components/ui/label/label.svelte";

  let fileUploaded = false;
  let fileNames: string[] = [];
  let selectedFiles: FileList | null = null;

  export let fileHandler: (files: FileList) => void;

  function onFilesReceived(event: CustomEvent<{ files: FileList }>) {
    selectedFiles = event.detail.files;
    fileNames = Array.from(selectedFiles).map((file) => file.name);
    toast.info(`Files received: ${fileNames.join(", ")}`);
  }

  function startUpload() {
    if (selectedFiles && fileHandler) {
      fileHandler(selectedFiles);
      fileUploaded = true;
    } else {
      toast.error("No file selected!");
    }
  }
</script>

<div class="flex flex-col items-center gap-4 w-full">
  <p class="text-lg font-semibold">Turn Research into Play! 🎓🧩</p>
  <ul class="text-start border border-zinc-300 rounded-md p-2">
    <li>📄 Upload a research paper</li>
    <li>🧠 Solve word puzzles based on its content</li>
    <li>🎯 Enhance comprehension & retention</li>
  </ul>
  <div class="w-[25vw]">
    <Label for="file-input">Upload a File</Label>
    <FileDrop
      on:files={onFilesReceived}
      accept="application/pdf"
      multiple={false}
    />
    <Button on:click={startUpload} class="mt-[.3rem] mb-[.3rem] w-full">
      Start
    </Button>
    {#if fileNames.length}
      <div class="w-full flex flex-wrap justify-start p-1">
        {#each fileNames as fileName}
          <Badge class="mr-2 mb-2" variant="secondary">
            {fileName}
          </Badge>
        {/each}
      </div>
    {/if}
  </div>
</div>

