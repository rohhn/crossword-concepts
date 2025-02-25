<script lang="ts">
  import Crossword, {
    type CrosswordData,
  } from "$lib/components/crossword/Crossword.svelte";
  import * as Tabs from "$lib/components/ui/tabs/index.js";
  import * as Card from "$lib/components/ui/card/index.js";
  import Button from "$lib/components/ui/button/button.svelte";
  import WordPlay from "$lib/components/wordsearch/WordPlay.svelte";

  import Input from "$lib/components/ui/input/input.svelte";
  import type { ChangeEventHandler } from "svelte/elements";
  import Label from "$lib/components/ui/label/label.svelte";

  export let crosswordData: CrosswordData;
</script>

<Tabs.Root value="crossword" class="w-full h-[90vh]">
  <Tabs.List class="grid w-full grid-cols-2">
    <Tabs.Trigger value="crossword">Crossword 🧩</Tabs.Trigger>
    <Tabs.Trigger value="word-search">Word Search 🔎</Tabs.Trigger>
  </Tabs.List>
  <Tabs.Content value="crossword">
    <Card.Root>
      <Card.Header>
        <Card.Description>play a game of crossword...</Card.Description>
      </Card.Header>
      <Card.Content class="w-full h-full px-4">
        <Crossword bind:data={crosswordData} />
      </Card.Content>
    </Card.Root>
  </Tabs.Content>
  <Tabs.Content value="word-search">
    <Card.Root>
      <Card.Header>
        <Card.Description
          >...or maybe word search, if that's your thing.</Card.Description
        >
      </Card.Header>
      <Card.Content class="w-[65vw] h-[80vh]">
        <div class="text-center">Coming Soon!</div>
      </Card.Content>
    </Card.Root>
  </Tabs.Content>
</Tabs.Root>
