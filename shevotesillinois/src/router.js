import Vue from 'vue';
import Router from 'vue-router';
import Main from './components/Main.vue';
import WhoWeAre from './components/whoweare.vue';
import Photo from './Photo.vue';

Vue.use(Router);

export default new Router({
  mode: 'history',
  base: process.env.BASE_URL,
  routes: [
    {
      path: '/',
      name: 'Main',
      component: Main,
    },
    {
      path: '/whoweare',
      name: 'WhoWeAre',
      component: WhoWeAre,
    },
    {
      path: '/photo/:id',
      name: 'photo',
      component: Photo,
    },
  ],
});
