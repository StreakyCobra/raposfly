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
        },
        ADDTOCART: function (state, { id }) {
            console.log(id)
        }
    },
    getters: {
        items: state => state.items
    },
    actions: {
        getItems: function ({ commit }) {
            shop.get_items(
                (items) => {
                    commit('RECEIVED', { items })
                },
                () => {})
        },
        addToCart: function ({ commit }, item) {
            commit('ADDTOCART', { id: item.id })
        }
    }
})
