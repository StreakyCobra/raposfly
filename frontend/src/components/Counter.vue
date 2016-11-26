<template>
    <div>
        <p>{{ count }}</p>
        <button class="btn" @click="add">Add</button>
    </div>
</template>

<script>
 import { mapState, mapMutations } from 'vuex'

 export default {
     name: 'counter',
     computed: mapState([
         'count'
     ]),
     methods: {
         ...mapMutations([
             'increment' // map this.increment() to this.$store.commit('increment')
         ]),
         ...mapMutations({
             add: 'increment' // map this.add() to this.$store.commit('increment')
         })
     }
 }
</script>
