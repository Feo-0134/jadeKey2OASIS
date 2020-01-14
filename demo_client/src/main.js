import Vue from 'vue'
import App from './App.vue'
import vuetify from './plugins/vuetify';
import router from './router'
import Axios from 'axios'
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
