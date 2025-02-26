<script lang="ts">
  import { toast } from "svelte-sonner";
  import ProfileCard from "$lib/components/subUI/ProfileCard.svelte";
</script>

<div class="h-full flex items-center justify-center text-center">
  <div class="flex flex-col flex-wrap justify-between gap-4">
    <div class="">
      <ProfileCard name="Rohan Deshmukh" githubUsername="rohhn"></ProfileCard>
    </div>
    <div class=""><ProfileCard name="Prateek Pravanjan" githubUsername="dunkeln"></ProfileCard></div>
  </div>
</div>
