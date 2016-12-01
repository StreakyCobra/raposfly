<template>
    <div class="cart">
        <h1 class="page-header">{{ $t('Cart') }}</h1>
        <div class="controls">
            <p class="total">Total: <span class="amount">{{ total }} CHF</span></p>
            <div class="buttons btn-group">
                <button class="btn btn-lg btn-success" @click="purchaseCart">{{ $t('Purchase') }}</button>
                <button class="btn btn-lg btn-danger" @click="discardCart">{{ $t('Discard') }}</button>
            </div>
        </div>
        <div class="form-group">
            <input type="checkbox" autocomplete="off" name="fancy-checkbox" id="fancy-checkbox" />
            <div class="btn-group">
                <label for="fancy-checkbox" class="mychk btn btn-info">
                    <span class="[ glyphicon glyphicon-ok ]"></span>
                    <span> </span>
                </label>
                <label for="fancy-checkbox" class="desc btn btn-default active">
                    Print Receipt
                </label>
            </div>
        </div>
        <hr />
        <template
            v-for="entry in cart">
            <item display_style=small
                  :item="entry.item"
                  :quantity="entry.quantity"
                  @clicked="removeFromCart(entry.item)"/>
        </template>
        <div id="alerts"></div>
    </div>
</template>

<script>
 import Item from './Item'
 import { mapActions, mapGetters } from 'vuex'

 export default {
     name: 'cart',
     components: {
         Item
     },
     computed: {
         total: function () {
             function add (a, b) {
                 return a + b
             }
             return this.cart.map(entry => parseFloat(entry.item.price) * entry.quantity).reduce(add, 0)
         },
         ...mapGetters([
             'cart'
         ])
     },
     methods: mapActions([
         'discardCart',
         'purchaseCart',
         'removeFromCart'
     ])
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

 #alerts {
     margin-top: 2em;
 }

 .form-group {
     width: 100%;
 }

 .form-group .btn-group {
     width: 100%;
 }

 .form-group .mychk {
     float: left;
 }

 .form-group .desc {
     float: left;
     width: calc(100% - 45px);
 }

 .form-group input[type="checkbox"] {
     display: none;
 }

 .form-group input[type="checkbox"] + .btn-group > label span {
     width: 20px;
 }

 .form-group input[type="checkbox"] + .btn-group > label span:first-child {
     display: none;
 }
 .form-group input[type="checkbox"] + .btn-group > label span:last-child {
     display: inline-block;
 }

 .form-group input[type="checkbox"]:checked + .btn-group > label span:first-child {
     display: inline-block;
 }
 .form-group input[type="checkbox"]:checked + .btn-group > label span:last-child {
     display: none;
 }
</style>
