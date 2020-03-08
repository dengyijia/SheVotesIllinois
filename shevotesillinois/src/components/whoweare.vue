<template>
  <div class="whoweare_gallery">
    <div class="gallery-panel"
         v-for="photo in photos"
         :key="photo.id">
     <router-link :to="`/photo/${photo.id}`">
       <img :src="thumbUrl(photo.filename)" >
     </router-link>
    </div>
  </div>
</template>

<script>
import photos from '@/photos.json';

const images = require.context('./../assets/profile_photos/thumbnails/', false, /\.jpg$/);

export default {
  name: 'Gallery',
  data() {
    return {
      photos,
    };
  },
  created() {
    // eslint-disable-next-line
    console.log(photos);
  },
  methods: {
    thumbUrl(filename) {
      // eslint-disable-next-line
      return images('./' + filename);
    },
  },
};
</script>

<style>
  .gallery {
    display: grid;
    grid-template-columns: repeat(5, minmax(20rem, 20rem));
    grid-gap: 1rem;
    max-width: 20rem;
    margin: 5rem auto;
    padding: 0 5rem;
  }
  .gallery-panel img {
    width: 30%;
    height: 22vw;
    object-fit: cover;
    border-radius: 0.75rem;
  }
</style>
