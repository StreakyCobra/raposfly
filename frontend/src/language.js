import Vue from 'vue'
import en from './assets/i18n/en.json'
import fr from './assets/i18n/fr.json'

var locales = {
    en: en,
    fr: fr
}

Object.keys(locales).forEach(function (lang) {
    Vue.locale(lang, locales[lang])
})

export function setLang (lang) {
    Vue.locale(lang, locales[lang])
    Vue.config.lang = lang
}
