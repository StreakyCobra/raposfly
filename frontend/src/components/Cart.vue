<template>
    <div>
        <h1 class="page-header">{{ $t('Cart') }}</h1>
        <item
            del=true
            v-for="(item, index) in items"
            v-bind:item="item"
            @remove="remove_item(item, index)"/>
        <p class="bold">Total: <span class="amount">{{ total }} CHF</span></p>
        <button class="btn btn-success" @click="purchase">{{ $t('Purchase') }}</button>
        <button class="btn btn-warning" @click="reset">{{ $t('Discard') }}</button>
        <div id="alerts"></div>
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
             return items.map(item => parseFloat(item.price)).reduce(add, 0)
         },
         recompute_total: function () {
             this.total = this.get_items_total(this.items)
         },
         add_item: function (item) {
             this.items.push(item)
         },
         remove_item: function (item, index) {
             this.items.splice(index, 1)
         },
         purchase: function () {
             if (this.items.length > 0) {
                 this.$http.post('shop/purchase/', this.items).then((response) => {
                     this.$emit('purchase', this.items, this.total)
                 }, (response) => {
                     this.$emit('error', 'Impossible to purchase items')
                 })
             }
             $('#alerts').append('<div class="alert alert-info fade in">' + this.$t('Items purchased') + '</div>')
             $('.alert').delay(2000).slideUp(500)
             this.reset()
         },
         reset: function () {
             this.items = []
         }
     }
 }
</script>

<style scoped>
 .bold {
     font-weight: bold
 }

 .amount {
     color: #287379
 }

 #alerts {
     margin-top: 2em;
 }
</style>
