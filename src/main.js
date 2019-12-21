import '@babel/polyfill'
import 'mutationobserver-shim'
import Vue from 'vue'
import './plugins/bootstrap-vue'
import App from './App.vue'
import VueRouter from 'vue-router'
import router from './router'
import vuetify from './plugins/vuetify';
import BootstrapVue from 'bootstrap-vue'
import '@fortawesome/fontawesome-free/css/all.css'
import Breadcrumb from './components/Breadcrumb/Breadcrumb'

import { LMap, LTileLayer, LMarker , LPolyline } from 'vue2-leaflet';
import { Icon } from 'leaflet'

import 'leaflet/dist/leaflet.css'


/////////SECTION OF ERROR IN MAP////////////////////////////

/////////////////////////////////////////////////////////


Vue.component('l-map', LMap);
Vue.component('l-tile-layer', LTileLayer);
Vue.component('l-marker', LMarker);
Vue.component('l-polyline', LPolyline);



Vue.use(BootstrapVue);
Vue.use(VueRouter);

Vue.config.productionTip = false;

new Vue({
  render: h => h(App),
  router,
  vuetify
}).$mount('#app');
