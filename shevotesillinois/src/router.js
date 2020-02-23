/* eslint-disable linebreak-style */
import Vue from 'vue';
import Router from 'vue-router';
import Main from './components/Main.vue';
import blog from './components/blogHome.vue';
import blogPosts from './assets/blog_posts.json';
import regInfo from './components/howToRegister.vue';
import plan from './components/planToVote.vue';

Vue.use(Router);

const blogRoutes = Object.keys(blogPosts).map((section) => {
  const children = blogPosts[section].map(child => ({
    path: child.id,
    name: child.id,
    component: () => import(`./assets/blog_posts/${section}/${child.id}.md`),
  }));
  return {
    path: `/${section}`,
    name: section,
    component: () => import('./components/blogPost.vue'),
    children,
  };
});

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
      path: '/blog',
      name: 'Blog',
      component: blog,
    },
    {
      path: '/registrationInfo',
      name: 'Voter Registration Info',
      component: regInfo,
    },
    {
      path: '/planToVote',
      name: 'Making Your Plan to Vote',
      component: plan,
    },
    ...blogRoutes,
  ],
});
