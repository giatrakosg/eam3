import '@babel/polyfill'
import 'mutationobserver-shim'
import Vue from 'vue'
import App from './App.vue'
import VueRouter from 'vue-router'
import router from './router'
import vuetify from './plugins/vuetify';
import VueI18n from 'vue-i18n';
import '@fortawesome/fontawesome-free/css/all.css'
import store from './store'

Vue.use(VueI18n)


import { ENGLISH_TRANSLATIONS } from './translations/en';
import { GREEK_TRANSLATIONS } from './translations/gr';

const TRANSLATIONS = {
  en: ENGLISH_TRANSLATIONS,
  gr: GREEK_TRANSLATIONS
}
const i18n = new VueI18n({
  locale: 'en',
  messages: TRANSLATIONS,
})

import { Icon } from 'leaflet'

import { LMap, LTileLayer, LMarker,LPolyline,LCircleMarker ,LIcon , LPopup} from 'vue2-leaflet';
import 'leaflet/dist/leaflet.css'
import L from 'leaflet';

delete L.Icon.Default.prototype._getIconUrl;

L.Icon.Default.mergeOptions({
  iconRetinaUrl: require('leaflet/dist/images/marker-icon-2x.png'),
  iconUrl: require('leaflet/dist/images/marker-icon.png'),
  shadowUrl: require('leaflet/dist/images/marker-shadow.png')
});

Vue.component('l-map', LMap);
Vue.component('l-tile-layer', LTileLayer);
Vue.component('l-marker', LMarker);
Vue.component('l-circle-marker', LCircleMarker);
Vue.component('l-polyline', LPolyline);
Vue.component('l-icon', LIcon);
Vue.component('l-popup', LPopup);

delete Icon.Default.prototype._getIconUrl;

Icon.Default.mergeOptions({
  iconRetinaUrl: require('leaflet/dist/images/marker-icon-2x.png'),
  iconUrl: require('leaflet/dist/images/marker-icon.png'),
  shadowUrl: require('leaflet/dist/images/marker-shadow.png')
});


Vue.use(VueRouter);

Vue.config.productionTip = false;

new Vue({
  render: h => h(App),
  router,
  store,
  vuetify ,
  i18n
}).$mount('#app');
