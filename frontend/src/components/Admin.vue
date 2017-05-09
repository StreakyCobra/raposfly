<template>
    <div class="container">
        <h1 class="page-header">{{ $t('Administration') }}</h1>
        <p>
            {{ $t('Access the database administration') }}:<br />
            <a class="btn btn-info" :href="this.$backend_url + '/admin'"><i class="fa fa-external-link" aria-hidden="true"></i> {{ $t('Database administration') }}</a>
        </p>
        <p>
            {{ $t('Shutdown the device') }}:<br />
            <twiceButton button="Shutdown" confirmation="Are you sure?" type="btn-danger" icon="fa-power-off" @click="shutdown"></twiceButton>
        </p>
    </div>
</template>

<script>
 import shop from '../api/shop.js'
 import TwiceButton from './TwiceButton'
 var $ = require('jquery')

 export default {
     name: 'admin',
     components: {
         TwiceButton
     },
     data: function () {
         return {
             event: 'Welcome to raposfly'
         }
     },
     methods: {
         shutdown: function () {
             shop.shutdown(() => {
                 $('#splash').fadeIn()
             }, () => {})
         }
     }
 }
</script>
