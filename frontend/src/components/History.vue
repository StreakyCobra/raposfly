<template>
    <div class="container">
        <h1 class="page-header">History</h1>
        <template v-for="purchase in purchases">
            <div class="bg-info">
                <p>{{ purchase.date }}</p>
                <item v-for="item in purchase.items"
                      v-bind:item="item"/>
            </div>
        </template>
    </div>
</template>

<script>
 import Item from './Item'

 export default {
     name: 'history',
     components: {
         Item
     },
     data () {
         return {
             purchases: []
         }
     },
     mounted: function () {
         this.$http.get('shop/purchases/').then((response) => {
             this.purchases = response.body
         }, null)
     }
 }
</script>
