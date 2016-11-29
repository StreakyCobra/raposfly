<template>
    <div class="container">
        <h1 class="page-header">{{ $t('History') }}</h1>
        <template v-for="purchase in purchases">
            <div class="panel panel-info">
                <div class="panel-heading clearfix">
                    <div class="btn-group pull-right">
                        <a class="btn btn-danger btn-xs" @click="remove(purchase)">{{ $t('Delete') }}</a>
                    </div>
                    {{ format_date(purchase.date) }}
                </div>
                <div class="panel-body">
                    <template v-for="order in purchase.orders">
                        {{ order.quantity }} ×
                        <item
                            display_style="list"
                            :item="order.item"/>
                    </template>
                </div>
                <div class="panel-footer">
                    Total
                </div>
            </div>
        </template>
    </div>
</template>

<script>
 import Item from './Item'

 var moment = require('moment')
 moment.locale('fr-ch')

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
         this.load()
     },
     methods: {
         load: function () {
             this.$http.get('shop/history/').then((response) => {
                 this.purchases = response.body
             }, (response) => {
                 this.$bus.$emit('error', 'Impossible to load history')
             })
         },
         remove: function (purchase) {
             this.$http.delete('shop/purchases/' + purchase.id + '/').then((response) => {
                 this.load()
             }, (response) => {
                 this.$bus.$emit('error', 'Impossible to delete purchase')
             })
         },
         format_date: function (date) {
             var result = moment(date).format('LLLL')
             return result.charAt(0).toUpperCase() + result.slice(1)
         }
     }
 }
</script>

<style scoped>
 .panel-heading {
     line-height: 22px;
 }
</style>
