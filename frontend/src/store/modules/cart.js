import shop from '../../api/shop'
import * as types from '../mutation-types'

const state = {
    cart: [],
    receipt: false
}

const getters = {
    cart: function (state) {
        return state.cart
    },
    receipt: function (state) {
        return state.receipt
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
        state.receipt = false
    },
    [types.PURCHASE_CART]: function (state) {
        shop.purchaseItems(
            state.cart,
            (items) => {
                state.cart = []
            },
            () => {})
        state.receipt = false
    },
    [types.TOGGLE_RECEIPT]: function (state) {
        state.receipt = !state.receipt
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
    },
    toggleReceipt: function ({ commit }) {
        commit(types.TOGGLE_RECEIPT)
    }
}

export default {
    state,
    getters,
    actions,
    mutations
}
