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

<main class="">
  <Router
    {url}
    viewtransition={() => ({
      fn: fade,
      duration: 100,
    })}
  >
    <div id="main" class="h-screen px-8 md:px-40 py-4">
      <!-- sm:px-8 md:px-40 py-4 flex flex-col sm:gap-y-8 md:gap-y-8 -->
      <div id="navbar" class="static flex justify-between items-center font-mono h-[5vh]">
        <h5 class="font-semibold font-mono">
          <Link to="/">Crossword Concepts</Link>
        </h5>
        <nav class="flex flex-row text-sm items-center font-semibold gap-3">
          <Link to="/puzzle">play</Link>
          <Link to="/about">about</Link>
        </nav>
      </div>
      <div id="game-app" class="w-full h-[90vh]">
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
    </div>
  </Router>
</main>

<Toaster position="bottom-left" />
