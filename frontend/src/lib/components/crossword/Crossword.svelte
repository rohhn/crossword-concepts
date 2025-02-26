<script module lang="ts">
  export type CrosswordLegend = {
    x: number;
    y: number;
    direction: string;
    clue: string;
    answer: string;
  };

  export type CrosswordData = {
    solution: string;
    legend: Array<CrosswordLegend>;
  };

  export type QuestionInCellData = {
    questionIdx: number;
    direction: string;
  };

  export type SingleCellData = {
    xCoord: number;
    yCoord: number;
    correctValue: string;
    questions: Array<QuestionInCellData>;
    startFor: Array<number>;
    enteredValue: string;
  };

  export type CrosswordGridCells = {
    [name: string]: SingleCellData;
  };
</script>

<script lang="ts">
  import Grid from "$lib/components/crossword/Grid.svelte";
  import Clues from "$lib/components/crossword/Clues.svelte";
  import Button from "$lib/components/ui/button/button.svelte";
  import * as AlertDialog from "$lib/components/ui/alert-dialog/index";
  import { onDestroy, onMount } from "svelte";
  // import { resolveUpload } from "../../../routes/Puzzles.svelte";

  export let selectedFiles: FileList | null;
  export let data: CrosswordData = {
    solution: "",
    legend: [],
  };

  export let currentSelectedQuestionIdx: number = -999;
  export let puzzleSolved: boolean = false;
  export let openAlertDialog: boolean = false;
  export let currentX: number = 0;
  export let currentY: number = 0;

  let puzzle = data.solution
    .trim()
    .split("\n")
    .map((line) => line.trim().split(/\s+/));
  let gridSize = puzzle.length > 0 ? puzzle[0].length : 0;

  const createCellsForCrossword = (data: CrosswordData) => {
    let allCells: CrosswordGridCells = {};
    for (let row = 0; row < gridSize; row++) {
      for (let col = 0; col < gridSize; col++) {
        const singleCell: SingleCellData = {
          xCoord: col,
          yCoord: row,
          correctValue: "",
          questions: [],
          startFor: [],
          enteredValue: "",
        };
        allCells[`${row}-${col}`] = singleCell;
      }
    }

    for (let questionIdx = 0; questionIdx < data.legend.length; questionIdx++) {
      const singleQuestionObj = data.legend[questionIdx];

      const direction = singleQuestionObj.direction;
      const questionInfo: QuestionInCellData = { questionIdx, direction };

      for (let index = 0; index < singleQuestionObj.answer.length; index++) {
        const cellValue = singleQuestionObj.answer[index].toLowerCase().trim();
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

        allCells[`${xCoord}-${yCoord}`].correctValue = cellValue;
        allCells[`${xCoord}-${yCoord}`]["questions"].push(questionInfo);
      }
    }
    return allCells;
  };

  export let crosswordGrid = createCellsForCrossword(data);

  const handleKeyDown = (event: KeyboardEvent) => {
    blurCell(currentX, currentY);
    let newX = currentX;
    let newY = currentY;

    switch (event.key) {
      case "ArrowUp":
        newY = Math.max(0, currentY - 1);
        break;
      case "ArrowDown":
        newY = Math.min(gridSize - 1, currentY + 1);
        break;
      case "ArrowLeft":
        newX = Math.max(0, currentX - 1);
        break;
      case "ArrowRight":
        newX = Math.min(gridSize - 1, currentX + 1);
        break;
    }

    currentX = newX;
    currentY = newY;

    if (isValidCell(currentX, currentY)) {
      focusCell(newX, newY);
    } else {
      return handleKeyDown(event);
    }
  };

  const isValidCell = (x: number, y: number) => {
    const cell = document.querySelector(`input[data-xcoord="${x}"][data-ycoord="${y}"]`);
    return cell;
  };

  const focusCell = (x: number, y: number) => {
    const cellInput = document.querySelector(`input[data-xcoord="${x}"][data-ycoord="${y}"]`);
    if (cellInput) {
      (cellInput as HTMLInputElement).focus();
    }
  };

  const blurCell = (x: number, y: number) => {
    const cellInput = document.querySelector(`input[data-xcoord="${x}"][data-ycoord="${y}"]`);
    if (cellInput) {
      (cellInput as HTMLInputElement).blur();
    }
  };

  $: focusCell(currentX, currentY);

  export const resetCrossword = () => {
    for (const key in crosswordGrid) {
      if (Object.prototype.hasOwnProperty.call(crosswordGrid, key)) {
        crosswordGrid[key] = { ...crosswordGrid[key], enteredValue: "" }; // we have to update the object reference to trigger a change for Svelte
      }
    }
    puzzleSolved = false;
    currentSelectedQuestionIdx = -999;
  };

  export const revealCrossword = () => {
    for (const key in crosswordGrid) {
      if (Object.prototype.hasOwnProperty.call(crosswordGrid, key)) {
        const element = crosswordGrid[key];
        crosswordGrid[key] = { ...crosswordGrid[key], enteredValue: element.correctValue }; // we have to update the object reference to trigger a change for Svelte
      }
    }
  };

  export const checkSolution = () => {
    let isSolved = true;
    let checkIdx = 0;

    let cellKeys = Object.keys(crosswordGrid);
    let totalCells = cellKeys.length;

    while (isSolved && checkIdx < totalCells) {
      if (crosswordGrid[cellKeys[checkIdx]].enteredValue !== crosswordGrid[cellKeys[checkIdx]].correctValue) {
        isSolved = false;
      }
      checkIdx++;
    }
    // console.log("isSolved", isSolved);
    return isSolved;
  };

  // export const regenerateCrossword = () => {
  //   if (selectedFiles) {
  //     resolveUpload(selectedFiles);
  //   }
  // };

  onMount(() => {
    document.addEventListener("keydown", handleKeyDown);
    focusCell(currentX, currentY);
  });

  onDestroy(() => {
    document.removeEventListener("keydown", handleKeyDown);
  });
</script>

<div class="h-full w-full">
  <div class="h-full w-full flex flex-row flex-wrap justify-between overflow-y-auto">
    <div id="crossword" class="w-full md:w-1/2 flex flex-col gap-y-4 h-fit">
      <div class="flex flex-col gap-2">
        <div class="flex justify-center gap-2">
          <Button size="sm" onclick={resetCrossword}>Reset</Button>
          <Button size="sm" onclick={revealCrossword}>Reveal</Button>
          <Button
            size="sm"
            onclick={() => {
              puzzleSolved = checkSolution();
              openAlertDialog = true;
            }}>Check</Button
          >
          <!-- <Button size="sm" onclick={regenerateCrossword}>Re-generate</Button> -->
        </div>
        <Grid bind:gridSize bind:grid={crosswordGrid} bind:currentSelectedQuestionIdx bind:currentX bind:currentY />
      </div>
    </div>
    <div id="quesitons" class="w-full md:w-1/2 p-2 h-full">
      <Clues bind:questions={data.legend} bind:currentSelectedQuestionIdx />
    </div>
  </div>

  <AlertDialog.Root open={openAlertDialog}>
    <AlertDialog.Content>
      {#if puzzleSolved}
        <AlertDialog.Header>
          <AlertDialog.Title>Congratulations!</AlertDialog.Title>
          <AlertDialog.Description>You did it!</AlertDialog.Description>
        </AlertDialog.Header>
      {:else}
        <AlertDialog.Header>
          <AlertDialog.Title>Ooops!</AlertDialog.Title>
          <AlertDialog.Description>u dumb!</AlertDialog.Description>
        </AlertDialog.Header>
      {/if}
      <AlertDialog.Footer>
        <AlertDialog.Cancel
          onclick={() => {
            puzzleSolved = false;
            openAlertDialog = false;
          }}>Close</AlertDialog.Cancel
        >
        {#if puzzleSolved}
          <a href="/puzzle"><Button>New Game</Button></a>
        {/if}
      </AlertDialog.Footer>
    </AlertDialog.Content>
  </AlertDialog.Root>
</div>
