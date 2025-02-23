<script lang="ts">
  import "./app.css";
  import { Link, Router, Route } from "svelte-routing";
  import { Toaster } from "$lib/components/ui/sonner";
  import { User, Puzzle } from "lucide-svelte";
  import Content from "./routes/Content.svelte";
  import Auth from "./routes/Auth.svelte";
  import About from "./routes/About.svelte";
  let url = "";
</script>

<main
  class="border-1 border-black min-h-screen flex items-center justify-center p-0 m-0 flex-col"
>
  <Router {url}>
    <div
      class="flex justify-between items-center w-[75vw] p-0 rounded-md font-mono"
    >
      <h5 class="font-semibold font-mono">crossword concepts</h5>
      <nav class="flex flex-row pb-[1rem] text-md">
        <Link to="/" class="m-[.4rem]">content</Link>
        <Link to="/about" class="m-[.4rem]">about</Link>
        <Link to="/auth" class="m-[.4rem]"><User size="1.5rem" /></Link>
      </nav>
    </div>
    <div>
      <Route path="/auth" component={Auth} />
      <Route path="/" component={Content} />
      <Route path="/about" component={About} />
    </div>
  </Router>
</main>

<Toaster position="bottom-left" />
