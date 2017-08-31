<template>
    <div class="container">
        <div id="shutdown-splash">
            <div>
                <img src="/static/logo_full.png" />
                <br />
                <i id="shutdown-progress" class="fa fa-spinner fa-spin" style="font-size:48px"></i>
                <br />
                <h2>{{ $t('Raposfly is shutting down') }}.</h2>
                <h2>{{ $t('Please wait at least one minute until the animation stop spinning before unplugging the device') }}.</h2>
            </div>
        </div>
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
             shop.shutdown(() => {}, () => {})
             $('#shutdown-splash').fadeIn(100)
             $('#shutdown-progress').delay(60000).queue(function (nxt) {
                 $(this).hide()
                 nxt()
             })
         }
     },
     mounted: function () {
         $('#shutdown-splash').hide()
     }
 }
</script>

<style scoped>
 #shutdown-splash {
     z-index: 1500;
     position:absolute;
     top:0;
     left:0;
     height:100%;
     width:100%;
     background-color: #cccccc;
     background-position: center;
     background-repeat: no-repeat;
     text-align: center;
     display: flex;
     align-items: center;
     justify-content: center;
 }

 #shutdown-splash img {
     width: 100%;
     max-width: 888px;
 }
</style>
