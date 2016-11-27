// ------------------------------------------------------------------------- //
// IMPORTS                                                                   //
// ------------------------------------------------------------------------- //

import Vue from 'vue'
import Vuex from 'vuex'
import * as actions from './actions'
import * as getters from './getters'
import cart from './modules/cart'
import products from './modules/products'

// ------------------------------------------------------------------------- //
// CONFIGURATION                                                             //
// ------------------------------------------------------------------------- //

// Use vuex
Vue.use(Vuex)

// Check for prod/dev status
const debug = process.env.NODE_ENV !== 'production'

// ------------------------------------------------------------------------- //
// EXPORT                                                                    //
// ------------------------------------------------------------------------- //

export default new Vuex.Store({
    actions,
    getters,
    modules: {
        cart,
        products
    },
    strict: debug
})
