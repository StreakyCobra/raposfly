<template>
    <div class="container" style="padding-top: 50px;">
        <shop class="col-md-8" ref="shop" @add_item="add_item"/>
        <cart class="col-md-4" ref="cart" @purchase="purchase"/>
    </div>
</template>

<script>
 import Shop from './components/Shop'
 import Cart from './components/Cart'
 var $ = require('jquery')

 export default {
     name: 'app',
     components: {
         Shop,
         Cart
     },
     mounted: function () {
         $('#splash').delay(2000).fadeOut(1000)
     },
     methods: {
         add_item: function (item) {
             this.$refs.cart.add_item(item)
         },
         purchase: function (items, total) {
             this.$refs.history.add_order(items, total)
         }
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
