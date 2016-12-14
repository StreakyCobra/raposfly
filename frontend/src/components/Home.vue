<template>
    <div class="container">
        <h1 class="page-header">{{ $t(event) }}</h1>
        <h2>{{ $t('Usage') }}</h2>
        <p>
            {{ $t('You can directly access the shop') }}:<br />
            <router-link to="/shop" tag="a" class="btn btn-info" style="width: 150px;">{{ $t('Shop') }}</router-link>
        </p>
        <p>
            {{ $t('Or see the history from') }}:<br />
            <router-link to="/history" tag="a" class="btn btn-info" style="width: 150px;">{{ $t('History') }}</router-link>
        </p>
        <p>
            {{ $t('And finally access stats through') }}:<br />
            <router-link to="/stats" tag="a" class="btn btn-info" style="width: 150px;">{{ $t('Stats') }}</router-link>
        </p>
        <hr />
        <h2>{{ $t('Administration') }}</h2>
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
     name: 'home',
     components: {
         TwiceButton
     },
     data: function () {
         return {
             event: 'Welcome to raposfly'
         }
     },
     mounted: function () {
         this.$http.get('shop/config/').then((response) => {
             this.event = response.body['EVENT_NAME']
         }, (response) => {
             this.$bus.$emit('error', 'Impossible to connect to the database')
         })
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
