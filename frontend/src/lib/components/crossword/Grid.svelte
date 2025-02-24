<script lang="ts">
  import { toast } from "svelte-sonner";
  import type { Legend } from "./Crossword.svelte";
  import Cell from "./Cell.svelte";

  export let gridSize: number;
  export let grid: Object;
  // export let legend: Array<Legend>;
  // export let drawNumbers: boolean = true;
  export let currentSelectedQuestionIdx: number | null;

  // let counter = 0;
  // let positions = legend.map(({ x, y }: Legend) => ({
  //   x,
  //   y,
  //   idx: (counter += 1),
  // }));

  // console.log(positions);

  // FIXME: overlaps not considered at box superscript
  // const computeQuestionNumber = (idx: number, jdx: number) => {
  //   for (const pos of positions) {
  //     if (pos.y === idx + 1 && pos.x === jdx + 1 && drawNumbers) {
  //       return pos.idx;
  //     }
  //   }
  //   return null;
  // };

  const computeQuestionNumber = (rowIdx: number, colIdx: number) => {
    return 0;
  };

  // let puzzle = grid
  //   .trim()
  //   .split("\n")
  //   .map((line) => line.trim().split(/\s+/));

  // let numCols = puzzle.length > 0 ? puzzle[0].length : 0;
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
