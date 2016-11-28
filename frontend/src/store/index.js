import Vue from 'vue'
import Vuex from 'vuex'

import shop from '../api/shop'

// Use vuex
Vue.use(Vuex)

export default new Vuex.Store({
    state: {
        items: []
    },
    mutations: {
        RECEIVED: function (state, { items }) {
            state.items = items.items
        }
    },
    getters: {
        getItems: state => state.items
    },
    actions: {
        getItems: function ({ commit }) {
            shop.get_items(
                (items) => {
                    commit('RECEIVED', { items })
                },
                () => {})
        }
    }
})
