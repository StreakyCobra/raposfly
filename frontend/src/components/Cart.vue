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
            v-for="(item, index) in items"
            :item="item" />
        <div id="alerts"></div>
    </div>
</template>

<script>
 import Item from './Item'

 export default {
     name: 'cart',
     components: {
         Item
     },
     data: function () {
         return {
             items: [],
             total: 0
         }
     },
     mounted: function () {
         this.recompute_total()
     },
     watch: {
         items: {
             handler: function (items) {
                 this.recompute_total()
             },
             deep: true
         }
     },
     methods: {
         get_items_total: function (items) {
             function add (a, b) {
                 return a + b
             }
             return items.map(item => parseFloat(item.price) * item.quantity).reduce(add, 0)
         },
         recompute_total: function () {
             this.total = this.get_items_total(this.items)
         },
         add_item: function (item) {
             var index = this.items.indexOf(item)
             if (index !== -1) {
                 this.items[index].quantity += 1
             } else {
                 item.quantity = 1
                 this.items.push(item)
             }
         },
         remove_item: function (item, index) {
             if (this.items[index].quantity > 1) {
                 this.items[index].quantity -= 1
             } else {
                 this.items.splice(index, 1)
             }
         },
         reset: function () {
             this.items = []
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
