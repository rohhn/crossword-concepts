<script module lang="ts">
  export type GameType = {
    file: string;
    game: CrosswordData;
    guess_game: WordGuessType;
  };
</script>

<script lang="ts">
  import Crossword, { type CrosswordData } from "$lib/components/crossword/Crossword.svelte";
  import * as Tabs from "$lib/components/ui/tabs/index.js";
  import * as Card from "$lib/components/ui/card/index.js";
  import WordGuess, { type WordGuessType } from "$lib/components//wordguess/WordGuess.svelte";

  export let gameData: GameType;
  export let selectedFiles: FileList | null;

  let crosswordData = gameData.game;
  let wordguessData = gameData.guess_game;
  console.log("super data");
  console.log(gameData);
</script>

<Tabs.Root class="w-full h-full">
  <Tabs.List class="grid grid-cols-2 w-full md:w-5/7">
    <Tabs.Trigger value="crossword">Crossword 🧩</Tabs.Trigger>
    <Tabs.Trigger value="word-search">Guess the word 🔎</Tabs.Trigger>
  </Tabs.List>
  <Tabs.Content value="crossword" class="h-full w-full">
    <Card.Root class="w-full" style="height:90%">
      <!-- hardcoded height to cuz Card compoent auto adjusts to height, wordguess component shrinks -->
      <Card.Content class="w-full h-full px-4">
        <Crossword bind:data={crosswordData} bind:selectedFiles />
      </Card.Content>
    </Card.Root>
  </Tabs.Content>
  <Tabs.Content class="h-full w-full" value="word-search">
    <Card.Root class="w-full" style="height:90%">
      <Card.Content class="w-full h-full px-4">
        <WordGuess bind:data={wordguessData} />
      </Card.Content>
    </Card.Root>
  </Tabs.Content>
</Tabs.Root>
