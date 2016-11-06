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
     src: url('/static/fonts/Montserrat-Regular.otf');
     font-weight: normal;
 }

 @font-face {
     font-family: 'Montserrat';
     src: url('/static/fonts/Montserrat-Bold.otf');
     font-weight: bold;
 }

 #app {
     font-family: 'Montserrat', Helvetica, Arial, sans-serif;
 }
</style>
