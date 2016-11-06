<template>
    <div>
        <h1 class="page-header">Store</h1>
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
     name: 'store',
     components: {
         Item
     },
     data () {
         return {
             items: []
         }
     },
     mounted: function () {
         this.$http.get('shop/items/').then((response) => {
             this.items = response.body
             console.log(response.body)
         }, null)
     },
     methods: {
         add_item: function (item) {
             this.$emit('add_item', item)
         }
     }
 }
</script>

