<script lang="ts">
  import Label from "$lib/components/ui/label/label.svelte";
  import Input from "$lib/components/ui/input/input.svelte";
  import Button from "$lib/components/ui/button/button.svelte";
  import { fly } from "svelte/transition";
  import { toast } from "svelte-sonner";

  export let data: WordGuessType;
  const ENDPOINT = "http://127.0.0.1:8000";

  let idx = 0;
  $: question = data.questions.at(idx);
  $: word = data.words.at(idx);

  // Display progress e.g., "1/10"
  $: progress = `${idx + 1}/${data.questions.length}`;

  type Guess = {
    guess: string;
    score: number;
  };

  let guesses: Guess[] = [];
  let inputVal = "";
  let solved = false;

  function enterFn(event: KeyboardEvent) {
    if (event.key === "Enter") {
      submitGuess();
    }
  }

  async function submitGuess() {
    // Prevent duplicate guesses
    if (
      guesses.some(
        (item) => item.guess.toLowerCase() === inputVal.trim().toLowerCase(),
      )
    ) {
      toast.warning("You have already guessed the word");
      inputVal = "";
      return;
    }

    try {
      const response = await fetch(`${ENDPOINT}/similarity`, {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify({
          target: word,
          prediction: inputVal,
        }),
      });
      if (!response.ok) {
        throw new Error("Network response was not ok");
      }
      const result = await response.json();
      const retGuess = { guess: inputVal, score: result.score };
      guesses = [...guesses, retGuess].sort((a, b) => a.score - b.score);
      inputVal = "";
      // Mark as solved if the guess is perfect (score 0)
      if (retGuess.score === 0) {
        solved = true;
        toast.success("Correct! Well done.");
      }
    } catch (error) {
      console.error("Error fetching similarity:", error);
    }
  }

  function nextWord() {
    idx = (idx + 1) % data.questions.length;
    guesses = [];
    inputVal = "";
    solved = false;
  }

  const getBgClass = (score: number) => {
    if (score < 3) return "bg-green-300";
    else if (score < 15) return "bg-yellow-300";
    else return "bg-red-300";
  };
</script>

<div class="max-w-md mx-auto h-full flex flex-col">
  <!-- Display current word progress -->
  <div class="mb-2">
    <div class="text-[.7rem] font-mono italic">{progress}</div>
    <Label>{question} &amp; {word}</Label>
  </div>

  <div class="flex items-center space-x-2">
    <Input
      bind:value={inputVal}
      placeholder="give your best..."
      on:keydown={enterFn}
      disabled={solved}
    />

    {#if solved}
      <Button variant="secondary" on:click={nextWord}>Next Word</Button>
    {:else}
      <Button variant="default" on:click={submitGuess}>guess</Button>
    {/if}
  </div>

  <div class="mt-4 overflow-y-auto h-full p-2 space-y-2 scrollbar-hide">
    {#each guesses as item (item.guess + item.score)}
      <div
        transition:fly={{ x: -50, duration: 300 }}
        class={`p-2 rounded shadow ${getBgClass(item.score)} flex justify-between`}
      >
        <div class="font-semibold">{item.guess}</div>
        {#if item.score === 0}
          <span>🎉</span>
        {:else}
          <div class="font-semibold">{item.score}</div>
        {/if}
      </div>
    {/each}
  </div>
</div>

{#if idx === data.questions.length}
  <!-- set an alert msg -->
{/if}

<style>
  .scrollbar-hide::-webkit-scrollbar {
    display: none;
  }
  .scrollbar-hide {
    -ms-overflow-style: none;
    scrollbar-width: none;
  }
</style>

