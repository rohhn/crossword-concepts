<script lang="ts">
  import Button from "$lib/components/ui/button/button.svelte";
  import Gif from "$lib/assets/travis-scott-fire.gif";
</script>

<div class="grid grid-cols-6">
  <div class="col-span-4 col-start-2">
    <div class="grid grid-rows-5 gap-4">
      <!-- <div class="row-span-2">
        <h1 class="text-2xl text-center">Research Rumble</h1>
      </div> -->
      <div class="row-span-3 row-start-2 text-center flex flex-col gap-y-4">
        <div class="flex flex-col gap-y-2">
          <p>
            Make learning fun with Research Rumble — the app that transforms
            research papers into engaging word puzzles!
          </p>
          <p>
            Simply upload a paper, and we’ll generate interactive challenges to
            help you explore key concepts, terminology, and ideas in a whole new
            way. Whether you're a student, researcher, or lifelong learner, dive
            into academic content like never before.
          </p>

          <p>
            Ready to gamify your research? Upload your paper and start playing!
            🚀
          </p>
        </div>
        <div>
          <a href="/puzzle"><Button type="button">Get Started!</Button></a>

          <img
            src={Gif}
            alt="Description of GIF"
            class="w-[15vw] mx-auto mt-[.5rem] rounded-sm"
          />
        </div>
      </div>
    </div>
  </div>
</div>
