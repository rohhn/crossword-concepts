<script lang="ts">
  import type { MouseEventHandler } from "svelte/elements";
  import Button from "../ui/button/button.svelte";
  import type { CrosswordLegend } from "./Crossword.svelte";
  import Toggle from "../ui/toggle/toggle.svelte";

  export let questions: Array<CrosswordLegend>;
  export let currentSelectedQuestionIdx: number;
</script>

<div class="w-full">
  <h5 class="static text-lg text-center font-medium leading-none pb-[.9rem]">Questions</h5>
  <div class="grid grid-rows-7 overflow-y-scroll">
    {#each questions as legendObject, idx}
      <!-- svelte-ignore a11y_interactive_supports_focus -->
      <!-- svelte-ignore a11y_click_events_have_key_events -->
      <!-- svelte-ignore a11y_missing_attribute -->
      <a
        role="button"
        class="focus-visible:ring-ring inline-flex items-center justify-start rounded-md text-sm font-medium transition-colors focus-visible:outline-none focus-visible:ring-1 hover:bg-accent hover:text-accent-foreground p-2"
        onclick={() => {
          currentSelectedQuestionIdx = currentSelectedQuestionIdx === idx ? -999 : idx;
        }}>{idx + 1}. {legendObject.clue}</a
      >
    {/each}
  </div>
</div>
