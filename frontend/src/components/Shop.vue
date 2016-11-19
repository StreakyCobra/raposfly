<template>
    <div>
        <store ref="store" class="col-md-8" @add_item="add_item" @error="error"></store>
        <cart ref="cart" class="col-md-4" @error="error"></cart>
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
         },
         error: function (msg) {
             this.$emit('error', 'Impossible to purchase items')
         }
     }
 }
</script>
