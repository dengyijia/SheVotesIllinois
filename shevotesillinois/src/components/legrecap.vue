<template>
  <div class="home">
  <b-container class="container-fluid">
    <navbar></navbar>
    <b-carousel
      background="#ababab">
      <!-- Text slides with image -->
      <b-carousel-slide>
        <template v-slot:img>
          <img src="./1200px-Illinois_State_Capitol_pano.jpg"/>
        </template>
        <h1 style="color: white">Current and Past Initatives</h1>
        <!--eslint-disable-next-line-->
        <p style="color: white">Showcasing successful and upcoming efforts to improve women's lives in Illinois</p>
      </b-carousel-slide>
    </b-carousel>

    <b-jumbotron>
      <template v-slot:header>Past Legislation</template>

      <template v-slot:lead>
        These bills became law in the 2019 spring session due to your hard work and advocacy.
      </template>

      <!--eslint-disable-next-line-->
      <b-button variant="warning" href="./hb3394.vue"> Yeet<img src="./title_image.jpg" /> </b-button>
      <b-button variant="primary" href="#">Reproductive Health Act</b-button>
      <b-button variant="primary" href="#">Reproductive Health Act</b-button>
      <b-button variant="primary" href="#">Reproductive Health Act</b-button>
      <b-button variant="primary" href="#">Reproductive Health Act</b-button>
      <b-button variant="primary" href="#">Reproductive Health Act</b-button>
      <b-button variant="primary" href="#">Reproductive Health Act</b-button>
      <b-button variant="primary" href="#">Reproductive Health Act</b-button>
      <b-button variant="primary" href="#">Reproductive Health Act</b-button>
      <b-button variant="primary" href="#">Reproductive Health Act</b-button>
      <b-button variant="primary" href="#">Reproductive Health Act</b-button>
      <div v-for="(section, index) in Object.keys(entries)" :key="index" class="group">
        <h2 class="center">{{section}}</h2>
        <div class="section" v-for="entry in entries[section]" :key="entry.id">
          <b-button variant="primary" href="#">Reproductive Health Act</b-button>
          <div class="entry">
            <h3 @click="$router.push({name: entry.id})">
              {{entry.title}}
              <span class="subtitle">{{entry.date}}</span>
            </h3>
            <p>{{entry.description}}</p>
          </div>
        </div>
      </div>
    </b-jumbotron>

    <b-jumbotron>
      <template v-slot:header>What we do</template>

      <template v-slot:lead>
        Our work focuses on three things: voting, education,
        and getting more women involved in politics. We are a grassroots team of
        Illinois women working to engage a new wave of voters, community members,
        activists, and politicians.
      </template>

      <hr class="my-4">

      <b-row center>
        <b-col>
          <b-card
              title="Voting"
              tag="article"
              style="max-width: 20rem;"
              class="mb-2">
              <b-card-text>
                  Make sure all women can vote in every state and local election
              </b-card-text>

              <b-button
              squared variant="outline-secondary"
              href="#">Become Aware</b-button>
            </b-card>
        </b-col>
        <b-col>
          <b-card
            title="Education"
            tag="article"
            style="max-width: 20rem;"
            class="mb-2">
            <b-card-text>
              Ensure our elected officials and candidates for office understand
              the issues most important to Illinois women
            </b-card-text>

            <b-button
                squared variant="outline-secondary"
                href="#">Be Informed</b-button>
          </b-card>
        </b-col>
        <b-col>
          <b-card
            title="Engagement"
            tag="article"
            style="max-width: 20rem;"
            class="mb-2">
            <b-card-text>
              Support women entering into state and local politic
            </b-card-text>
            <b-button
                    squared variant="outline-secondary"
                    href="#">Get Active</b-button>
          </b-card>
        </b-col>
      </b-row>
    </b-jumbotron>
    <b-jumbotron>
      <template v-slot:header>History</template>

      <template v-slot:lead>
        She Votes Illinois was founded when a few women got together over coffee in 2017.
        We were disappointed that there were no women running for governor of
        Illinois—especially since Illinois has never had a woman serve as governor.
      </template>

      <hr class="my-4">

      <p>
        More than 500 people attended our inaugural event, where we questioned and
         challenged the candidates on the record on a wide range of issues that
         included violence against women, equal pay for equal work, and access
         to choice in healthcare.
      </p>

      <b-button variant="primary" href="#">More history</b-button>
    </b-jumbotron>
  </b-container>
  </div>
</template>

<script>
import BLOGENTRIES from '@/assets/blog_posts.json';

export default {
  name: 'home',
  computed: {
    entries() {
      return BLOGENTRIES;
    },
  },
};
</script>
