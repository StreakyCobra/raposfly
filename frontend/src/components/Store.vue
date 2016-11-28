<template>
    <div>
        <div class="col-md-6"
             v-for="category in items">
            <h1 class="page-header">{{category.name}}</h1>
            <item v-for="item in category.items"
                  display_style=big
                  :item="item"
                  :show_quantity=false />
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
     computed: {
         items: function () {
             return this.$store.getters.getItems
         }
     },
     mounted: function () {
         this.$store.dispatch('getItems')
     }
 }
</script>

