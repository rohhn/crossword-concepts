<script lang="ts">
  import Grid from "./Grid.svelte";
  import data from "./data.json";
  import { Input } from "$lib/components/ui/input/index.js";
  import { Label } from "$lib/components/ui/label/index.js";
  // const getGame = fetch("http://127.0.0.1:8000/upload", {
  //   method: 'POST',
  //   headers: {'content-type': 'multipart/form-data' },
  //   data:
  // })
</script>

<!--
<div class="">
  <Label for="file">Upload Paper</Label>
  <Input id="file" type="file" />
</div>
-->

<Grid grid={data.solution} legend={data.legend} />
