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
@font-face {
  font-family: 'Montserrat';
  src: url('/static/fonts/Montserrat-Black.otf');
  src: url('/static/fonts/Montserrat-Bold.otf');
  src: url('/static/fonts/Montserrat-ExtraBold.otf');
  src: url('/static/fonts/Montserrat-ExtraLight.otf');
  src: url('/static/fonts/Montserrat-Light.otf');
  src: url('/static/fonts/Montserrat-Medium.otf');
  src: url('/static/fonts/Montserrat-Regular.otf');
  src: url('/static/fonts/Montserrat-SemiBold.otf');
  src: url('/static/fonts/Montserrat-Thin.otf');
  src: url('/static/fonts/Montserrat-UltraLight.otf');
  src: local('Monserrat') format('truetype');
}

#app {
  font-family: 'Montserrat', Helvetica, Arial, sans-serif;
}
</style>
