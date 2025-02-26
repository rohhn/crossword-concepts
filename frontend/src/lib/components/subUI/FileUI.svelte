<script lang="ts">
  import { toast } from "svelte-sonner";
  import Button from "$lib/components/ui/button/button.svelte";
  import Badge from "$lib/components/ui/badge/badge.svelte";
  import FileDrop from "$lib/components/ui/input/filedropzone.svelte";
  import Label from "$lib/components/ui/label/label.svelte";
  import { X } from "lucide-svelte";

  let fileUploaded = false;
  let fileNames: string[] = [];
  export let selectedFiles: FileList | null;
  let selectedFilesArray: File[] = [];

  export let fileHandler: (files: FileList) => void;

  function onFilesReceived(event: CustomEvent<{ files: FileList }>) {
    selectedFilesArray = Array.from(event.detail.files);
    selectedFiles = event.detail.files;
    fileNames = selectedFilesArray.map((file) => file.name);
    toast.info(`Files received: ${fileNames.join(", ")}`);
  }

  function startUpload() {
    if (selectedFiles && fileHandler) {
      fileHandler(selectedFiles);
      fileUploaded = true;
    } else {
      toast.error("No file found.");
    }
  }

  function removeFile(fileName: string) {
    selectedFilesArray = selectedFilesArray.filter((file) => file.name !== fileName);
    fileNames = selectedFilesArray.map((file) => file.name);
    const dataTransfer = new DataTransfer();
    selectedFilesArray.forEach((file) => dataTransfer.items.add(file));
    selectedFiles = dataTransfer.files;
  }
</script>

<div class="flex flex-col items-center justify-center gap-4 w-full h-full">
  <p class="text-lg font-semibold">Turn Research into Play! 🎓🧩</p>
  <ul class="text-start border border-zinc-300 rounded-md p-2">
    <li>📄 Upload a research paper</li>
    <li>🧠 Solve word puzzles based on its content</li>
    <li>🎯 Enhance comprehension & retention</li>
  </ul>
  <div>
    <!-- <Label for="file-input">Upload a File</Label> -->
    <FileDrop on:files={onFilesReceived} accept="application/pdf" multiple={false} />
    <Button on:click={startUpload} class="mt-[.3rem] mb-[.3rem] w-full">upload</Button>
    {#if fileNames.length}
      <div class="w-full flex flex-wrap justify-start p-1">
        {#each fileNames as fileName}
          <Badge class="mr-2 mb-2" variant="secondary">
            <span>{fileName}</span>
            <Button size="sm" variant="destructive" class="text-xs ml-1 p-1" onclick={() => removeFile(fileName)}
              ><X class="h-3 w-3" /></Button
            >
          </Badge>
        {/each}
      </div>
    {/if}
  </div>
</div>
