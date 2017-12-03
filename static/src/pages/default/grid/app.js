import Vue from 'vue'
import ElementUI from 'element-ui'
import 'element-theme-default'
import App from './app.vue'

Vue.use(ElementUI)

new Vue({
  el: '#app',
  render: h => h(App)
})
