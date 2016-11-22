<template>
    <div @click="clicked(item)">
        <!-- Big display -->
        <div v-if="style === 'big'"
             class="big item panel panel-default">
            <div v-if="show_quantity" class="panel-heading">
                <span class="quantity">{{ String(this.quantity) }}×</span>
            </div>
            <div class="panel-body" :style="{ backgroundColor: this.item.color }">
                <span class="name">{{ item.name }}</span>
                <img :src="item_image(item)"/>
            </div>
            <div class="panel-footer">
                <span class="price"> {{ item.quantity * item.price }} CHF</span>
            </div>
        </div>
        <!-- Small display -->
        <div v-if="style == 'small'"
             class="small item panel panel-default">
            <div class="panel-body" :style="{ backgroundColor: this.item.color }">
                <span v-if="show_quantity" class="quantity">{{ String(this.quantity) }}×</span>
                <span class="name">{{ item.name }}</span>
                <span class="price pull-right">{{ item.quantity * item.price }} CHF</span>
            </div>
        </div>
        <!-- List display -->
        <div v-if="style == 'list'"
             class="small item panel panel-default">
            <div :style="{ backgroundColor: this.item.color }">
                <span v-if="show_quantity" class="quantity">{{ String(this.quantity) }}×</span>
                <span class="name">{{ item.name }}</span>
                <span class="price">{{ item.quantity * item.price }} CHF</span>
            </div>
        </div>
    </div>
</template>

<script>
 export default {
     name: 'item',
     props: {
         item: {},
         style: String,
         show_quantity: {
             type: Boolean,
             default () { return true }
         }
     },
     methods: {
         clicked: function (item) {
             this.$emit('clicked', item)
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
 }

 .big .panel-body {
     height: 100px;
 }

 .big .panel-footer {
     overflow: auto;
     padding: 3px;
 }

 .big .name {
     font-size: 2em;
 }

 .big .price, .big .quantity {
     font-size: 1em;
     font-weight: bold;
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
 }

 .small .quantity {
     height: 100%;
     vertical-align: middle;
 }

 .small .name {
     font-size: 1.5em;
 }
</style>
