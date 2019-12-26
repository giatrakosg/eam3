import Vue from 'vue'
import VueRouter from 'vue-router'
import Home from '../views/Home.vue'
import SearchRoutes from "../views/SearchRoutes";
import LoginPage from "../views/LoginPage";
import SignUpPage from "../views/SignUpPage";
import RoutePage from "../views/RoutePage";
import StopPage from "../views/StopPage";


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
    component : RoutePage ,
    props : true ,
    meta: {
      title: 'Δρομολογιο'
    },
  } ,
  {
    path: '/stop/:id' ,
    name: 'StopPage' ,
    component : StopPage ,
    props : true ,
    meta: {
      title: 'Σταση'
    },
  } ,
  {
    path: '/login' ,
    name: 'loginpage' ,
    component : LoginPage ,
  } ,
  {
    path: '/signup' ,
    name: 'signuppage' ,
    component : SignUpPage ,
  } ,



];

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
});

export default router
