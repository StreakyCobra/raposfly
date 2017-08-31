<template>
    <div class="container">

        <h1 class="page-header">{{ $t('Cart') }}</h1>

        <div v-if="!pay_view">
            <div class="controls">
                <p class="total">Total: <span class="amount">{{ total.toFormat(2) }} CHF</span></p>
                <div class="buttons btn-group">
                    <button class="btn btn-lg btn-success" @click="to_pay">{{ $t('Pay') }}</button>
                    <button class="btn btn-lg btn-danger" @click="discard">{{ $t('Discard') }}</button>
                </div>
            </div>
            <hr />
            <template v-for="entry in cart">
                <item display_style=small
                      :item="entry.item"
                      :quantity="entry.quantity"
                      @click="itemClick(entry.item, arguments[1])"/>
            </template>
        </div>

        <div v-else>
            <div class="alert alert-info">
                <p class="total spacing-after">
                    {{ $t('To pay') }}: <span class="amount">&nbsp;{{ total.toFormat(2) }} CHF</span>
                </p>
                <checkbox :label="$t('Print client receipt')" :checked="receipt" @change="toggleReceipt"></checkbox>
                <template v-for="entry in cart">
                    <item display_style="list"
                          :quantity="entry.quantity"
                          :item="entry.item" />
                </template>
            </div>
            <div class="total alert alert-warning">
                <p class="spacing-after">
                    {{ $t('Cashed') }}: <span class="amount">{{ given.toFormat(2) }} CHF</span>
                </p>
                <numpad ref="numpad" v-model="given"></numpad>
            </div>
            <div class="btn-group">
                <div class="back-button btn btn-warning" @click="hidePayView"><i class="fa fa-chevron-circle-left"></i></div>
                <div :class="'purchase-button btn btn-' + (to_return.gt(0) || given.eq(0) || given.eq(total) ? 'success' : 'danger')" @click="purchase"><i class="fa fa-sign-in"></i>&nbsp;{{ to_return.toFormat(2) }} CHF</div>
            </div>
        </div>

    </div>
</template>

<script>
 import Item from './Item'
 import Checkbox from './Checkbox'
 import Numpad from './Numpad'
 import { mapActions, mapGetters } from 'vuex'
 import BigNumber from '../math.js'
 var $ = require('jquery')

 export default {
     name: 'cart',
     components: {
         Checkbox,
         Item,
         Numpad
     },
     data: function () {
         return {
             pay_view: false,
             given: new BigNumber(0)
         }
     },
     computed: {
         total: function () {
             return this.cart.map(entry => {
                 return new BigNumber(entry.item.price).times(entry.quantity)
             }).reduce((a, b) => a.plus(b), new BigNumber(0))
         },
         ...mapGetters([
             'cart',
             'receipt'
         ]),
         to_return: function () {
             return (this.given.gt(this.total) && this.given.minus(this.total)) || new BigNumber(0)
         }
     },
     methods: {
         add_item: function (item) {
             this.pay_view = false
             this.addToCart(item)
         },
         to_pay: function () {
             if (this.cart.length) { this.pay_view = true }
         },
         purchase: function () {
             this.given = new BigNumber(0)
             this.purchaseCart()
             this.pay_view = false
         },
         discard: function () {
             this.given = new BigNumber(0)
             this.discardCart()
         },
         itemClick: function (item, element) {
             $(element).stop().fadeTo(100, 0.3).fadeTo(100, 1)
             this.removeFromCart(item)
         },
         exitNumpad: function () {
             this.given = new BigNumber(0)
         },
         hidePayView: function () {
             this.pay_view = false
         },
         ...mapActions([
             'addToCart',
             'discardCart',
             'purchaseCart',
             'removeFromCart',
             'toggleReceipt'
         ])
     }
 }
</script>

<style scoped>
 .controls {
     margin-bottom: 1em;
 }
 .controls .btn-group {
     width: 100%;
 }

 .controls .btn {
     width: 50%;
 }

 .btn-group {
     width: 100%;
 }

 .back-button {
     font-size: 2em;
     text-align: center;
     width: 20%;
 }

 .purchase-button {
     font-size: 2em;
     width: 80%;
 }

 .total {
     font-size: 1.5em;
     font-weight: bold;
 }

 .amount {
     float: right;
 }

 .padValues {
     font-size: 1.2em;
     font-weight: bold;
 }

 .toReturn {
     font-size: 2em;
     text-align: center;
     cursor: pointer;
 }

 .spacing-after {
     margin-bottom: 1em;
 }
</style>
