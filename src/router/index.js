import Vue from 'vue'
import VueRouter from 'vue-router'
import Home from '../views/Home.vue'
import SearchRoutes from "../views/SearchRoutes";
import LoginPage from "../views/LoginPage";
import SignUpPage from "../views/SignUpPage";
import Route from "../components/StationInfo/Route"
import Contact from "../views/Contact";


Vue.use(VueRouter);

const routes = [
  {
    path: '/',
    name: 'home',
    component: Home,
    meta:{
      breadCrumb:'Home'
    }
  },
  {
    path: '/SearchRoutes',
    name: 'search_routes',
    component: SearchRoutes,
    meta:{
      breadCrumb:'Search Results'
    }
  } ,
  {
    path: '/bus/route/:id' ,
    name: 'routepage' ,
    component : Route ,
    props : true ,
    meta: {
      breadCrumb:'Routes',
      title: 'Σταση'
    },
  } ,
  {
    path: '/login' ,
    name: 'loginpage' ,
    component : LoginPage ,
    meta:{
      breadCrumb:'Login'
    }
  } ,
  {
    path: '/signup' ,
    name: 'signuppage' ,
    component : SignUpPage ,
    meta:{
      breadCrumb:'Sign Up'
    }
  } ,
  {
    path: '/contact' ,
    name: 'contact' ,
    component : Contact ,
    meta:{
      breadCrumb:'Contact'
    }
  }



];

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
});

export default router
