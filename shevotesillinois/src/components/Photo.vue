<template>
  <div class="lightbox">
    <img :src="photoUrl(photo.filename)">
    <div class="lightbox-info">
      <div class="lightbox-info-inner">
        <p v-if="photo.name">{{ photo.name}}</p>
        <p v-if="photo.position">{{ photo.position }}</p>
        <p v-if="photo.bio">{{ photo.bio }}</p>
        <p v-if="photo.intro">{{ photo.intro }}</p>
      </div>
    </div>
  </div>
</template>

<script>
import photos from '@/photos.json';

const images = require.context('./../assets/profile_photos/', false, /\.jpg$/);

export default {
  name: 'Photo',
  data() {
    return {
      photos,
    };
  },
  computed: {
    photo() {
      // eslint-disable-next-line
      return this.photos.find((photo) => {
        return photo.id === Number(this.$route.params.id);
      });
    },
  },
  methods: {
    photoUrl(filename) {
      // eslint-disable-next-line
      return images('./' + filename);
    },
  },
};
</script>

<style>
  .lightbox {
    position: fixed;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
    background-color: rgba(0, 0, 0, 0.8);
    display: grid;
    grid-template-columns: repeat(3, 1fr);
    grid-gap: 2rem;
  }
  .lightbox img {
    margin: auto;
    width: 100%;
    grid-column-start: 2;
  }
  .lightbox-info {
    margin: auto 2rem auto 0;
    height: 700px;
    width: 800px;
    overflow-x: scroll;
  }
  .lightbox-info-inner {
    background-color: #FFFFFF;
    display: inline-block;
    padding: 2rem;
  }
</style>
