<script lang="ts">
  import "./crossword.css";
  import type { ChangeEventHandler } from "svelte/elements";
  import Input from "../ui/input/input.svelte";
  import { toast } from "svelte-sonner";

  // Component Variables
  export let cellValue: string = ""; // The actual value in the cell
  export let xCoord: number; // the x coordinate of this cell
  export let yCoord: number; // the y coordinate of this cell
  export let startFor: Array<number> = [];
  export let gridSize: number; // the size of the crossword grid
  export let questions: Array<Object>; // An array containing information of the questions contained within this cell
  export let currentSelectedQuestionIdx: number | null; // A global state dervied from the Crossword component to show selected question

  let _isBlankCell: boolean = cellValue.trim() === "" ? true : false;
  cellValue = _isBlankCell ? "" : cellValue;

  let _questionNumbers = questions ? questions.map(({ questionIdx }) => questionIdx) : [];

  const computeBorderClasses = () => {
    const classList = [];
    if (xCoord < gridSize) {
      classList.push("border-e");
    }
    if (yCoord < gridSize) {
      classList.push("border-b");
      // classList.push("border-t");
    }

    return classList.join(" ");
  };

  const checkCellValue: ChangeEventHandler<HTMLInputElement> = (event) => {
    const target = event.target as HTMLInputElement;
    if (!target) {
      toast.error("No target found");
      return;
    }

    const enteredValue = target.value.trim();
    if (!enteredValue) {
      target.setAttribute("data-status", "empty");
    } else {
      if (enteredValue.toLowerCase() === cellValue.toLowerCase()) {
        target.setAttribute("data-status", "correct");
      } else {
        target.setAttribute("data-status", "incorrect");
      }
    }
  };
</script>

<div class="m-0 p-0">
  {#if _isBlankCell}
    <div
      class="bg-zinc-900 w-full h-full border-solid border-slate-400 rounded-none shadow-none drop-shadow-none {computeBorderClasses()}"
    ></div>
  {:else}
    {#if startFor.length > 0}
      <span class="absolute object-left-top text-[0.6rem] text-zinc-700">{startFor.map((i) => i + 1).join(",")}</span>
    {/if}
    <Input
      class=" p-0 text-center rounded-none shadow-none drop-shadow-none {computeBorderClasses()} 
      {_questionNumbers.includes(currentSelectedQuestionIdx) ? 'border-solid border-sky-400 border divide-hidden' : ''}"
      placeholder={cellValue}
      type="text"
      maxlength={1}
      disabled={_isBlankCell}
      onchange={checkCellValue}
      data-xcoord={xCoord}
      data-ycoord={yCoord}
    />
  {/if}
</div>
