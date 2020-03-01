/* eslint-disable linebreak-style */
import Vue from 'vue';
import Router from 'vue-router';
import Main from './components/Main.vue';
import blog from './components/blogHome.vue';
import legrecap from './components/legrecap.vue';
import blogPosts from './assets/blog_posts.json';
import legPosts from './assets/legislation_recap.json';

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

const legRoutes = Object.keys(legPosts).map((section) => {
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
      path: '/legrecap',
      name: 'legrecap',
      component: legrecap,
    },
    {
      path: '/blog',
      name: 'Blog',
      component: blog,
    },
    ...blogRoutes,
    ...legRoutes,
  ],
});
