<script lang="ts">
  import Grid from "./Grid.svelte";
  import data_ from "./data_1.json";
</script>

<Grid grid={data_.word_find} legend={data_.legend} drawNumbers={false} />
