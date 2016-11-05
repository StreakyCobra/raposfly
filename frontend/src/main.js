import Vue from 'vue'
import App from './App'
import VueRouter from 'vue-router'
import VueResource from 'vue-resource'

// jquery
var $ = require('jquery')
window.jQuery = window.$ = $

// bootstrap
require('bootstrap')
import 'bootstrap/dist/css/bootstrap.css'

Vue.use(VueResource)
Vue.use(VueRouter)

const routes = [
  { path: '/', component: App }
]

const router = new VueRouter({routes})

new Vue({
  router
}).$mount('#app')
