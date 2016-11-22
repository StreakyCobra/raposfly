import Vue from 'vue'
import App from './App'
import History from './components/History'
import Home from './components/Home'
import Shop from './components/Shop'
import Stats from './components/Stats'
import VueI18n from 'vue-i18n'
import VueRouter from 'vue-router'
import VueResource from 'vue-resource'
Vue.use(VueI18n)
Vue.use(VueRouter)
Vue.use(VueResource)

// config
var ROOT_URL = 'http://localhost:8080'
var ROOT_BACKEND_URL = 'http://localhost:8000'
var ROOT_API_URL = ROOT_BACKEND_URL + '/api'

// jquery
var $ = require('jquery')
window.jQuery = window.$ = $

// bootstrap
require('bootstrap')
import 'bootstrap/dist/css/bootstrap.css'
import 'chartist/dist/chartist.css'

// font-awesome
import 'font-awesome/css/font-awesome.css'

// vue-router
const routes = [
    { path: '/', component: Home },
    { path: '/shop', component: Shop },
    { path: '/history', component: History },
    { path: '/stats', component: Stats }
]

const router = new VueRouter({
    mode: 'history',
    routes: routes
})

// vue-resource
Vue.url.options.root = ROOT_API_URL

// vue-i18n
var language = require('./language')
language.setLang('en')

var busVue = new Vue()

// properties
Object.defineProperties(Vue.prototype, {
    $bus: {
        get: function () {
            return busVue
        }
    },
    $root_url: {
        get: function () {
            return ROOT_URL
        }
    },
    $backend_url: {
        get: function () {
            return ROOT_BACKEND_URL
        }
    },
    $language: {
        get: function () {
            return Vue.config.lang
        },
        set: function (lang) {
            language.setLang(lang)
        }
    }
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
