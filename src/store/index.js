import Vue from 'vue'
import Vuex from 'vuex'

Vue.use(Vuex)

export default new Vuex.Store({
  state: {
    lang : 'gr'
  },
  mutations: {
    setLanguage(state , payload) {
      state.lang = payload.lang ;
    }
  },
  actions: {
  },
  modules: {
  }
})
