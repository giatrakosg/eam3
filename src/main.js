import '@babel/polyfill'
import 'mutationobserver-shim'
import Vue from 'vue'
import './plugins/bootstrap-vue'
import App from './App.vue'
import VueRouter from 'vue-router'
import router from './router'
import vuetify from './plugins/vuetify';
import BootstrapVue from 'bootstrap-vue'

Vue.use(BootstrapVue)
Vue.use(VueRouter)

Vue.config.productionTip = false

new Vue({
  render: h => h(App),
  router,
  vuetify
}).$mount('#app')
