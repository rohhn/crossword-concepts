<script lang="ts">
  import { toast } from "svelte-sonner";
  import ProfileCard from "$lib/components/subUI/ProfileCard.svelte";
</script>

<div class="grid grid-cols-4 gap-4">
  <div class="col-start-2">
    <ProfileCard name="Rohan Deshmukh" githubUsername="rohhn"></ProfileCard>
  </div>
  <div><ProfileCard name="Prateek Pravanjan" githubUsername="dunkeln"></ProfileCard></div>
</div>
