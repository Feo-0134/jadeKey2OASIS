import Vue from 'vue'
import App from './App.vue'
import vuetify from './plugins/vuetify';
import router from './router'
import Axios from 'axios'
import Vuex from 'vuex';
import AsyncComputed from 'vue-async-computed'

Vue.use(Vuex)

const store = new Vuex.Store({
  state: {
    role: 'engineer',
    username: '',
    password: '',
  },
  mutations: {
    setAccount (state, userAccount) {
      state.username = userAccount.username
      state.password = userAccount.password
    },
    switch2Reviewer (state) {
      state.role = 'reviewer'
    },
    switch2Engineer (state) {
      state.role = 'engineer'
    },
  }
})

Vue.use(AsyncComputed, {
  default: {context:'Loading...'}
});

Vue.config.productionTip = false

Vue.prototype.$http = Axios;

new Vue({
  store,
  vuetify,
  router,
  render: h => h(App)
}).$mount('#app')
