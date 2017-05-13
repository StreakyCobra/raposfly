<template>
    <div class="container">
        <h1 class="page-header">{{ $t('Stats') }}<span class="pull-right btn btn-info" @click="getStats">{{ $t('Refresh') }}</span></h1>
        <h2>{{ $t('Total Sales') }}</h2>
        <h3 class="alert alert-info">{{ total_sales.toFormat(2) }} CHF</h3>
        <h2>{{ $t('Sales History') }}</h2>
        <div class="chart-cumulative-sales ct-minor-eleventh"></div>
        <h2>{{ $t('Counts') }}</h2>
        <div class="chart-counts ct-square"></div>
    </div>
</template>

<script>
 import { mapActions, mapGetters } from 'vuex'
 import Chartist from 'chartist'
 import BigNumber from '../math.js'
 var moment = require('moment')
 moment.locale('fr-ch')

 export default {
     name: 'stats',
     data: function () {
         return {
             total_sales: new BigNumber(0)
         }
     },
     computed: mapGetters([
         'stats'
     ]),
     mounted: function () {
         this.$store.dispatch('getStats')
     },
     watch: {
         stats: function (stats) {
             this.plot(stats)
             this.total_sales = new BigNumber(stats.total_sales)
         }
     },
     methods: {
         plot: function (stats) {
             Chartist.Line('.chart-cumulative-sales', {
                 series: [
                     stats.cumulative_sales
                 ]
             }, {
                 axisX: {
                     type: Chartist.FixedScaleAxis,
                     divisor: 5,
                     labelInterpolationFnc: function (value) {
                         return moment.unix(value).format('D/M LT')
                     }
                 }
             })

             Chartist.Bar('.chart-counts', {
                 labels: stats.counts.labels,
                 series: [
                     stats.counts.series
                 ]
             }, {
                 seriesBarDistance: 10,
                 reverseData: true,
                 horizontalBars: true,
                 axisY: {
                     offset: 150
                 },
                 axisX: {
                     onlyInteger: true
                 }
             })
         },
         ...mapActions([
             'getStats'
         ])
     }
 }
</script>

<style>
 .chart-cumulative-sales .ct-label {
     font-size: 2rem !important;
 }

 .chart-counts .ct-label {
     font-size: 2rem !important;
 }

 .chart-counts .ct-bar {
     stroke-width: 20px;
 }
</style>
