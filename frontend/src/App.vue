<template>
  <div id="app">
  </div>
</template>

<script>
import Hello from './components/Hello'
var $ = require('jquery')

export default {
  name: 'app',
  components: {
    Hello
  },
  mounted: function () {
    $('#splash').delay(2000).fadeOut(1000)
  }
}
</script>

<style>
#app {
  font-family: 'Avenir', Helvetica, Arial, sans-serif;
}
</style>
