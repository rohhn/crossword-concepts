<script lang="ts">
  import "./crossword.css";
  import type { ChangeEventHandler } from "svelte/elements";
  import Input from "../ui/input/input.svelte";
  import { toast } from "svelte-sonner";
  import type { QuestionInCellData, SingleCellData } from "./Crossword.svelte";
  import type { FormInputEvent } from "../ui/input";

  // Component Variables
  export let cell: SingleCellData;

  export let gridSize: number; // the size of the crossword grid
  export let currentSelectedQuestionIdx: number; // A global state dervied from the Crossword component to show selected question
  export let currentX: number;
  export let currentY: number;

  let _isBlankCell: boolean = cell.correctValue.trim() === "" ? true : false;
  // correctValue = _isBlankCell ? "" : correctValue;

  let _questionNumbers = cell.questions ? cell.questions.map(({ questionIdx }) => questionIdx) : [];

  const computeBorderClasses = () => {
    const classList = [];
    if (cell.xCoord < gridSize) {
      classList.push("border-e");
    }
    if (cell.yCoord < gridSize) {
      classList.push("border-b");
      // classList.push("border-t");
    }

    return classList.join(" ");
  };

  const clearCellValue = (event: FocusEvent) => {
    const target = event.target as HTMLInputElement;
    if (target) {
      target.value = "";
    }
  };

  const checkCellValue: ChangeEventHandler<HTMLInputElement> = (event) => {
    const target = event.target as HTMLInputElement;
    if (!target) {
      toast.error("No target found");
      return;
    }

    const inputValue = target.value.trim();
    if (!inputValue) {
      target.setAttribute("data-status", "empty");
    } else {
      if (inputValue.toLowerCase() === cell.correctValue.toLowerCase()) {
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
    {#if cell.startFor.length > 0}
      <span class="absolute object-left-top text-[0.6rem] text-zinc-700"
        >{cell.startFor.map((i) => i + 1).join(",")}</span
      >
    {/if}
    <Input
      class="p-0 text-center rounded-none shadow-none drop-shadow-none caret-transparent {computeBorderClasses()} 
      {_questionNumbers.includes(currentSelectedQuestionIdx) ? 'bg-amber-200' : ''}
      focus:bg-sky-100 "
      type="text"
      maxlength={1}
      disabled={_isBlankCell}
      onchange={checkCellValue}
      onclick={() => {
        currentX = cell.xCoord;
        currentY = cell.yCoord;
      }}
      data-xcoord={cell.xCoord}
      data-ycoord={cell.yCoord}
      bind:value={cell.enteredValue}
      on:focus={clearCellValue}
    />
  {/if}
</div>
