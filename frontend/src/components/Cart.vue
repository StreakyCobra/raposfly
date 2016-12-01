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
        <checkbox label="Print client receipt" :checked="receipt" @change="toggleReceipt"></checkbox>
        <hr />
        <template
            v-for="entry in cart">
            <item display_style=small
                  :item="entry.item"
                  :quantity="entry.quantity"
                  @clicked="removeFromCart(entry.item)"/>
        </template>
    </div>
</template>

<script>
 import Item from './Item'
 import Checkbox from './Checkbox'
 import { mapActions, mapGetters } from 'vuex'

 export default {
     name: 'cart',
     components: {
         Checkbox,
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
             'cart',
             'receipt'
         ])
     },
     methods: mapActions([
         'discardCart',
         'purchaseCart',
         'removeFromCart',
         'toggleReceipt'
     ])
 }
</script>

<style scoped>
 .controls {
     margin-bottom: 1em;
 }
 .controls .btn-group {
     width: 100%;
 }

 .controls .btn {
     width: 50%;
 }

 .total {
     font-size: 1.5em;
     font-weight: bold;
 }

 .amount {
     float: right;
 }
</style>
