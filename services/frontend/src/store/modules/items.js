import shop from '../../api/shop'
import * as types from '../mutation-types'

const state = {
    items: []
}

const getters = {
    items: state => state.items
}

const mutations = {
    [types.RECEIVE_ITEMS]: function (state, { items }) {
        state.items = items
    }
}

const actions = {
    getItems: function ({ commit }) {
        shop.getItems((items) => {
            commit(types.RECEIVE_ITEMS, { items })
        }, () => {})
    }
}

export default {
    state,
    getters,
    actions,
    mutations
}
