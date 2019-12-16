import Vue from 'vue'
import VueRouter from 'vue-router'
import Home from '../views/Home.vue'
import Route from '../components/StationInfo/Route.vue'
Vue.use(VueRouter)

const routes = [
  {
    path: '/',
    name: 'home',
    component: Home
  },
  {
    path: '/bus/route/:id' ,
    name: 'routepage' ,
    component : Route ,
    props : true
  }
];

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
});

export default router
