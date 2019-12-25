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


import { LMap, LTileLayer, LMarker,LPolyline,LCircleMarker ,LIcon} from 'vue2-leaflet';


import 'leaflet/dist/leaflet.css'

////Map Marker  ERROR////////////////////////////////

import L from 'leaflet';
delete L.Icon.Default.prototype._getIconUrl;

L.Icon.Default.mergeOptions({
  iconRetinaUrl: require('leaflet/dist/images/marker-icon-2x.png'),
  iconUrl: require('leaflet/dist/images/marker-icon.png'),
  shadowUrl: require('leaflet/dist/images/marker-shadow.png')
});

/////////////////////////////////////////////////////////////





Vue.component('l-map', LMap);
Vue.component('l-tile-layer', LTileLayer);
Vue.component('l-marker', LMarker);
Vue.component('l-circle-marker', LCircleMarker);
Vue.component('l-polyline', LPolyline);
Vue.component('l-icon', LIcon);



Vue.use(BootstrapVue);
Vue.use(VueRouter);

Vue.config.productionTip = false;

new Vue({
  render: h => h(App),
  router,
  vuetify
}).$mount('#app');
