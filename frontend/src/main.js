import Vue from 'vue'
import App from './App'
import History from './components/History'
import Home from './components/Home'
import Shop from './components/Shop'
import VueI18n from 'vue-i18n'
import VueRouter from 'vue-router'
import VueResource from 'vue-resource'
Vue.use(VueI18n)
Vue.use(VueRouter)
Vue.use(VueResource)

// config
var ROOT_URL = 'http://localhost'
var ROOT_BACKEND_URL = 'http://localhost:8000/api'

// jquery
var $ = require('jquery')
window.jQuery = window.$ = $

// bootstrap
require('bootstrap')
import 'bootstrap/dist/css/bootstrap.css'

// font-awesome
import 'font-awesome/css/font-awesome.css'

// vue-router
const routes = [
    { path: '/', component: Home },
    { path: '/shop', component: Shop },
    { path: '/history', component: History }
]

const router = new VueRouter({
    mode: 'history',
    routes: routes
})

// vue-resource
Vue.url.options.root = ROOT_BACKEND_URL

// vue-i18n
var language = require('./language')
language.setLang('en')

// properties
Object.defineProperties(Vue.prototype, {
    $root_url: {
        get: function () {
            return ROOT_URL
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
