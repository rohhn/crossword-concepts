<script lang="ts">
  import { createEventDispatcher } from "svelte";
  import { Upload } from "lucide-svelte";
  // Create an event dispatcher to send out events (like file selection)
  const dispatch = createEventDispatcher();

  // Props to customize file types and whether multiple files can be selected
  export let accept: string = "";
  export let multiple: boolean = false;

  // Called when files are dropped onto the zone
  function handleDrop(event: DragEvent) {
    event.preventDefault();
    event.stopPropagation();
    const files = event.dataTransfer?.files;
    if (files) {
      dispatch("files", { files });
    }
  }

  // Allow drop by preventing default behavior
  function handleDragOver(event: DragEvent) {
    event.preventDefault();
    event.stopPropagation();
  }

  // Called when the hidden input changes (user selects files via dialog)
  function handleChange(event: Event) {
    const input = event.target as HTMLInputElement;
    if (input.files) {
      dispatch("files", { files: input.files });
    }
  }
</script>

<!--
  The outer div is styled as a drop zone with a dashed border and rounded corners.
  The native file input is absolutely positioned, transparent, and covers the entire area,
  allowing users to click anywhere on the drop zone to open the file dialog.
-->
<div
  class="relative flex items-center justify-center border-2 border-dashed border-gray-400 rounded-md p-4 cursor-pointer"
  on:dragover={handleDragOver}
  on:drop={handleDrop}
>
  <input
    type="file"
    {accept}
    {multiple}
    on:change={handleChange}
    class="absolute inset-0 w-full h-full opacity-0 cursor-pointer"
  />
  <p class="flex items-center pointer-events-none text-gray-600">
    <span class="pr-[1rem]"> Drop files here or click to select </span>
    <Upload />
  </p>
</div>

