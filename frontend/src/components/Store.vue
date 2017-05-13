<template>
    <div>
        <div v-for="category in items">
            <h1 class="page-header">{{category.name}}</h1>
            <div class="row">
                <item v-for="item in category.items"
                      class="col-lg-4 col-md-4 col-sm-6 col-xs-12"
                      display_style=big
                      :item="item"
                      :key="item.id"
                      @click="itemClick(item, arguments[1])"/>
            </div>
        </div>
    </div>
</template>

<script>
 import Item from './Item'
 import { mapGetters } from 'vuex'
 var $ = require('jquery')

 export default {
     name: 'store',
     components: {
         Item
     },
     computed: mapGetters([
         'items'
     ]),
     methods: {
         itemClick: function (item, element) {
             $(element).stop().fadeTo(100, 0.3).fadeTo(100, 1)
             this.$emit('click', item)
         }
     },
     mounted: function () {
         this.$store.dispatch('getItems')
     }
 }
</script>
