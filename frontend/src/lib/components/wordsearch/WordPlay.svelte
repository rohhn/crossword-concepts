<script lang="ts">
  import type { Legend } from "../crossword/Crossword.svelte";
  import Grid from "../crossword/Grid.svelte";

  export let grid: Object;
  export let legend: Legend;
</script>

<Grid bind:grid legend={data_.legend} drawNumbers={false} />
