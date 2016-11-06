<template>
    <div>
        <h1 v-if="orders.length > 0">History:</h1>
        <template v-for="order in orders">
            <div class="well">
                <p class="time">{{ ('0'+order.datetime.getHours()).substr(-2) }}:{{('0'+order.datetime.getMinutes()).substr(-2) }}</p>
                <p class="bold">Total: <span class="amount">{{ order.total }} CHF</span></p>
                <item
                    v-for="item in order.items"
                    v-bind:item="item"
                />
            </div>
        </template>
    </div>
</template>

<script>
 import Item from './Item'

 var STORAGE_KEY = 'shop-history'
 var localStorage = window.localStorage
 var ordersStorage = {
     fetch () {
         var orders = JSON.parse(localStorage.getItem(STORAGE_KEY) || '[]')
         orders.forEach(function (order, index) {
             order.datetime = new Date(order.datetime)
         })
         return orders
     },
     save (orders) {
         localStorage.setItem(STORAGE_KEY, JSON.stringify(orders))
     }
 }

 export default {
     name: 'history',
     components: {
         Item
     },
     data () {
         return {
             orders: ordersStorage.fetch()
         }
     },
     watch: {
         orders: {
             handler: function (orders) {
                 ordersStorage.save(orders)
             },
             deep: true
         }
     },
     methods: {
         add_order: function (items, total) {
             this.orders.unshift({
                 items: items,
                 total: total,
                 datetime: new Date()
             })
         }
     }
 }
</script>

<style scoped>
 .well {
     /* background-color: red; */
     border-radius: 1em
 }

 .bold {
     font-weight: bold
 }

 .amount {
     color: #287379
 }

 .time {
     float: right
 }
</style>
