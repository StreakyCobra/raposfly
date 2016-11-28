<template>
    <div class="cart">
        <h1 class="page-header">{{ $t('Cart') }}</h1>
        <div class="controls">
            <p class="total">Total: <span class="amount">{{ total }} CHF</span></p>
            <div class="buttons btn-group">
                <button class="btn btn-lg btn-success">{{ $t('Purchase') }}</button>
                <button class="btn btn-lg btn-danger">{{ $t('Discard') }}</button>
            </div>
        </div>
        <hr />
        <item
            display_style=small
            v-for="(item, index) in added"
            :item="item" />
        <div id="alerts"></div>
    </div>
</template>

<script>
 import Item from './Item'
 import { mapGetters } from 'vuex'

 export default {
     name: 'cart',
     components: {
         Item
     },
     computed: mapGetters([
         'added'
     ]),
     methods: {
         get_items_total: function (items) {
             function add (a, b) {
                 return a + b
             }
             return items.map(item => parseFloat(item.price) * item.quantity).reduce(add, 0)
         },
         recompute_total: function () {
             this.total = this.get_items_total(this.items)
         }
     }
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
