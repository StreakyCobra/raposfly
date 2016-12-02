import shop from '../../api/shop'
import * as types from '../mutation-types'

const state = {
    stats: []
}

const getters = {
    stats: state => state.stats
}

const mutations = {
    [types.RECEIVE_STATS]: function (state, { stats }) {
        state.stats = stats
    }
}

const actions = {
    getStats: function ({ commit }) {
        shop.getStats((stats) => {
            commit(types.RECEIVE_STATS, { stats })
        }, () => {})
    }
}

export default {
    state,
    getters,
    actions,
    mutations
}
