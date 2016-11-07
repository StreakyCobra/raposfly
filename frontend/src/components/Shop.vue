<template>
    <div>
        <store ref="store" class="col-md-8" @add_item="add_item" @error="error"></store>
        <cart ref="cart" class="col-md-4" @purchase="purchase" @error="error"></cart>
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
             $('#alerts').append('<div class="alert alert-info fade in">Items purchased.</div>')
             $('.alert').delay(2000).slideUp(500)
         },
         error: function (msg) {
             $('#modal').modal('show')
         }
     }
 }
</script>
