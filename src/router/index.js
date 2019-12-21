import Vue from 'vue'
import VueRouter from 'vue-router'
import Home from '../views/Home.vue'
import SearchRoutes from "../views/SearchRoutes";
import Route from "../components/StationInfo/Route"
Vue.use(VueRouter);

const routes = [
  {
    path: '/',
    name: 'home',
    component: Home
  },
  {
    path: '/SearchRoutes',
    name: 'search_routes',
    component: SearchRoutes
  } ,
  {
    path: '/bus/route/:id' ,
    name: 'routepage' ,
    component : Route ,
    props : true ,
    meta: {
      title: 'Σταση'
    },
  }

];

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
});

export default router
