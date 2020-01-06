import Vue from 'vue'
import VueRouter from 'vue-router'
import Home from '../views/Home.vue'
import SearchRoutes from "../views/SearchRoutes";
import LoginPage from "../views/LoginPage";
import SignUpPage from "../views/SignUpPage";

import Contact from "../views/Contact";

import RoutePage from "../views/RoutePage";
import StopPage from "../views/StopPage";
import BusMapsPage from "../views/BusMapsPage";

import Tickets from "../views/Tickets"

Vue.use(VueRouter);

const routes = [
  {
    path: '/',
    name: 'home',
    component: Home,
    meta: {
      breadCrumb: 'Home'
    },

  },
  {
    path: '/SearchRoutes',
    name: 'search_routes',
    component: SearchRoutes,
    meta: {
      breadCrumb: 'Search Route'
    }
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
    meta: {
      breadCrumb: 'Login'
    },
  } ,
  {
    path: '/signup' ,
    name: 'signuppage' ,
    component : SignUpPage ,
    meta: {
      breadCrumb: 'SignUp'
    },
  } ,
  {
    path: '/contact' ,
    name: 'contact' ,
    component : Contact ,
    meta: {
      breadCrumb: 'Contact'
    },
  } ,
  {
    path: '/maps/bus' ,
    name: 'bussearchpage' ,
    component : BusMapsPage ,
    meta: {
      breadCrumb: 'Bus Maps'
    },
  },
  {
	path: '/tickets',
	name: 'tickets_page',
	component : Tickets,
	meta: {
		breadCrumb: 'Tickets'
	},
  },


];

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
});

export default router
