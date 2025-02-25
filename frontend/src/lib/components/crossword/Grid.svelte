<script lang="ts">
  import { toast } from "svelte-sonner";
  import type { Legend } from "./Crossword.svelte";
  import Cell from "./Cell.svelte";

  export let gridSize: number;
  export let grid: Object;
  export let legend: Array<Legend>;
  // export let drawNumbers: boolean = true;
  export let currentSelectedQuestionIdx: number | null;
  console.log(legend);
</script>

<div class="grid" style="grid-template-columns: repeat({gridSize}, 2rem);">
  {#each Object.entries(grid) as [_, cellObject]}
    <Cell
      xCoord={cellObject.xCoord}
      yCoord={cellObject.yCoord}
      cellValue={cellObject.cellContent}
      questions={cellObject.questions}
      {gridSize}
      bind:currentSelectedQuestionIdx
      startFor={cellObject.startFor}
    ></Cell>
  {/each}
</div>
