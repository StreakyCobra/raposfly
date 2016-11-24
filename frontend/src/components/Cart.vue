<template>
    <div>
        <h1 class="page-header">{{ $t('Cart') }}</h1>
        <div class="buttons btn-group">
            <button class="btn btn-lg btn-success" @click="purchase">{{ $t('Purchase') }}</button>
            <button class="btn btn-lg btn-danger" @click="reset">{{ $t('Discard') }}</button>
        </div>
        <p class="total">Total: <span class="amount">{{ total }} CHF</span></p>
        <div id="alerts"></div>
        <item
            display_style=small
            v-for="(item, index) in items"
            :item="item"
            @clicked="remove_item(item, index)"/>
    </div>
</template>

<script>
 import Item from './Item'

 var $ = require('jquery')

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
         purchase: function () {
             if (this.items.length > 0) {
                 this.$http.post('shop/do-purchase/', this.items).then((response) => {
                     this.$emit('purchase', this.items, this.total)
                     $('#alerts').append('<div class="alert alert-info fade in">' + this.$t('Items purchased') + '</div>')
                     $('.alert').delay(2000).slideUp(500)
                     this.reset()
                 }, (response) => {
                     this.$bus.$emit('error', 'Impossible to purchase items')
                 })
             }
         },
         reset: function () {
             this.items = []
         }
     }
 }
</script>

<style scoped>
 .btn-group {
     width: 100%;
     margin-bottom: 1em;
 }

 .btn {
     width: 50%;
 }

 .total {
     font-weight: bold;
     font-size: 1.5em;
 }

 .amount {
     float: right;
     color: #287379;
 }

 #alerts {
     margin-top: 2em;
 }
</style>
