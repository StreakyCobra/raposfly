import Vue from 'vue'
import Vuex from 'vuex'

import cart from './modules/cart'
import history from './modules/history'
import items from './modules/items'

// Use vuex
Vue.use(Vuex)

export default new Vuex.Store({
    modules: {
        cart,
        history,
        items
    }
})
