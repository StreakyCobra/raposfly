// ------------------------------------------------------------------------- //
// IMPORTS                                                                   //
// ------------------------------------------------------------------------- //

// Vue imports
import Vue from 'vue'
import VueResource from 'vue-resource'
import { sync } from 'vuex-router-sync'

// Components imports
import App from './App'

// Code imports
import store from './store'
import i18n from './language'
import router from './router'

// ------------------------------------------------------------------------- //
// EXTERNAL LIBRARIES                                                        //
// ------------------------------------------------------------------------- //

// Load bootstrap
import 'bootstrap/dist/css/bootstrap.css'

// Load chartist
import 'chartist/dist/chartist.css'

// Load font-awesome
import 'font-awesome/css/font-awesome.css'

require('bootstrap')

// ------------------------------------------------------------------------- //
// URLS                                                                      //
// ------------------------------------------------------------------------- //

// Check for prod/dev status
const production = process.env.NODE_ENV === 'production'

// DEV urls
var DEV_ROOT_URL = 'http://localhost:8080'
var DEV_ROOT_BACKEND_URL = 'http://localhost:8000'

// PROD urls
var PROD_ROOT_URL = 'http://raposfly.shop'
var PROD_ROOT_BACKEND_URL = 'http://backend.raposfly.shop'

// URLs
var ROOT_URL = production ? PROD_ROOT_URL : DEV_ROOT_URL
var ROOT_BACKEND_URL = production ? PROD_ROOT_BACKEND_URL : DEV_ROOT_BACKEND_URL
var ROOT_API_URL = ROOT_BACKEND_URL + '/api'

// ------------------------------------------------------------------------- //
// VUE CONFIGURATION                                                         //
// ------------------------------------------------------------------------- //

// router
sync(store, router)

router.afterEach((to, from) => {
    i18n.locale = to.params.lang
})

// vue-resource
Vue.use(VueResource)
Vue.url.options.root = ROOT_API_URL

// Create a bus for global events
var busVue = new Vue()

// vue properties
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
    }
})

// ------------------------------------------------------------------------- //
// EXPORT                                                                    //
// ------------------------------------------------------------------------- //

/* eslint-disable no-new */
new Vue({
    el: '#app',
    template: '<App/>',
    components: {
        App
    },
    store,
    i18n,
    router
})
