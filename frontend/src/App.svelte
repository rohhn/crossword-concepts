<script lang="ts">
  import "./app.css";
  import { Toaster } from "$lib/components/ui/sonner";
  import { toast } from "svelte-sonner";
  import { Button } from "$lib/components/ui/button";
</script>

<main>
  <Button variant="outline" on:click={() => toast.success("site works")}>
    Invoke
  </Button>
</main>

<Toaster />
