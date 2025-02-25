<script module lang="ts">
  export type WordGuessType = {
    questions: string[];
    words: string[];
  };
</script>

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

  type Guess = {
    guess: string;
    score: number;
  };

  let guesses: Guess[] = [];
  let inputVal = "";

  function enterFn(event: KeyboardEvent) {
    if (event.key === "Enter") {
      submitGuess();
    }
  }

  async function submitGuess() {
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
      inputVal = ""; // Clear the input after submitting
    } catch (error) {
      console.error("Error fetching similarity:", error);
    }
  }

  const getBgClass = (score: number) => {
    if (score < 3) return "bg-green-300";
    else if (score < 15) return "bg-yellow-300";
    else return "bg-red-300";
  };
</script>

<div class="max-w-md mx-auto">
  <Label>{question} &amp; {word}</Label>
  <div class="flex items-center space-x-2">
    <Input
      bind:value={inputVal}
      placeholder="Give your best"
      on:keydown={enterFn}
    />
    <Button variant="default" on:click={submitGuess}>guess</Button>
  </div>

  <div class="mt-4 overflow-y-auto h-64 p-2 space-y-2 scrollbar-hide">
    {#each guesses as item (item.guess + item.score)}
      <div
        transition:fly={{ x: -50, duration: 300 }}
        class={`p-2 rounded shadow ${getBgClass(item.score)} flex justify-between`}
      >
        <div class="font-semibold">{item.guess}</div>
        <div>{item.score}</div>
      </div>
    {/each}
  </div>
</div>

<style>
  .scrollbar-hide::-webkit-scrollbar {
    display: none;
  }

  /* For IE, Edge and Firefox */
  .scrollbar-hide {
    -ms-overflow-style: none; /* IE and Edge */
    scrollbar-width: none; /* Firefox */
  }
</style>
