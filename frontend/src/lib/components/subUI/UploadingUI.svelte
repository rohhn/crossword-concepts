<script lang="ts">
  import { LoaderCircle } from "lucide-svelte";
  import { fade } from "svelte/transition";
  import Gif from "$lib/assets/hangover-math.gif";
</script>

<div
  class="absolute top-1/2 left-1/2 transform -translate-x-1/2 -translate-y-1/2 flex flex-col items-center gap-4 justify-center w-full h-full"
  in:fade={{ duration: 300 }}
>
  <h1 class="text-[3rem] font-mono font-semibold">
    Building Game<span class="animate-ellipsis"></span>
  </h1>
  <img
    src={Gif}
    alt="Description of GIF"
    class="w-[30vw] mx-auto mt-[.5rem] rounded-sm"
  />
  <!-- <LoaderCircle class="animate-spin w-10 h-10" /> -->
</div>

<style>
  @keyframes ellipsis {
    0% {
      content: "";
    }
    33% {
      content: ".";
    }
    66% {
      content: "..";
    }
    100% {
      content: "...";
    }
  }
  /* The pseudo-element on the span will animate the ellipsis */
  .animate-ellipsis::after {
    content: "";
    animation: ellipsis 1.5s steps(4, end) infinite;
    display: inline-block;
    width: 2ch; /* Reserve space for 2 characters (adjust as needed) */
  }
</style>

