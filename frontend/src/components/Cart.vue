<template>
    <div>
        <h1 class="page-header">Cart</h1>
        <item
            del=true
            v-for="(item, index) in items"
            v-bind:item="item"
            @remove="remove_item(item, index)"/>
        <p class="bold">Total: <span class="amount">{{ total }} CHF</span></p>
        <button class="btn btn-success" @click="purchase">Purchase</button>
        <button class="btn btn-warning" @click="reset">Discard</button>
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
         items_total: function (items) {
             function add (a, b) {
                 return a + b
             }
             return items.map(item => item.price).reduce(add, 0)
         },
         recompute_total: function () {
             this.total = this.items_total(this.items)
         },
         add_item: function (item) {
             this.items.push(item)
         },
         remove_item: function (item, index) {
             this.items.splice(index, 1)
         },
         purchase: function () {
             if (this.items.length > 0) {
                 this.$http.post('http://dubosson.tk:8080/purchase/', this.items)
                 this.$emit('purchase', this.items, this.total)
             }
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
</style>
