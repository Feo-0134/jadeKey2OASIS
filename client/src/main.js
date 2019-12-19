import Vue from 'vue'
import App from './App.vue'
import Axios from 'axios'
import router from './router'
import vuetify from './plugins/vuetify';
import AsyncComputed from 'vue-async-computed'

Vue.use(AsyncComputed, {
  default: 'Loading...'
});

Vue.config.productionTip = false
Vue.prototype.$http = Axios;

new Vue({
  vuetify,
  router,
  render: h => h(App)
}).$mount('#app')
