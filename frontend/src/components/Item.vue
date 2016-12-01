<template>
    <!-- Big display -->
    <div v-if="display_style === 'big'"
         class="big item panel panel-default"
         @click="clicked">
        <div class="panel-body" :style="{ backgroundColor: this.item.color,
                                        backgroundImage: 'url(' + item_image(item) + ')',
                                        backgroundRepeat: 'no-repeat',
                                        backgroundPosition: 'right',
                                        backgroundOrigin: 'content-box',
                                        backgroundSize: 'auto 100%'}">
            <span class="quantity btn-xs" v-if="quantity">{{ quantity }}×</span>
            <span class="name">{{ item.name }}</span>
        </div>
        <div class="panel-footer">
            <span class="price"> {{ item.price }} CHF</span>
        </div>
    </div>
    <!-- Small display -->
    <div v-else-if="display_style === 'small'"
         class="small item panel panel-default"
        @click="clicked">
        <div class="panel-body" :style="{ backgroundColor: this.item.color }">
            <span class="price pull-right">{{ item.price }} CHF</span>
            <span class="quantity btn-xs" v-if="quantity">{{ quantity }}×</span>
            <span class="name">{{ item.name }}</span>
        </div>
    </div>
    <!-- List display -->
    <div v-else-if="display_style === 'list'"
         class="list"
         @click="clicked">
        <div>
            <span class="price pull-right">{{ quantity * item.price }} CHF</span>
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
     font-size: 2em;
 }

 .big .quantity {
     font-size: 1.5em;
 }

 .big .price {
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
     display: inline;
     overflow: hidden;
 }

</style>
