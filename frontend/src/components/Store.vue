<template>
    <div>
        <div class="col-md-6"
             v-for="category in items">
            <h1 class="page-header">{{category.name}}</h1>
            <item v-for="item in category.items"
                  display_style=big
                  :item="item"
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

