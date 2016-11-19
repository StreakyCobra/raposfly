<template>
    <div>
        <div class="col-md-6"
             v-for="(category, c_index) in items">
            <h1 class="page-header">{{category.name}}</h1>
            <item
                add=true
                v-for="(item, index) in category.items"
                v-bind:item="item"
                @add="add_item"/>
        </div>
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
         }, null)
     },
     methods: {
         add_item: function (item) {
             this.$emit('add_item', item)
         }
     }
 }
</script>

