// ------------------------------------------------------------------------- //
// IMPORTS                                                                   //
// ------------------------------------------------------------------------- //

// Vue imports
import Vue from 'vue'
import VueI18n from 'vue-i18n'

// Languages imports
import en from './assets/i18n/en.json'
import fr from './assets/i18n/fr.json'

// ------------------------------------------------------------------------- //
// CONFIGURATION                                                             //
// ------------------------------------------------------------------------- //

// Use vue-i18n
Vue.use(VueI18n)

// Define languages
var locales = {
    en: en,
    fr: fr
}

// Load languages
Object.keys(locales).forEach(function (lang) {
    Vue.locale(lang, locales[lang])
})

// Select default language
var lang = 'en'
Vue.locale(lang, locales[lang])
Vue.config.lang = lang

// ------------------------------------------------------------------------- //
// EXPORT                                                                    //
// ------------------------------------------------------------------------- //

export default {
    set: function (lang) {
        Vue.locale(lang, locales[lang])
        Vue.config.lang = lang
    },
    get: function () {
        return Vue.config.lang
    }
}
