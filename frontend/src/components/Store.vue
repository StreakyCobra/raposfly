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
 import { mapGetters } from 'vuex'

 export default {
     name: 'store',
     components: {
         Item
     },
     computed: mapGetters([
         'items'
     ]),
     mounted: function () {
         this.$store.dispatch('getItems')
     }
 }
</script>

