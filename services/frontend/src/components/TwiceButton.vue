<template>
    <button :class="classes"
            @blur="reset"
            @click="trigger">
        <i :class="['fa', this.icon]"></i>
        {{ $t(message) }}
    </button>
</template>

<script>
 export default {
     name: 'twiceButton',
     props: {
         button: '',
         confirmation: '',
         type: '',
         icon: ''
     },
     computed: {
         message: function () {
             if (this.triggered) {
                 return this.confirmation
             } else {
                 return this.button
             }
         },
         classes: function () {
             var base = ['btn', this.type]
             if (this.triggered) {
                 return [...base, 'btn-outline']
             } else {
                 return base
             }
         }
     },
     data: function () {
         return {
             triggered: false
         }
     },
     methods: {
         trigger: function () {
             if (this.triggered) {
                 this.$emit('click')
                 this.reset()
             } else {
                 this.triggered = true
             }
         },
         reset: function () {
             this.triggered = false
         }
     }
 }
</script>
