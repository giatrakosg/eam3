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
    routes : [] ,
    stopPIDS : {} ,
    stops : [] ,
    routes_status : '',
    stops_status : '' ,
    pending_routes : 0 ,
    pending_stops : 0 ,
    route : {} ,
    stop : {} ,
  },
  mutations: {
    setLanguage(state , payload) {
      state.lang = payload.lang ;
    },
    setRoutes(state,payload){
      state.routePIDS = payload.routes
    },
    routes_request(state){
      state.routes_status = 'loading'
    },
    routes_success(state) {
      state.routes_status = 'success'
    } ,
    routes_error(state) {
      state.routes_status = 'error'
    } ,
    increment_stops(state) {
      state.pending_stops++;
    },
    increment_routes(state) {
      state.pending_routes++;
    },
    decrease_stops(state) {
      state.pending_stops--;
      if (state.pending_stops == 0) {
        state.stops_status = 'success'
      }
    },
    decrease_routes(state) {
      state.pending_routes--;
      if (state.pending_routes == 0) {
        state.routes_status = 'success'
      }
    },
    stops_request(state){
      state.stops_status = 'loading'
    },
    stops_success(state) {
      state.stops_status = 'success'
    } ,
    stops_error(state) {
      state.stops_status = 'error'
    } ,
    addRoute(state,payload) {
      state.routes.push(payload.route)
    },
    addSelectedRoute(state,payload) {
      state.route = payload.route
    },
    setStops(state,payload){
      state.stopPIDS = payload.stops
    },
    addStop(state,payload) {
      state.stops.push(payload.stop) ;
    },
    addUser(state,payload) {
      state.user = payload.user ;
    },
    addSelectedStop(state,payload) {
      state.stop = payload.stop ;
    },
    auth_request(state) {
      state.status = 'loading'
    },
    auth_success(state, payload) {
      state.status = 'success'
      state.token = payload.token
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
    login({ commit , dispatch}, user) {
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
            axios.defaults.headers.common['x-access-token'] = token
            commit('auth_success', { token , user})
            resolve(resp)
            dispatch('getUser');
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
    update({ commit }, user) {
      return new Promise((resolve, reject) => {
        commit('auth_request')
        axios({ url: 'http://localhost:5000/user', data: user, method: 'PUT' })
          .then(resp => {
              resolve(resp)
          })
          .catch(err => {
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
        commit('routes_request')
        axios({ url: 'http://localhost:5000/routes', method: 'GET' })
          .then(resp => {
            //console.log(resp.data)
            const routes = resp.data.routes
            commit('setRoutes',{routes})
            for (var i = 0; i < routes.length; i++) {
              commit('increment_routes')
              dispatch('getRoute',routes[i])
            }
            resolve(resp)
          })
          .catch(err => {
            commit('routes_error')
          })
      })
    } ,
  getRoute({ commit } ,route_pid) {
      return new Promise((resolve, reject) => {
        axios({ url: 'http://localhost:5000/route/' + route_pid, method: 'GET' })
          .then(resp => {
            //console.log(resp.data)
            const route = resp.data.route
            console.log(route)
            commit('addRoute',{route})
            commit('decrease_routes')
            resolve(resp)
          })
          .catch(err => {
          })
    }) ;
  } ,
  getSelectedRoute({ commit } ,route_pid) {
      return new Promise((resolve, reject) => {
        axios({ url: 'http://localhost:5000/route/' + route_pid, method: 'GET' })
          .then(resp => {
            //console.log(resp.data)
            const route = resp.data.route
            console.log(route)
            commit('addSelectedRoute',{route})
            //commit('decrease_routes')
            resolve(resp)
          })
          .catch(err => {
          })
    }) ;
  } ,
  getStops({ commit , dispatch } ) {
    return new Promise((resolve, reject) => {
      commit('stops_request')
      axios({ url: 'http://localhost:5000/stations', method: 'GET' })
        .then(resp => {
          //console.log(resp.data)
          const stops = resp.data.stops
          commit('setStops',{stops})
          for (var i = 0; i < stops.length; i++) {
            commit('increment_stops')
            dispatch('getStop',stops[i])
          }
          commit('stops_success')
          resolve(resp)
        })
        .catch(err => {
          commit('stops_error')
        })
    })
  },
  getSelectedStop({ commit } ,stop_pid) {
      return new Promise((resolve, reject) => {
        axios({ url: 'http://localhost:5000/station/' + stop_pid, method: 'GET' })
          .then(resp => {
            //console.log(resp.data)
            const stop = resp.data.stop
            console.log(stop)
            commit('addSelectedStop',{stop})
            resolve(resp)
          })
          .catch(err => {
          })
    }) ;
  } ,
  getUser({ commit }) {
      return new Promise((resolve, reject) => {
        axios({ url: 'http://localhost:5000/user', method: 'GET' })
          .then(resp => {
            //console.log(resp.data)
            const user = resp.data.user
            console.log(stop)
            commit('addUser',{user})
            resolve(resp)
          })
          .catch(err => {
          })
    }) ;

  },
  getStop({ commit } ,stop_pid) {
      return new Promise((resolve, reject) => {
        axios({ url: 'http://localhost:5000/station/' + stop_pid, method: 'GET' })
          .then(resp => {
            //console.log(resp.data)
            const stop = resp.data.stop
            console.log(stop)
            commit('addStop',{stop})
            commit('decrease_stops');
            resolve(resp)
          })
          .catch(err => {
          })
    }) ;
  },
  userHasCard({commit}, user_id){
      return new Promise((resolve, reject) => {
          axios({url: 'http://localhost:5000/HasPersona/' + user_id, method: 'GET'})
            .then(resp=>{
                const card=resp.data.card
                console.log(card)
                commit('card',{card})
                resolve(resp)
            })
            .catch(err=> {
                
            })
    });
    },
  addPersonalCard({commit}, card){
      return new Promise((resolve, reject) => {
          axios({url: 'http://localhost:5000/BuyPersona', method: 'POST'})
            .then(resp=>{
                const card=resp.data.card
                console.log(card)
                commit('card',{card})
                resolve(resp)
            })
            .catch(err=> {
                
            })
    });
    },
RechargeCard({commit}, card){
      return new Promise((resolve, reject) => {
          axios({url: 'http://localhost:5000/tickets/recharge/', method: 'GET'})
            .then(resp=>{
                const card=resp.data.card
                console.log(card)
                commit('card',{card})
                resolve(resp)
            })
            .catch(err=> {
                
            })
    });
    },
getProducts({commit}, card_id){
      return new Promise((resolve, reject) => {
          axios({url: 'http://localhost:5000/products/get' + card_id, method: 'GET'})
            .then(resp=>{
                const card=resp.data.card
                console.log(card)
                commit('card',{card})
                resolve(resp)
            })
            .catch(err=> {
                
            })
    });
    },
},
  modules: {
  }
})
