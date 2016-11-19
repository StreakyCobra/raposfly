<template>
    <div class="container">
        <h1 class="page-header">{{ $t('History') }}</h1>
        <template v-for="purchase in purchases">
            <div class="panel panel-info">
                <div class="panel-heading">{{ purchase.date }}</div>
                <div class="panel-body">
                    <item v-for="item in purchase.items"
                          v-bind:item="item"/>
                </div>
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
         }, (response) => {
             this.$emit('error', 'Impossible to load history')
         })
     }
 }
</script>

<style scoped>
 .purchase {
     background-repeat:repeat-x;
     border-radius:4px;
     box-shadow:rgba(255, 255, 255, 0.14902) 0 1px 0 inset, rgba(0, 0, 0, 0.0745098) 0 1px 5px;
     padding:1em;
     margin-bottom: 1em;
 }
</style>
