<template>
    <div>
        <p>
            <a v-if="del" class="btn btn-danger" @click="$emit('remove', item)">x</a>
            <a v-if="add" class="btn btn-primary" @click="$emit('add', item)">+</a>
            <span class="price"> {{ item.price }} CHF</span>
            <span>{{ item.name }}</span>
        </p>
    </div>
</template>

<script>
 export default {
     name: 'item',
     props: {
         item: {},
         del: {
             default () { return false }
         },
         add: {
             default () { return false }
         }
     }
 }
</script>

<style scoped>

 .price {
     width: 10em;
     font-size: 0.8em;
     font-weight: bold;
 }
</style>
