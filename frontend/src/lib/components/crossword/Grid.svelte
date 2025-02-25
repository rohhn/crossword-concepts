<script lang="ts">
  import { toast } from "svelte-sonner";
  import type { CrosswordGridCells, CrosswordLegend } from "./Crossword.svelte";
  import Cell from "./Cell.svelte";

  export let gridSize: number;
  export let grid: CrosswordGridCells;
  export let currentSelectedQuestionIdx: number;
  export let currentX: number;
  export let currentY: number;
</script>

<div
  class="grid border-collapse"
  style="grid-template-columns: repeat({gridSize}, 2rem);"
>
  {#each Object.entries(grid) as [_, cell]}
    <Cell
      bind:cell
      bind:gridSize
      bind:currentSelectedQuestionIdx
      bind:currentX
      bind:currentY
    ></Cell>
  {/each}
</div>
