import Vue from 'vue'

// HACK: Change the lang first so it detect a change when setting english…
Vue.config.lang = 'WRONG?'

// isomorphic-fetch
var fetch = require('isomorphic-fetch')

export function setLang (lang) {
    Vue.locale(lang, function () {
        return fetch('/static/i18n/' + lang + '.json', {
            method: 'get',
            headers: {
                'Accept': 'application/json',
                'Content-Type': 'application/json'
            }
        }).then(function (res) {
            return res.json()
        }).then(function (json) {
            if (Object.keys(json).length === 0) {
                return Promise.reject(new Error('locale empty !!'))
            } else {
                return Promise.resolve(json)
            }
        })
    }, function () {
        Vue.config.lang = lang
        Vue.config.fallbackLang = 'en'
    })
}
