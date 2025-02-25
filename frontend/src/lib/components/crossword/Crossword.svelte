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

  export let data: CrosswordData = {
    solution: "",
    legend: [],
  };

  export let currentSelectedQuestionIdx: number = -999;
  export let puzzleSolved: boolean = false;
  export let currentX: number = 0;
  export let currentY: number = 0;

  // TODO: Redirect to Puzzle page if no data is present

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
    // TODO: show the user if the puzzle is correct, Alert Dialog? Freeze the puzzle?
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

  onMount(() => {
    document.addEventListener("keydown", handleKeyDown);
    focusCell(currentX, currentY);
  });

  onDestroy(() => {
    document.removeEventListener("keydown", handleKeyDown);
  });
</script>

<div>
  <div class="flex flex-row flex-wrap justify-between gap-2">
    <div id="crossword" class="row-span-2 justify-center">
      <div class="flex flex-col gap-2">
        <div>
          <Button onclick={resetCrossword}>Reset</Button>
          <Button onclick={revealCrossword}>Reveal</Button>
          <Button
            onclick={() => {
              puzzleSolved = checkSolution();
            }}>Check</Button
          >
        </div>
        <Grid bind:gridSize bind:grid={crosswordGrid} bind:currentSelectedQuestionIdx bind:currentX bind:currentY />
      </div>
    </div>
    <div id="quesitons" class="row-span-1">
      <Clues bind:questions={data.legend} bind:currentSelectedQuestionIdx />
    </div>
  </div>

  <AlertDialog.Root open={puzzleSolved}>
    <AlertDialog.Content>
      <AlertDialog.Header>
        <AlertDialog.Title>Congratulations!</AlertDialog.Title>
        <AlertDialog.Description>You did it!</AlertDialog.Description>
      </AlertDialog.Header>
      <AlertDialog.Footer>
        <AlertDialog.Cancel
          onclick={() => {
            puzzleSolved = false;
          }}>Close</AlertDialog.Cancel
        >
      </AlertDialog.Footer>
    </AlertDialog.Content>
  </AlertDialog.Root>
</div>
