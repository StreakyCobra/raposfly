<template>
    <div class="container">
        <h1 class="page-header">{{ $t('History') }}<span class="pull-right btn btn-info" @click="getHistory">{{ $t('Refresh') }}</span></h1>
        <template v-for="purchase in history">
            <div class="panel panel-info">
                <div class="panel-heading clearfix">
                    <div class="pull-right">
                        <a class="btn btn-primary btn-xs" @click="printReceipt(purchase)">{{ $t('Receipt') }}</a>
                        <a class="btn btn-danger btn-xs" @click="deletePurchase(purchase)">{{ $t('Delete') }}</a>
                    </div>
                    {{ format_date(purchase.date) }}
                </div>
                <div class="panel-body">
                    <template v-for="order in purchase.orders">
                        <item
                            display_style="list"
                            :quantity="order.quantity"
                            :item="order.item"/>
                    </template>
                </div>
                <div class="panel-footer">
                    Total: <span class="pull-right">{{ compute_total(purchase).toFormat(2) }} CHF</span>
                </div>
            </div>
        </template>
        <a id="more" class="btn btn-info" @click='getMoreHistory'>Load more</a>
    </div>
</template>

<script>
 import Item from './Item'
 import BigNumber from '../math.js'
 import { mapActions, mapGetters } from 'vuex'

 var moment = require('moment')
 moment.locale('fr-ch')

 export default {
     name: 'history',
     components: {
         Item
     },
     computed: mapGetters([
         'history'
     ]),
     mounted: function () {
         this.$store.dispatch('getHistory')
     },
     methods: {
         compute_total: function (purchase) {
             return purchase.orders.map(entry => {
                 return new BigNumber(entry.item.price).times(entry.quantity)
             }).reduce((a, b) => a.plus(b), new BigNumber(0))
         },
         format_date: function (date) {
             var result = moment(date).format('LLLL')
             return result.charAt(0).toUpperCase() + result.slice(1)
         },
         ...mapActions([
             'getHistory',
             'getMoreHistory',
             'deletePurchase',
             'printReceipt'
         ])
     }
 }
</script>

<style scoped>
 .panel-heading {
     line-height: 22px;
 }

 .panel-footer {
     font-weight: bold;
 }
</style>
