import shop from '../../api/shop'
import * as types from '../mutation-types'

const state = {
    cart: []
}

const getters = {
    cart: function (state) {
        return state.cart
    }
}

const mutations = {
    [types.ADD_TO_CART]: function (state, item) {
        var index = state.cart.findIndex((elm) => elm.item === item)
        if (index !== -1) {
            state.cart[index].quantity++
        } else {
            state.cart.push({
                item: item,
                quantity: 1
            })
        }
    },
    [types.REMOVE_FROM_CART]: function (state, item) {
        var index = state.cart.findIndex((elm) => elm.item === item)
        console.log(item)
        if (index !== -1) {
            if (state.cart[index].quantity > 1) {
                state.cart[index].quantity--
            } else {
                state.cart.splice(index, 1)
            }
        }
    },
    [types.DISCARD_CART]: function (state) {
        state.cart = []
    },
    [types.PURCHASE_CART]: function (state) {
        shop.purchaseItems(
            state.cart,
            (items) => {
                state.cart = []
            },
            () => {})
    }
}

const actions = {
    addToCart: function ({ commit }, item) {
        commit(types.ADD_TO_CART, item)
    },
    removeFromCart: function ({ commit }, item) {
        commit(types.REMOVE_FROM_CART, item)
    },
    discardCart: function ({ commit }) {
        commit(types.DISCARD_CART)
    },
    purchaseCart: function ({ commit }) {
        commit(types.PURCHASE_CART)
    }
}

export default {
    state,
    getters,
    actions,
    mutations
}
