import Vue from 'vue'
import App from './App'
import History from './History'
import Shop from './Shop'
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
    { path: '/', component: App },
    { path: '/shop', component: Shop },
    { path: '/history', component: History }
]

const router = new VueRouter({
    mode: 'history',
    routes: routes
})

new Vue({
    router
}).$mount('#app')
