<script module lang="ts">
  export type Legend = {
    x: number;
    y: number;
    direction: string;
    clue: string;
    answer: string;
  };

  export type CrosswordData = {
    solution: string;
    legend: Array<Legend>;
  };
</script>

<script lang="ts">
  import Grid from "./Grid.svelte";
  import Clues from "./Clues.svelte";

  export let data: CrosswordData = {
    solution: "",
    legend: [],
  };

  let currentSelectedQuestionIdx: number | null = null;

  // if (typeof data === "string") {
  //   data = JSON.parse(data) as CrosswordData;
  // }

  let puzzle = data.solution
    .trim()
    .split("\n")
    .map((line) => line.trim().split(/\s+/));
  let gridSize = puzzle.length > 0 ? puzzle[0].length : 0;

  let allCells: Object = {};
  for (let row = 0; row < gridSize; row++) {
    for (let col = 0; col < gridSize; col++) {
      const singleCell = {
        xCoord: row,
        yCoord: col,
        cellContent: "",
        // direction: undefined,
        // questionIdx: [],
        questions: [],
        startFor: [],
      };
      allCells[`${row}-${col}`] = singleCell;
    }
  }

  for (let questionIdx = 0; questionIdx < data.legend.length; questionIdx++) {
    const singleQuestionObj = data.legend[questionIdx];

    const direction = singleQuestionObj.direction;
    const questionInfo = { questionIdx, direction, startFor: [] };

    for (let index = 0; index < singleQuestionObj.answer.length; index++) {
      const cellValue = singleQuestionObj.answer[index];
      let xCoord = singleQuestionObj.x - 1;
      let yCoord = singleQuestionObj.y - 1;

      if (direction == "down") {
        yCoord += index;
      } else {
        xCoord += index;
      }
      if (cellValue && index === 0) {
        allCells[`${xCoord}-${yCoord}`].startFor.push(questionIdx);
      }

      allCells[`${xCoord}-${yCoord}`].cellContent = cellValue;
      allCells[`${xCoord}-${yCoord}`]["questions"].push(questionInfo);
    }
  }

  // let puzzleQuestions = data.legend.map(({ clue }: Legend) => clue);
</script>

<div class="">
  <div class="flex flex-row flex-wrap justify-between gap-2">
    <div id="crossword" class="row-span-2 justify-center">
      <Grid bind:gridSize bind:grid={allCells} bind:currentSelectedQuestionIdx />
    </div>
    <div id="quesitons" class="row-span-1">
      <Clues bind:questions={data.legend} bind:currentSelectedQuestionIdx />
    </div>
  </div>
</div>
