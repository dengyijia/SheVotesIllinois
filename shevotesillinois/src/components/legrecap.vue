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

<template>
  <div>
    <span
      @mouseover="hover = true"
      @mouseleave="hover = false"
    >
      <b-button
                    squared variant="outline-secondary"
                    href="#">First test button<img src="./title_image.jpg" /></b-button>
    </span>
      <!--eslint-disable-next-line-->
    <span v-if="hover"><b-button variant="warning" href="#">Test</b-button></span>
  </div>
</template>

      <!--eslint-disable-next-line-->
      <button id="reproductivehealth" href=""> <img src="./title_image.jpg" /> </button>
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
    </b-jumbotron>
  </b-container>
  </div>
</template>
<style>
#reproductivehealth:hover {
  background-color: yellow;
}
#reproductivehealth {
  background-color: green;
}
</style>
<script>
export default {
  data() {
    return {
      hover: false,
    };
  },
};
</script>
