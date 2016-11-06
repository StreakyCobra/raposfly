<template>
    <div>
        <div class="row">
            <store ref="store" class="col-md-8" @add_item="add_item"></store>
            <cart ref="cart" class="col-md-4" @purchase="purchase"></cart>
        </div>
        <div id="alerts"></div>
    </div>
</template>

<script>
 import Store from './Store'
 import Cart from './Cart'

 var $ = require('jquery')

 export default {
     name: 'shop',
     components: {
         Cart,
         Store
     },
     methods: {
         add_item: function (item) {
             this.$refs.cart.add_item(item)
         },
         purchase: function (items) {
             console.log(items)
             $('#alerts').append('<div class="alert alert-info fade in">Items purchased.</div>').delay(2000).slideUp(500)
         }
     }
 }
</script>
