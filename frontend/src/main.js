import Vue from 'vue'
import App from './App'
import History from './components/History'
import Home from './components/Home'
import Shop from './components/Shop'
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
    { path: '/', component: Home },
    { path: '/shop', component: Shop },
    { path: '/history', component: History }
]

const router = new VueRouter({
    mode: 'history',
    routes: routes
})

/* eslint-disable no-new */
new Vue({
    el: '#app',
    template: '<App/>',
    components: {
        App
    },
    router: router
})
