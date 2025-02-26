<script lang="ts">
  import Button from "$lib/components/ui/button/button.svelte";
  import Gif from "$lib/assets/travis-scott-fire.gif";
</script>

<div class="flex h-full flex-col justify-center items-center text-center gap-y-4">
  <p>Make learning fun with Research Rumble — the app that transforms research papers into engaging word puzzles!</p>
  <p>
    Simply upload a paper, and we’ll generate interactive challenges to help you explore key concepts, terminology, and
    ideas in a whole new way. Whether you're a student, researcher, or lifelong learner, dive into academic content like
    never before.
  </p>

  <p>Ready to gamify your research? Upload your paper and start playing! 🚀</p>

  <a href="/puzzle" class="text-center"><Button type="button">Get Started!</Button></a>
  <img src={Gif} alt="Description of GIF" class="h-1/3 mx-auto rounded-sm" />
</div>
