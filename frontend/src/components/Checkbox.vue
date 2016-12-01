<template>
    <div class="form-group">
        <input type="checkbox"
               autocomplete="off"
               name="fancy-checkbox"
               id="fancy-checkbox"
               :checked="checked"
               @change="$emit('change')"/>
        <div class="btn-group">
            <label for="fancy-checkbox" :class="'lblchk btn btn-' + color">
                <span class="glyphicon glyphicon-ok"></span>
                <span> </span>
            </label>
            <label for="fancy-checkbox" class="lbldesc btn btn-default active">
                {{ label }}
            </label>
        </div>
    </div>
</template>

<script>
 export default {
     name: 'checkbox',
     props: {
         label: String,
         color: {
             type: String,
             default () { return 'info' }
         }
     },
     data: function () {
         return {
             checked: false
         }
     }
 }
</script>

<style>
 .form-group {
     width: 100%;
 }

 .form-group .btn-group {
     width: 100%;
 }

 .form-group .lblchk {
     float: left;
 }

 .form-group .lbldesc {
     float: left;
     width: calc(100% - 45px);
     overflow: hidden;
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
