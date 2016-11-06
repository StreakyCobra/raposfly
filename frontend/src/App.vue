<template>
    <div class="container">
        <shop class="col-md-8" ref="shop" @add_item="add_item"/>
        <cart class="col-md-4" ref="cart" @purchase="purchase"/>
    </div>
</template>

<script>
 import Shop from './components/Shop'
 import Cart from './components/Cart'

 export default {
     name: 'app',
     components: {
         Shop,
         Cart
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
</style>
