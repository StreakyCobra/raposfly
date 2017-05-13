<template>
    <div class="row innerscroll">
        <store ref="store"
               class="col-lg-9 col-md-8 col-sm-8 col-xs-12 scrollable"
               @add_item="add_item">
        </store>
        <cart ref="cart"
              class="col-lg-3 col-md-4 col-sm-4 col-xs-12 scrollable">
        </cart>
    </div>
</template>

<script>
 import Store from './Store'
 import Cart from './Cart'

 export default {
     name: 'shop',
     components: {
         Cart,
         Store
     },
     methods: {
         add_item: function (item) {
             this.$refs.cart.add_item(item)
         }
     }
 }
</script>

<style scoped>
 .scrollable {
     height: 100%;
     overflow: auto;
 }
</style>
