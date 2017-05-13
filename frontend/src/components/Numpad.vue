<template>
    <div class="numpad">
        <div class="btn btn-info button" @click="digit(1)">
            1
        </div>
        <div class="btn btn-info button" @click="digit(2)">
            2
        </div>
        <div class="btn btn-info button" @click="digit(3)">
            3
        </div>
        <div class="btn btn-info button" @click="digit(4)">
            4
        </div>
        <div class="btn btn-info button" @click="digit(5)">
            5
        </div>
        <div class="btn btn-info button" @click="digit(6)">
            6
        </div>
        <div class="btn btn-info button" @click="digit(7)">
            7
        </div>
        <div class="btn btn-info button" @click="digit(8)">
            8
        </div>
        <div class="btn btn-info button" @click="digit(9)">
            9
        </div>
        <div class="btn btn-danger button" @click="erase">
            <i class="fa fa-remove"></i>
        </div>
        <div class="btn btn-info button" @click="digit(0)">
            0
        </div>
        <div class="btn btn-success button" @click="dot">
            •
        </div>
    </div>
</template>

<script>
 import BigNumber from '../math.js'

 export default {
     name: 'numpad',
     data: function () {
         return {
             value: ''
         }
     },
     methods: {
         digit: function (val) {
             this.value += val
             this.input()
         },
         erase: function () {
             this.value = ''
             this.input()
         },
         dot: function () {
             if (this.value.indexOf('.') === -1) {
                 this.value += '.'
                 this.input()
             }
         },
         input: function () {
             this.$emit('input', new BigNumber(this.value || 0))
         }
     }
 }
</script>

<style scoped>
 .number {
     display: flex;
     flex-wrap: wrap;
     width: 100%;
 }

 .button {
     display: inline-flex;
     flex: 1 1 33%;
     width: 31%;
     margin: 0px 0px 4px 0px;
     justify-content: center;
     align-items: center;
     height: 50px;
     cursor: pointer;
 }

</style>
