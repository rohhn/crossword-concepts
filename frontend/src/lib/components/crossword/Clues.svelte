<script lang="ts">
  import type { MouseEventHandler } from "svelte/elements";
  import Button from "../ui/button/button.svelte";
  import type { Legend } from "./Crossword.svelte";

  export let questions: Array<Legend>;
  export let currentSelectedQuestionIdx: number | null;

  const highlightQuestionGrid = (direction: string, start: number, end: number) => {};
</script>

<div>
  <h5 class="text-lg text-center font-medium leading-none pb-[.9rem]">Questions</h5>
  <div class="flex flex-col gap-1">
    {#each questions as legendObject, idx}
      <Button
        variant="ghost"
        class="text-start"
        type="button"
        onclick={() => {
          currentSelectedQuestionIdx = idx;
        }}>{idx + 1}. {legendObject.clue}</Button
      >
      <!-- <div role="button" class="p-1 text-sm hover:bg-blue-50 text-wrap" on:click={() => (currentQuestion = idx + 1)}>
      {legendObject.clue}
    </div> -->
    {/each}
  </div>
</div>
