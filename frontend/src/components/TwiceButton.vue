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
                 return base
             } else {
                 return [...base, 'btn-outline']
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

<style>
 .btn-outline {
     background-color: transparent !important;
     color: inherit;
     transition: all .5s;
 }

 .btn-primary.btn-outline {
     color: #428bca !important;
 }

 .btn-success.btn-outline {
     color: #5cb85c !important;
 }

 .btn-info.btn-outline {
     color: #5bc0de !important;
 }

 .btn-warning.btn-outline {
     color: #f0ad4e !important;
 }

 .btn-danger.btn-outline {
     color: #d9534f !important;
 }

 .btn-danger.btn-outline:hover {
     color: #d9534f;
 }
</style>
