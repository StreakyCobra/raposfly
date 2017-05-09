<template>
    <div class="noselect">
        <!-- NAVBAR -->
        <nav class="navbar navbar-inverse navbar-fixed-top">
            <div class="container-fluid">
                <div class="navbar-header">
                    <button type="button" class="navbar-toggle collapsed" data-toggle="collapse" data-target="#navbar" aria-expanded="false" aria-controls="navbar">
                        <span class="sr-only">Toggle navigation</span>
                        <span class="icon-bar"></span>
                        <span class="icon-bar"></span>
                        <span class="icon-bar"></span>
                    </button>
                    <router-link class="navbar-brand" to="/" exact>
                        <img style="float: left; display:inline-block; height: 1.5em;"src="/static/favicon.png" />
                        <span style="display: inline-block;">raposfly</span>
                    </router-link>
                </div>
                <div id="navbar" class="navbar-collapse collapse">
                    <ul class="nav navbar-nav">
                        <router-link to="/shop" tag="li" active-class="active" exact data-toggle="collapse" data-target=".navbar-collapse.in">
                            <router-link to="/shop">{{ $t('Shop') }}</router-link>
                        </router-link>
                        <router-link to="/history" tag="li" active-class="active" exact data-toggle="collapse" data-target=".navbar-collapse.in">
                            <router-link to="/history">{{ $t('History') }}</router-link>
                        </router-link>
                        <router-link to="/stats" tag="li" active-class="active" exact data-toggle="collapse" data-target=".navbar-collapse.in">
                            <router-link to="/stats">{{ $t('Stats') }}</router-link>
                        </router-link>
                    </ul>
                    <div class="navbar-right">
                        <ul class="nav navbar-nav">
                            <li><a @click="setLang('en')">EN</a></li>
                            <li><a @click="setLang('fr')">FR</a></li>
                        </ul>
                        <ul class="nav navbar-nav">
                            <li><a :href="this.$backend_url + '/admin'"><i class="fa fa-cog" aria-hidden="true"></i> {{ $t('Admin') }}</a></li>
                        </ul>
                    </div>
                </div>
            </div>
        </nav>

        <error ref="error"></error>

        <!-- APPLICATION -->
        <div id="view" class="container-fluid" style="padding-top: 50px;">
            <router-view @error="error"></router-view>
        </div>
    </div>
</template>

<script>
 import Error from './components/Error'
 var $ = require('jquery')

 export default {
     name: 'app',
     components: {
         Error
     },
     mounted: function () {
         $('#splash').delay(1000).fadeOut(1000)
     },
     methods: {
         error: function (msg) {
             this.$refs.error.alert(msg)
         },
         setLang: function (lang) {
             this.$i18n.locale = lang
         }
     }
 }
</script>

<style>
 @font-face {
     font-family: 'Montserrat';
     src: url('/static/fonts/Montserrat-Regular.otf');
     font-weight: normal;
 }

 @font-face {
     font-family: 'Montserrat';
     src: url('/static/fonts/Montserrat-Bold.otf');
     font-weight: bold;
 }

 #app {
     font-family: 'Montserrat', Helvetica, Arial, sans-serif;
 }

 .noselect {
     -webkit-touch-callout: none; /* iOS Safari */
     -webkit-user-select: none; /* Chrome/Safari/Opera */
     -khtml-user-select: none; /* Konqueror */
     -moz-user-select: none; /* Firefox */
     -ms-user-select: none; /* Internet Explorer/Edge */
     user-select: none; /* Non-prefixed version, currently
                           not supported by any browser */
 }

 .container {
     margin-bottom: 1em;
 }
</style>
