
/* eslint-disable linebreak-style */
import 'bootstrap/dist/css/bootstrap.css';
import BootstrapVue from 'bootstrap-vue';
import Vue from 'vue';
import App from './App.vue';
import router from './router';
import Home from './components/Home.vue';
import navbar from './components/navbar.vue';
import blogHome from './components/blogHome.vue';
import blogPost from './components/blogPost.vue';
import regInfo from './components/howToRegister.vue';
import plan from './components/planToVote.vue';

Vue.config.productionTip = false;

Vue.use(BootstrapVue);
Vue.component('home', Home);
Vue.component('navbar', navbar);
Vue.component('blogHome', blogHome);
Vue.component('blogPost', blogPost);
Vue.component('regInfo', regInfo);
Vue.component('plan', plan);

new Vue({
  router,
  render: h => h(App),
}).$mount('#app');
