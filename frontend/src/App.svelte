<script lang="ts">
  import "./app.css";
  import { Link, Router, Route } from "svelte-routing";
  import { Toaster } from "$lib/components/ui/sonner";
  import Home from "./routes/Home.svelte";
  import Puzzles from "./routes/Puzzles.svelte";
  import About from "./routes/About.svelte";
  import { fade, slide } from "svelte/transition";
  export let url = "";
</script>

<main class="border-1 border-black min-h-screen p-0 mx-8 my-2 flex-col">
  <Router
    {url}
    viewtransition={() => ({
      fn: fade,
      duration: 100,
    })}
  >
    <div
      class="static flex justify-between items-center rounded-md font-mono h-[64px]"
    >
      <h5 class="font-semibold font-mono">
        <a href="/">Crossword Concepts</a>
      </h5>
      <nav class="flex flex-row pb-[1rem] text-sm">
        <Link to="/puzzle" class="m-[.4rem]">play</Link>
        <Link to="/about" class="m-[.4rem]">about</Link>
      </nav>
    </div>
    <div class="w-full">
      <Route path="/">
        <Home />
      </Route>
      <Route path="/about">
        <About />
      </Route>
      <Route path="/puzzle">
        <Puzzles />
      </Route>
    </div>
  </Router>
</main>

<Toaster position="bottom-left" />
