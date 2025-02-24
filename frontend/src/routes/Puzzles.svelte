<script lang="ts">
  import { toast } from "svelte-sonner";
  import Crossword, { type CrosswordData } from "$lib/components/crossword/Crossword.svelte";
  import * as Tabs from "$lib/components/ui/tabs/index.js";
  import * as Card from "$lib/components/ui/card/index.js";
  import Button from "$lib/components/ui/button/button.svelte";
  import WordPlay from "$lib/components/wordsearch/WordPlay.svelte";
  import FileDrop from "filedrop-svelte";
  import { filedrop } from "filedrop-svelte";

  import Input from "$lib/components/ui/input/input.svelte";
  import type { ChangeEventHandler } from "svelte/elements";
  import Label from "$lib/components/ui/label/label.svelte";

  let fileUploaded = $state(false);

  let crosswordData: CrosswordData = $state({
    solution: "",
    legend: [],
  });

  const handleFileUpload: ChangeEventHandler<HTMLInputElement> = async (event) => {
    const eventTarget = event.target as HTMLInputElement;

    if (!eventTarget) {
      toast.error("Something went wrong");
      return;
    }
    if (!eventTarget.files) {
      toast.error("No file found!");
      return;
    }
    if (eventTarget.files.length === 1) {
      let file = eventTarget.files[0];
      const formData = new FormData();
      formData.append("file", file);

      try {
        const getGame: Response = await fetch("http://127.0.0.1:8000/puzzle", {
          method: "POST",
          headers: { "content-type": "application/json" },
          body: JSON.stringify({
            query: "make a puzzle on the attention is all you need paper.",
          }),
        });

        if (getGame) {
          fileUploaded = true;
          crosswordData = (await getGame.json()) as CrosswordData;
        }
      } catch (error) {
        console.error(error);
      }
    } else {
      toast.error("File could not be uploaded!");
    }
  };
</script>

{#if !fileUploaded}
  <div class="flex flex-row gap-y-4 justify-center">
    <div class="flex justify-center items-center flex-col gap-y-4">
      <p>Turn Research into Play! 🎓🧩</p>
      <ul class="text-start border border-zinc-300 rounded-md p-2">
        <li>📄 Upload a research paper</li>
        <li>🧠 Solve word puzzles based on its content</li>
        <li>🎯 Enhance comprehension & retention</li>
      </ul>
      <div class="border border-dotted border-zinc-800 rounded-lg">
        <Label for="file-input">Upload a File</Label>
        <Input
          id="file-input"
          class=""
          type="file"
          accept=".pdf"
          placeholder="Upload a file"
          onchange={(event) => {
            handleFileUpload(event);
          }}
        >
          <div class="w-full min-h-[4rem] max-h-[6rem]">
            <div class="min-w-[5rem] max-w-[10rem] flex flex-col justify-center items-center">
              <!-- <FileDrop accept=".pdf" on:filedrop={handleFileUpload} multiple={false} /> -->
            </div>
          </div></Input
        >
        <!-- <p>Upload a file</p> -->
      </div>
    </div>
  </div>
{:else}
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
          <Card.Description>...or maybe word search, if that's your thing.</Card.Description>
        </Card.Header>
        <Card.Content class="w-[65vw] h-[80vh]">
          <div class="text-center">Coming Soon!</div>
          <!-- <WordPlay /> -->
        </Card.Content>
      </Card.Root>
    </Tabs.Content>
  </Tabs.Root>
{/if}
