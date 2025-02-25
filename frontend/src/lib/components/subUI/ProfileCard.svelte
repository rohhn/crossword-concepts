<script lang="ts">
  import * as Card from "$lib/components/ui/card/index";
  import { Button } from "$lib/components/ui/button";
  import Progress from "../ui/progress/progress.svelte";

  export let name: string;
  export let githubUsername: string;
  $: _githubProfile = {};

  const getGHProfile = () => {
    const _headers = {
      "X-GitHub-Api-Version": "2022-11-28",
      Accept: "application/vnd.github+json",
      Authorization: `Bearer ${import.meta.env.VITE_GITHUB_TOKEN}`,
    };

    fetch(`https://api.github.com/users/${githubUsername}`, {
      method: "get",
      headers: _headers,
    }).then((result) => {
      result.json().then((result) => {
        _githubProfile = { ...result, languages: {}, _languagesTotal: 0 };

        // Gymastics to fetch Languages data from repos that Prateek said is for babies
        // let _ignoreLanguages = ["HTML", "CSS", "SCSS", "PHP", "Jupyter Notebook", "Handlebars"];
        // fetch(_githubProfile.repos_url, {
        //   method: "get",
        //   headers: _headers,
        // }).then((result) => {
        //   result.json().then((result) => {
        //     const repos = result;
        //     repos.forEach((repo) => {
        //       fetch(repo.languages_url, {
        //         method: "get",
        //         headers: _headers,
        //       }).then((result) => {
        //         result.json().then((result) => {
        //           const languages = result;
        //           for (const key in languages) {
        //             if (!_ignoreLanguages.includes(key) && Object.prototype.hasOwnProperty.call(languages, key)) {
        //               if (Object.hasOwn(_githubProfile.languages, key)) {
        //                 _githubProfile.languages[key] = _githubProfile.languages[key] + languages[key];
        //               } else {
        //                 _githubProfile.languages[key] = languages[key];
        //               }
        //               _githubProfile._languagesTotal = _githubProfile._languagesTotal + languages[key];
        //             }
        //           }

        //           //   let _sortedLanguages = [];
        //           //   for (const key in _githubProfile.languages) {
        //           //     _sortedLanguages.push([key, _githubProfile.languages[key]]);
        //           //   }
        //           //   _sortedLanguages.sort((a, b) => {
        //           //     return b[1] - a[1];
        //           //   });
        //           //   //   _sortedLanguages = _sortedLanguages.slice(-3);
        //           //   console.log(_sortedLanguages);
        //           _githubProfile = { ..._githubProfile, languages: _githubProfile.languages };
        //         });
        //       });
        //     });
        //   });
        // });
      });
    });
  };

  $: getGHProfile();
</script>

<div class="flex flex-col justify-center text-center items-center">
  <Card.Root class="w-full">
    <Card.Header>
      <Card.Title>{name}</Card.Title>
      <Card.Description>{_githubProfile.bio}</Card.Description>
    </Card.Header>
    <Card.Content>
      <div class="flex flex-col gap-y-2 justify-center items-center">
        <!-- svelte-ignore a11y_img_redundant_alt -->
        <img alt="profile photo" src={_githubProfile.avatar_url} class="rounded-full h-24 w-24" />
        <div id="social links" class="flex flex-row gap-x-2">
          <a aria-label="something" href={_githubProfile.html_url} target="_blank"
            ><img
              alt="github"
              src="https://raw.githubusercontent.com/devicons/devicon/ca28c779441053191ff11710fe24a9e6c23690d6/icons/github/github-original.svg"
              height="20px"
              width="20px"
            /></a
          >

          {#if _githubProfile.blog}
            <a aria-label="something" href={_githubProfile.html_url} target="_blank">
              <img
                alt="github"
                src="https://img.icons8.com/?size=100&id=3685&format=png&color=000000"
                height="20px"
                width="20px"
              />
            </a>
          {/if}
        </div>
        {#if false}
          <!--Show Languages from Github-->
          <Card.Root class="w-full mt-4">
            <Card.Header>
              <Card.Title>GitHub Languages</Card.Title>
            </Card.Header>
            <Card.Content>
              <div class="flex flex-col gap-y-2">
                {#each Object.entries(_githubProfile.languages) as [lang_name, val]}
                  <div class="grid grid-cols-3 gap-x-2 items-center">
                    <div class="col-span-1 text-end">{lang_name}</div>

                    <div class="col-span-2">
                      <div class="flex flex-row gap-x-1 items-center">
                        <Progress value={val} max={_githubProfile._languagesTotal} class="w-[80%]"></Progress>
                        <p class="text-xs">
                          {parseFloat(String((val / _githubProfile._languagesTotal) * 100)).toFixed(1)}
                        </p>
                      </div>
                    </div>
                  </div>
                {/each}
              </div>
            </Card.Content>
          </Card.Root>
        {/if}
      </div>
    </Card.Content>
  </Card.Root>
</div>
