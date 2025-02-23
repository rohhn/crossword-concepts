<script lang="ts">
  type Legend = {
    x: number;
    y: number;
    direction: string;
    clue: string;
  };

  import { toast } from "svelte-sonner";
  export let grid: string;
  export let legend: Array<Legend>;
  export let drawNumbers: boolean = true;

  let counter = 0;
  let positions = legend.map(({ x, y }: Legend) => ({
    x,
    y,
    idx: (counter += 1),
  }));

  let questions = legend.map(({ clue }: Legend) => clue);
  console.log(positions);
  console.log("questions");
  console.log(questions);

  // FIXME: overlaps not considered at box superscript
  const computeQuestionNumber = (idx: number, jdx: number) => {
    for (const pos of positions) {
      if (pos.y === idx + 1 && pos.x === jdx + 1 && drawNumbers) {
        return pos.idx;
      }
    }

    return "";
  };

  let puzzle = grid
    .trim()
    .split("\n")
    .map((line) => line.trim().split(/\s+/));

  let numCols = puzzle.length > 0 ? puzzle[0].length : 0;
  let currentQuestion = 0;
</script>

<div class="flex justify-between p-0 w-full">
  <div class="grid" style="grid-template-columns: repeat({numCols}, 2rem);">
    {#each puzzle as row, idx}
      {#each row as ch, jdx}
        <div class="m-0 p-0">
          {#if ch === "."}
            <div class="w-[30px] h-[30px]"></div>
          {:else}
            {@const sup = computeQuestionNumber(idx, jdx)}
            <div class="relative inline-block" data-sup={sup}>
              <input
                maxlength="1"
                class="w-[30px] h-[30px] flex justify-center text-center items-center cursor-pointer hover:bg-red-50 focus:outline-none text-[1rem]"
                placeholder={ch}
                class:bg-green-100={currentQuestion === sup}
                style="caret-color: transparent;"
                on:click|preventDefault={() =>
                  toast.info("event created", {
                    description: `at ${idx + 1}, ${jdx + 1}`,
                  })}
              />
            </div>
          {/if}
        </div>
      {/each}
    {/each}
  </div>

  <div class="pl-[2rem] flex-1 h-[60vh] w-[100%]">
    <h5 class="text-sm font-medium leading-none pb-[.9rem]">Questions</h5>
    <div class="h-full w-[100%] overflow-y-scroll">
      {#each questions as q, idx}
        <div
          role="button"
          class="p-1 text-sm hover:bg-blue-50 text-wrap"
          on:click={() => (currentQuestion = idx + 1)}
        >
          {q}
        </div>
      {/each}
    </div>
  </div>
</div>

<style>
  .relative {
    position: relative;
  }
  .relative::before {
    content: attr(data-sup);
    position: absolute;
    top: 0rem;
    left: 0rem;
    font-size: 0.1rem;
    font-weight: bold;
    pointer-events: none;
  }
</style>
