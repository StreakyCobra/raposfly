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
            <span class="name">{{ item.name }}</span>
            <span class="price pull-right">{{ item.price }} CHF</span>
        </div>
    </div>
    <!-- List display -->
    <div v-else-if="display_style === 'list'"
         @click="clicked">
        <div :style="{ backgroundColor: this.item.color }">
            <span class="name">{{ item.name }}</span>
            <span class="price">{{ item.price }} CHF</span>
        </div>
    </div>
</template>

<script>
 export default {
     name: 'item',
     props: {
         item: {},
         display_style: String
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
 }

 .small .name {
     font-size: 1.5em;
 }
</style>
