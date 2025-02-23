<script lang="ts">
  import "./app.css";
  import { Toaster } from "$lib/components/ui/sonner";
  import Content from "./Content.svelte";
</script>

<main
  class="border-1 border-black min-h-screen flex items-center justify-center p-0 m-0"
>
  <Content />
</main>

<Toaster position="bottom-left" />
