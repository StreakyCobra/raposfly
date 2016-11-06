<template>
    <div>
        <h1 class="page-header">Shop</h1>
        <item
            add=true
            v-for="(item, index) in items"
            v-bind:item="item"
            @add="add_item"/>
    </div>
</template>

<script>
 import Item from './Item'

 export default {
     name: 'shop',
     components: {
         Item
     },
     data () {
         return {
             items: [
                 {
                     name: 'Grillade',
                     price: 12
                 },
                 {
                     name: 'Raclette',
                     price: 10
                 },
                 {
                     name: 'Frites',
                     price: 6
                 },
                 {
                     name: 'Sandwich',
                     price: 3.5
                 }
             ]
         }
     },
     methods: {
         add_item: function (item) {
             this.$emit('add_item', item)
         }
     }
 }
</script>
