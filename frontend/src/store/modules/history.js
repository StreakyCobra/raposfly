import shop from '../../api/shop'
import * as types from '../mutation-types'

const state = {
    history: []
}

const getters = {
    history: state => state.history
}

const mutations = {
    [types.RECEIVE_HISTORY]: function (state, { purchases }) {
        state.history = purchases
    },
    [types.DELETE_PURCHASE]: function (state, purchase) {
        var index = state.history.indexOf(purchase)
        if (index !== -1) {
            state.history.splice(index, 1)
        }
    }
}

const actions = {
    getHistory: function ({ commit }) {
        shop.getHistory((purchases) => {
            commit(types.RECEIVE_HISTORY, { purchases })
        }, () => {})
    },
    deletePurchase: function ({ commit }, purchase) {
        shop.deletePurchase(purchase, (purchase) => {
            commit(types.DELETE_PURCHASE, purchase)
        }, () => {})
    },
    printReceipt: function ({ commit }, purchase) {
        shop.printReceipt(purchase, (purchase) => {}, () => {})
    }
}

export default {
    state,
    getters,
    actions,
    mutations
}
