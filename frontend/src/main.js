import Vue from 'vue'
import App from './App'

// jquery
var $ = require('jquery')
window.jQuery = window.$ = $

// bootstrap
require('bootstrap')
import 'bootstrap/dist/css/bootstrap.css'

/* eslint-disable no-new */
new Vue({
  el: '#app',
  template: '<App/>',
  components: { App }
})
