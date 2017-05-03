<template>
    <div class="cart">
        <h1 class="page-header">{{ $t('Cart') }}</h1>
        <div v-if="cart.length > 0 || last_total.eq(0)">
            <div class="controls">
                <p class="total">Total: <span class="amount">{{ total.toFormat(2) }} CHF</span></p>
                <div class="buttons btn-group">
                    <button class="btn btn-lg btn-success" @click="purchase">{{ $t('Purchase') }}</button>
                    <button class="btn btn-lg btn-danger" @click="discard">{{ $t('Discard') }}</button>
                </div>
            </div>
            <checkbox :label="$t('Print client receipt')" :checked="receipt" @change="toggleReceipt"></checkbox>
            <hr />
            <template
                v-for="entry in cart">
                <item display_style=small
                      :item="entry.item"
                      :quantity="entry.quantity"
                      @clicked="removeFromCart(entry.item)"/>
            </template>
        </div>
        <div v-else-if="last_total.gt(0)">
            <div class="total alert alert-warning">
                Paid: <span class="amount">{{ given.toFormat(2) }} CHF</span>
                <br />
                To pay: <span class="amount underline"><i class="fa fa-minus" style="font-size: 0.8em;"></i>&nbsp;{{ last_total.toFormat(2) }} CHF</span>
            </div>
            <div :class="'toReturn alert alert-' + (to_return.gt(0) || given.eq(0) || given.eq(last_total) ? 'success' : 'danger')" @click="exitNumpad"><i class="fa fa-sign-in"></i>&nbsp;{{ to_return.toFormat(2) }} CHF</div>
            <hr />
            <numpad ref="numpad" v-model="given"></numpad>
            <hr />
        </div>
    </div>
</template>

<script>
 import Item from './Item'
 import Checkbox from './Checkbox'
 import Numpad from './Numpad'
 import { mapActions, mapGetters } from 'vuex'
 import BigNumber from '../math.js'

 export default {
     name: 'cart',
     components: {
         Checkbox,
         Item,
         Numpad
     },
     data: function () {
         return {
             last_total: new BigNumber(0),
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
             return this.given.gt(this.last_total) && this.given.minus(this.last_total) || new BigNumber(0)
         }
     },
     methods: {
         purchase: function () {
             this.last_total = this.total
             this.given = new BigNumber(0)
             this.purchaseCart()
         },
         discard: function () {
             this.last_total = new BigNumber(0)
             this.given = new BigNumber(0)
             this.discardCart()
         },
         exitNumpad: function () {
             this.last_total = new BigNumber(0)
             this.given = new BigNumber(0)
         },
         ...mapActions([
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

 .underline {
     border-bottom: solid 1px black;
 }
</style>
