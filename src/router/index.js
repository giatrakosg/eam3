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
import ReducedTickets from "../views/ReducedTickets"
import ViewProfile from "../views/ViewProfile"
import EditProfile from "../views/EditProfile"
import BuyTicket from "../views/BuyTicket"

import RechargePage from "../views/RechargePage.vue"
import CheckoutPage from "../views/CheckoutPage.vue"
import About from "../views/About";
import SuccessBuyPage from "../views/SuccessBuyPage";


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
  {
	path: '/tickets/reduced_info',
	name: 'reduced_tickets_info_page',
	component : ReducedTickets,
	meta: {
		breadCrumb: 'Tickets/Reduced'
	},
  },
  {
	path: '/profile/view',
	name: 'view_profile',
	component : ViewProfile,
	meta: {
		breadCrumb: 'Profile/View'
	},
  },
  {
	path: '/profile/edit',
	name: 'edit_profile',
	component : EditProfile,
	meta: {
		breadCrumb: 'Profile/Edit'
	},
  },
  {
	path: '/tickets/buy',
	name: 'buy_ticket',
	component : BuyTicket,
	meta: {
		breadCrumb: 'Tickets/Buy'
	},
  },
  {
	path: '/tickets/recharge',
	name: 'recharge_page',
	component : RechargePage,
	meta: {
		breadCrumb: 'Tickets/Recharge'
	}
  },
   {
       path: '/about',
       name: 'about',
       component : About,
       meta: {
           breadCrumb: 'About'
       },
   },
  {
	path: '/tickets/checkout',
	name: 'checkout_page',
	component : CheckoutPage,
	meta: {
		breadCrumb: 'Tickets/Checkout'
	},
  },
  {
	path: '/buysuccess',
	name: 'buysuccess',
	component : SuccessBuyPage,
	meta: {
		breadCrumb: 'Success'
	},
  },


];

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
});

export default router
