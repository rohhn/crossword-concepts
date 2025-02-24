<script lang="ts">
  import "./app.css";
  import { Link, Router, Route } from "svelte-routing";
  import { Toaster } from "$lib/components/ui/sonner";
  import { User, Puzzle } from "lucide-svelte";
  import Home from "./routes/Home.svelte";
  import Puzzles from "./routes/Puzzles.svelte";
  import Auth from "./routes/Auth.svelte";
  import About from "./routes/About.svelte";
  let url = "";
</script>

<main class="border-1 border-black min-h-screen p-0 mx-8 my-2 flex-col">
  <Router {url}>
    <div class="static flex justify-between items-center rounded-md font-mono h-[64px]">
      <h5 class="font-semibold font-mono"><a href="/">Crossword Concepts</a></h5>
      <nav class="flex flex-row pb-[1rem] text-md">
        <Link to="/puzzle" class="m-[.4rem]">Puzzles</Link>
        <Link to="/about" class="m-[.4rem]">About</Link>
        <Link to="/auth" class="m-[.4rem]"><User size="1.5rem" /></Link>
      </nav>
    </div>
    <div class="w-full">
      <Route path="/" component={Home} />
      <Route path="/auth" component={Auth} />
      <Route path="/puzzle" component={Puzzles} />
      <Route path="/about" component={About} />
    </div>
  </Router>
</main>

<Toaster position="bottom-left" />
