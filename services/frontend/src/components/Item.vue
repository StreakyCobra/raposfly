<template>
    <!-- Big display -->
    <div v-if="display_style === 'big'"
         class="padded">
        <div class="big item panel panel-default"
             >
          <div class="panel-body"
               :style="{ backgroundColor: this.item.color,
                      backgroundImage: 'url(' + item_image(item) + ')',
                      backgroundRepeat: 'no-repeat',
                      backgroundPosition: 'right',
                      backgroundOrigin: 'content-box',
                      backgroundSize: 'auto 100%'}"
               @click="clicked">
                <span class="quantity btn-xs" v-if="quantity">{{ quantity }}×</span>
                <span class="name">{{ item.name }}</span>
            </div>
            <div class="panel-footer">
                <span class="info"
                      data-toggle="tooltip"
                      :title="info">
                    <i class="fa fa-info-circle"></i>
                </span>
                <span class="price"> {{ total_price.toFormat(2) }} CHF</span>
            </div>
        </div>
    </div>
    <!-- Small display -->
    <div v-else-if="display_style === 'small'"
         class="small item panel panel-default"
         @click="clicked">
        <div class="panel-body" :style="{ backgroundColor: this.item.color }">
            <span class="price pull-right">{{ total_price.toFormat(2) }} CHF</span>
            <span class="quantity btn-xs" v-if="quantity">{{ quantity }}×</span>
            <span class="name">{{ item.name }}</span>
        </div>
    </div>
    <!-- List display -->
    <div v-else-if="display_style === 'list'"
         class="list"
         @click="clicked">
        <div>
            <span class="price pull-right">{{ total_price.toFormat(2) }} CHF</span>
            <span v-if="quantity"
                  class="quantity btn-xs"
                  :style="{ backgroundColor: this.item.color }">
                {{ quantity }}×
            </span>
            <span class="name">{{ item.name }}</span>
        </div>
    </div>
</template>

<script>
 import BigNumber from '../math.js'
 var $ = require('jquery')

 export default {
     name: 'item',
     props: {
         item: {},
         display_style: String,
         quantity: {
             type: Number,
             default () { return 0 }
         }
     },
     computed: {
         total_price: function () {
             if (this.quantity <= 0) return new BigNumber(this.item.price)
             return new BigNumber(this.item.price).times(this.quantity)
         },
         info: function () {
             var text = ''
             text += this.item.name
             if (this.item.description) text += '<br /><br />' + this.item.description
             return text
         }
     },
     mounted: function () {
         $('[data-toggle="tooltip"]').tooltip({
             placement: 'bottom',
             trigger: 'click focus',
             html: true
         })
     },
     methods: {
         clicked: function (item) {
             this.$emit('click', item, this.$el)
         },
         item_image: function (item) {
             return this.$backend_url + item.image
         }
     }
 }
</script>

<style scoped>
 .item {
     box-shadow: 5px 5px 5px -2px gray;
     cursor: pointer;
     overflow-x: hidden;
 }

 .padded {
     padding: 10px;
 }

 .big.panel {
     margin-bottom: 0 !important;
 }

 .panel-body {
     border-radius: 4px;
 }

 .big .panel-body {
     height: 100px;
     white-space: nowrap;
     overflow: hidden;
 }

 .big .panel-footer {
     overflow: auto;
     padding: 3px;
 }

 .big .name {
     overflow: hidden;
     font-size: 2em;
     display: block;
     text-overflow: ellipsis;
 }

 .big .quantity {
     font-size: 1.5em;
 }

 .big .price {
     font-size: 1em;
     font-weight: bold;
 }

 .big .info {
     font-size: 1em;
     font-weight: bold;
     padding-left: 5px;
 }

 .big .price {
     float: right;
 }

 .big img {
     float: right;
     height: 100%;
 }

 .small .panel-body {
     height: 100%;
     white-space: nowrap;
     overflow: hidden;
 }

 .quantity {
     border: solid 1px #222222;
     margin-right: 0.5em;
 }

 .small .quantity, .small .name, .small .price {
     font-size: 1.5em;
 }

 .small .name {
     overflow: hidden;
     display: inline-block;
     text-overflow: ellipsis;
 }

 .small .price {
   position: relative;
   padding-left: 10px;
   background: inherit;
 }

</style>
