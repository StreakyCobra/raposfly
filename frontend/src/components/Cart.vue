<template>
    <div class="cart">
        <h1 class="page-header">{{ $t('Cart') }}</h1>
        <div class="controls">
            <p class="total">Total: <span class="amount">{{ total }} CHF</span></p>
            <div class="buttons btn-group">
                <button class="btn btn-lg btn-success" @click="purchaseCart">{{ $t('Purchase') }}</button>
                <button class="btn btn-lg btn-danger" @click="discardCart">{{ $t('Discard') }}</button>
            </div>
        </div>
        <hr />
        <template
            v-for="entry in cart">
            {{ entry.quantity }} × {{ entry.item.price }} = {{ entry.quantity * entry.item.price }} CHF
            <item display_style=small
                  :item="entry.item"
                  @clicked="removeFromCart(entry.item)"/>
        </template>
        <div id="alerts"></div>
    </div>
</template>

<script>
 import Item from './Item'
 import { mapActions, mapGetters } from 'vuex'

 export default {
     name: 'cart',
     components: {
         Item
     },
     computed: {
         total: function () {
             function add (a, b) {
                 return a + b
             }
             return this.cart.map(entry => parseFloat(entry.item.price) * entry.quantity).reduce(add, 0)
         },
         ...mapGetters([
             'cart'
         ])
     },
     methods: mapActions([
         'discardCart',
         'purchaseCart',
         'removeFromCart'
     ])
 }
</script>

<style scoped>
 .controls {
     margin-bottom: 1em;
 }
 .btn-group {
     width: 100%;
 }

 .btn {
     width: 50%;
 }

 .total {
     font-size: 1.5em;
     font-weight: bold;
 }

 .amount {
     float: right;
     text-decoration: underline;
 }

 #alerts {
     margin-top: 2em;
 }
</style>
