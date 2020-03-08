<template>
  <b-container>
    <b-carousel
      background="#ababab">
      <!-- Text slides with image -->
      <b-carousel-slide>
        <template v-slot:img>
          <img src="./title_image.jpg"/>
        </template>
        <h1 style="color: black; font-family: Times">She Votes Illinois</h1>
        <p style="color: black">Fighting for a state where all women experience justice, equity,
        and political representation</p>
      </b-carousel-slide>
    </b-carousel>

    <b-jumbotron bg-variant="transparent">
      <template v-slot:header>
        <p style="font-family: serif;">Who we are</p></template>

      <template v-slot:lead>
        She Votes Illinois is a statewide political action committee aimed at
           highlighting the importance of women’s voices in elections, government, and
            policymaking.
      </template>

      <b-button variant="info" href="#">Meet our members!</b-button>
    </b-jumbotron>

    <b-jumbotron bg-variant="light">
      <template v-slot:header><b-col align-self="end">What we do</b-col></template>

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
              style="max-width: 20rem; height: 270px"
              class="mb-2 border-0">
              <img slot="img" class="card-img img-fluid" src="../assets/Voting.png"/>
              <b-card-body>
              <b-card-text>
                  Make sure all women can vote in every state and local election
              </b-card-text>
              <b-button
              squared variant="outline-info"
              href="#">Become Aware</b-button>
            </b-card-body>
            </b-card>
        </b-col>
        <b-col>
          <b-card
            title="Education"
            tag="article"
             style="max-width: 20rem; height: 270px"
            class="mb-2 border-0">
            <b-card-body>
            <b-card-text>
              Ensure our elected officials and candidates understand
              the issues most important to Illinois women
            </b-card-text>

            <b-button
                squared variant="outline-info"
                href="#">Be Informed</b-button>
              </b-card-body>
          </b-card>
        </b-col>
        <b-col>
          <b-card
            title="Engagement"
            tag="article"
            style="max-width: 20rem; height: 270px"
            class="mb-2 border-0">
            <b-card-body>
            <b-card-text>
              Support women entering into state and local politic
            </b-card-text>
            <b-button
                    squared variant="outline-info"
                    href="#">Get Active</b-button>
            </b-card-body>
          </b-card>
        </b-col>
      </b-row>
    </b-jumbotron>
    <b-jumbotron bg-variant="transparent">
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

      <b-button variant="info" href="#">More history</b-button>
    </b-jumbotron>
  </b-container>
</template>
<style>
.card-card_title {
    font-size: 1.2em;
    font-shadow: 2px 2px #ccc;
}
.card-card_header {
    font-shadow: 2px 2px #00ff00;
}
.card-card_footer {
    color: #000;
    font-shadow: 2px 2px #FFAAFF;
}
</style>
