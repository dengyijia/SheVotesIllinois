<template>
  <div class="home">
    <navbar></navbar>
    <br>
    <img alt="Vue logo" src="../assets/logo.png">
    <h1 class="center">Volunteer Opportunities</h1>
    <div class="sections">
      <!--eslint-disable-next-line-->
      <p>Have you been looking to step up your involvement in the political process and advocate for women’s rights and equality in our state? She Votes Illinois is looking for bold and compassionate volunteers to help advance our mission.
      </p>
      <!--eslint-disable-next-line-->
      <p>If you have a skill not listed below and want to be a part of our volunteer team or are interested in becoming part of our <a rel="noreferrer noopener" href="#" target="_blank">Board of Directors or Advisory Council</a>, we’d love to talk to you!
      </p>
      <!--eslint-disable-next-line-->
      <p>Contact us at <a href="mailto:info@shevotesil.org">info@shevotesil.org</a> for more details and to be a part of our movement! All are welcome!!!
      </p>
    </div>
    <br>
    <h2 class="center">Open Positions</h2>
    <br>
    <div class="sections">
      <div v-for="(section, index) in Object.keys(entries)" :key="index" class="group">
        <div class="section" v-for="entry in entries[section]" :key="entry.id">
          <div class="entry">
            <h3>
              {{entry.title}}
              <span class="subtitle">{{entry.date}}</span>
            </h3>
            <p>{{entry.description}}</p>
          </div>
        </div>
      </div>
    </div>

  </div>
</template>

<script>
import POSITIONS from '@/assets/open_positions.json';

export default {
  name: 'home',
  computed: {
    entries() {
      return POSITIONS;
    },
  },
};
</script>

<style lang="scss" scoped>
  .center {
    text-align: center;
  }

  .headline {
    text-transform: uppercase;
    margin: 4rem auto;
    font-size: 4rem;
  }

  img {
    display: block;
    margin: 0 auto;
    width: 150px;
  }

  h2 {
    color: #35495e;
    text-transform: capitalize; // margin-bottom: 2rem;
  }

  h3 {
    color: #35495e;
    margin-bottom: 0;
    .subtitle {
      color: grey;
      font-size: .98rem;
      float: right;
      font-weight: normal;
    }
  }

  p {
    margin-top: .4rem;
  }

  .sections {
    max-width: 40vw;
    margin: 0 auto; // margin-top: 4rem;
  }

  .section {
    margin-bottom: 3rem;
  }

  .group {
    margin-bottom: 4rem;
  }

</style>
