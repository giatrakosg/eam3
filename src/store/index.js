import Vue from 'vue'
import Vuex from 'vuex'
import axios from 'axios'

Vue.use(Vuex)

export default new Vuex.Store({
  state: {
    lang : 'gr' ,
    status: '',
    token: localStorage.getItem('token') || '',
    user: {} ,
    routePIDS : {},
    routes : []
  },
  mutations: {
    setLanguage(state , payload) {
      state.lang = payload.lang ;
    },
    setRoutes(state,payload){
      state.routePIDS = payload.routes
    },
    addRoute(state,payload) {
      state.routes.push(payload.route)
    },
    auth_request(state) {
      state.status = 'loading'
    },
    auth_success(state, payload) {
      state.status = 'success'
      state.token = payload.token
      state.user = payload.user
    },
    auth_registererror(state) {
      state.status = 'error'
    },
    logout(state) {
      state.status = ''
      state.token = ''
      state.user = {}
    },
  },

  actions: {
    login({ commit }, user) {
      const tok = user.email + ':' + user.password;
      const hash = btoa(tok);
      const Basic = 'Basic ' + hash;
      return new Promise((resolve, reject) => {
        commit('auth_request')
        axios({ url: 'http://localhost:5000/login', headers : {'Authorization' : Basic}, method: 'GET' })
          .then(resp => {
            const token = resp.data.token
            const user = resp.data.user
            //console.log(user)
            localStorage.setItem('token', token)
            // Add the following line:
            axios.defaults.headers.common['Authorization'] = token
            commit('auth_success', { token , user})
            resolve(resp)
          })
          .catch(err => {
            commit('auth_error')
            localStorage.removeItem('token')
            reject(err)
          })
      })
    },
    register({ commit }, user) {
      return new Promise((resolve, reject) => {
        commit('auth_request')
        axios({ url: 'http://localhost:5000/user', data: user, method: 'POST' })
          .then(resp => {
            console.log(resp.data)
            const token = resp.data.token
            const user = resp.data.user
            localStorage.setItem('token', token)
            // Add the following line:
            axios.defaults.headers.common['Authorization'] = token
            commit('auth_success', token, user)
            resolve(resp)
          })
          .catch(err => {
            commit('auth_error', err)
            localStorage.removeItem('token')
            reject(err)
          })
      })
    },
    logout({ commit }) {
      return new Promise((resolve, reject) => {
        commit('logout')
        localStorage.removeItem('token')
        delete axios.defaults.headers.common['Authorization']
        resolve()
      })
    } ,
    getRoutes({ commit , dispatch}){
      return new Promise((resolve, reject) => {
        commit('auth_request')
        axios({ url: 'http://localhost:5000/routes', method: 'GET' })
          .then(resp => {
            //console.log(resp.data)
            const routes = resp.data.routes
            commit('setRoutes',{routes})
            for (var i = 0; i < routes.length; i++) {
              dispatch('getRoute',routes[i])
            }
            resolve(resp)
          })
          .catch(err => {
          })
      })
    } ,
    getRoute({ commit } ,route_pid) {
      return new Promise((resolve, reject) => {
        commit('auth_request')
        axios({ url: 'http://localhost:5000/route/' + route_pid, method: 'GET' })
          .then(resp => {
            //console.log(resp.data)
            const route = resp.data.route
            console.log(route)
            commit('addRoute',{route})
            resolve(resp)
          })
          .catch(err => {
          })
    }) ;
  }
},
  modules: {
  }
})
