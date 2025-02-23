<script lang="ts">
  import { toast } from "svelte-sonner";
  import Crossword from "$lib/components/crossword/Crossword.svelte";
  import * as Tabs from "$lib/components/ui/tabs/index.js";
  import * as Card from "$lib/components/ui/card/index.js";
  import Button from "$lib/components/ui/button/button.svelte";
  import WordPlay from "$lib/components/crossword/WordPlay.svelte";

  async function dummyWait() {
    toast.loading("Loading...");
    await new Promise((resolve) => setTimeout(resolve, 4000));
    toast.success("Done!");
  }
</script>

<Tabs.Root value="crossword" class="w-[65vw] h-[90vh]">
  <Tabs.List class="grid w-full grid-cols-2">
    <Tabs.Trigger value="crossword">Crossword 🧩</Tabs.Trigger>
    <Tabs.Trigger value="password">Word Play 🔎</Tabs.Trigger>
  </Tabs.List>
  <Tabs.Content value="crossword">
    <Card.Root>
      <Card.Header>
        <Card.Description>play a game of crossword...</Card.Description>
      </Card.Header>
      <Card.Content class="w-[65vw] h-[80vh]">
        <Crossword />

        <Button variant="outline" on:click={dummyWait}>Invoke</Button>
      </Card.Content>
    </Card.Root>
  </Tabs.Content>
  <Tabs.Content value="password">
    <Card.Root>
      <Card.Header>
        <Card.Description>
          ...or maybe word search, if that's your thing.
        </Card.Description>
      </Card.Header>
      <Card.Content class="w-[65vw] h-[80vh]">
        <WordPlay />
      </Card.Content>
    </Card.Root>
  </Tabs.Content>
</Tabs.Root>
