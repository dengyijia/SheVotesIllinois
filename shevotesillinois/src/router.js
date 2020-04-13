import Vue from 'vue';
import Router from 'vue-router';
import Main from './components/Main.vue';
import blog from './components/blogHome.vue';
import blogPosts from './assets/blog_posts.json';
import volunteer from './components/volunteer.vue';
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
      path: '/volunteer',
      name: 'Volunteer',
      component: volunteer,
    },
    {
      path: '/blog',
      name: 'Blog',
      component: blog,
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
