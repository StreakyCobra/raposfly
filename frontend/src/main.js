import Vue from 'vue'
import App from './App'
import VueRouter from 'vue-router'
import VueResource from 'vue-resource'
Vue.use(VueResource)
Vue.use(VueRouter)

// jquery
var $ = require('jquery')
window.jQuery = window.$ = $

// bootstrap
require('bootstrap')
import 'bootstrap/dist/css/bootstrap.css'

// font-awesome
import 'font-awesome/css/font-awesome.css'

const routes = [
  { path: '/', component: App }
]

const router = new VueRouter({routes})

new Vue({
  router
}).$mount('#app')
