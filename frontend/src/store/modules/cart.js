import * as types from '../mutation-types'

const state = {
    added: []
}

const getters = {
    added: state => state.added
}

const mutations = {
    [types.ADD_TO_CART]: function (state, item) {
        state.added.push(item)
    }
}

const actions = {
    addToCart: function ({ commit }, item) {
        commit(types.ADD_TO_CART, item)
    }
}

export default {
    state,
    getters,
    actions,
    mutations
}
