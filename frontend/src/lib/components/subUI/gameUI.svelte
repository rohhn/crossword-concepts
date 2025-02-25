<script module lang="ts">
  export type GameType = {
    file: string;
    game: CrosswordData;
    guess_game: WordGuessType;
  };
</script>

<script lang="ts">
  import Crossword, {
    type CrosswordData,
  } from "$lib/components/crossword/Crossword.svelte";
  import * as Tabs from "$lib/components/ui/tabs/index.js";
  import * as Card from "$lib/components/ui/card/index.js";
  import WordGuess, {
    type WordGuessType,
  } from "$lib/components//wordguess/WordGuess.svelte";

  export let gameData: GameType;
  let crosswordData = gameData.game;
  let wordguessData = gameData.guess_game;
  console.log("super data");
  console.log(gameData);
</script>

<Tabs.Root value="crossword" class="w-[75vw] h-[90vh] mx-auto">
  <Tabs.List class="grid w-[40vw] grid-cols-2 mx-auto">
    <Tabs.Trigger value="crossword">Crossword 🧩</Tabs.Trigger>
    <Tabs.Trigger value="word-search">Guess the word 🔎</Tabs.Trigger>
  </Tabs.List>
  <Tabs.Content value="crossword">
    <Card.Root>
      <Card.Header>
        <Card.Description>play a game of crossword...</Card.Description>
      </Card.Header>
      <!-- hardcoded height to cuz Card compoent auto adjusts to height, wordguess component shrinks -->
      <Card.Content class="w-full h-[75wh] px-4">
        <Crossword bind:data={crosswordData} />
      </Card.Content>
    </Card.Root>
  </Tabs.Content>
  <Tabs.Content value="word-search">
    <Card.Root>
      <Card.Header>
        <Card.Description
          >...or maybe word guess, if that's your thing.</Card.Description
        >
      </Card.Header>
      <Card.Content class="w-full h-[75vh] px-4">
        <WordGuess bind:data={wordguessData} />
      </Card.Content>
    </Card.Root>
  </Tabs.Content>
</Tabs.Root>
