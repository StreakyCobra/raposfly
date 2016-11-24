<template>
    <div>
        <div class="col-md-6"
             v-for="category in items">
            <h1 class="page-header">{{category.name}}</h1>
            <item v-for="item in category.items"
                  display_style=big
                  :item="item"
                  :show_quantity=false
                  @clicked="add_item(item)"/>
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
         this.$http.get('shop/store/').then((response) => {
             this.items = response.body
         }, (response) => {
             this.$bus.$emit('error', 'Impossible to load items')
         })
     },
     methods: {
         add_item: function (item) {
             this.$emit('add_item', item)
         }
     }
 }
</script>

