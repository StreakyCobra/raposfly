<template>
    <div class="container">
        <h1 class="page-header">{{ $t('Stats') }}</h1>
        <h2>{{ $t('Total Sales') }}</h2>
        <p class="btn btn-primary">{{ total_sales }} CHF</p>
        <h2>{{ $t('Sales History') }}</h2>
        <div class="chart-cumulative-sales ct-minor-eleventh"></div>
        <h2>{{ $t('Counts') }}</h2>
        <div class="chart-counts ct-square"></div>
    </div>
</template>

<script>
 var Chartist = require('chartist')
 var moment = require('moment')
 moment.locale('fr-ch')

 export default {
     name: 'stats',
     data: function () {
         return {
             'total_sales': 0
         }
     },
     mounted: function () {
         this.$http.get('shop/stats/').then((response) => {
             this.plot(response.body)
         }, (response) => {
             this.$bus.$emit('error', 'Impossible to load stats')
         })
     },
     methods: {
         plot: function (stats) {
             this.total_sales = stats.total_sales

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
         }
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
