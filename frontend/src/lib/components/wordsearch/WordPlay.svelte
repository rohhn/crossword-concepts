<script lang="ts">
  import type { CrosswordLegend } from "../crossword/Crossword.svelte";
  import Grid from "../crossword/Grid.svelte";

  export let grid: Object;
  export let legend: CrosswordLegend;
</script>

<Grid bind:grid legend={data_.legend} drawNumbers={false} />
