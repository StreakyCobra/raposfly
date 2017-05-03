<template>
    <div class="row">
        <div class="col-lg-4 col-md-4 col-sm-6 col-xs-12"
             v-for="category in items">
            <h1 class="page-header">{{category.name}}</h1>
            <item v-for="item in category.items"
                  display_style=big
                  :item="item"
                  :key="item.id"
                  @clicked="addToCart(item)"/>
        </div>
    </div>
</template>

<script>
 import Item from './Item'
 import { mapActions, mapGetters } from 'vuex'

 export default {
     name: 'store',
     components: {
         Item
     },
     computed: mapGetters([
         'items'
     ]),
     methods: mapActions([
         'addToCart'
     ]),
     mounted: function () {
         this.$store.dispatch('getItems')
     }
 }
</script>

