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
                    <router-link class="navbar-brand" :to="{name: 'home'}" exact>
                        <img style="float: left; display:inline-block; height: 1.5em;"src="/static/favicon.png" />
                        <span style="display: inline-block;">raposfly</span>
                    </router-link>
                </div>
                <div id="navbar" class="navbar-collapse collapse">
                    <ul class="nav navbar-nav">
                        <router-link :to="{name: 'shop'}" tag="li" active-class="active" exact data-toggle="collapse" data-target=".navbar-collapse.in">
                            <router-link :to="{name: 'shop'}">{{ $t('Shop') }}</router-link>
                        </router-link>
                        <router-link :to="{name: 'history'}" tag="li" active-class="active" exact data-toggle="collapse" data-target=".navbar-collapse.in">
                            <router-link :to="{name: 'history'}">{{ $t('History') }}</router-link>
                        </router-link>
                        <router-link :to="{name: 'stats'}" tag="li" active-class="active" exact data-toggle="collapse" data-target=".navbar-collapse.in">
                            <router-link :to="{name: 'stats'}">{{ $t('Stats') }}</router-link>
                        </router-link>
                    </ul>
                    <div class="navbar-right">
                        <ul class="nav navbar-nav">
                            <li class="dropdown">
                                <a class="dropdown-toggle" data-toggle="dropdown" role="button" aria-haspopup="true" aria-expanded="false">{{ $i18n.locale | uppercase }} <span class="caret"></span></a>
                                <ul class="dropdown-menu">
                                    <li><a @click="set_lang('en')">EN</a></li>
                                    <li><a @click="set_lang('fr')">FR</a></li>
                                </ul>
                            </li>
                            <router-link :to="{name: 'admin'}" tag="li" active-class="active" exact data-toggle="collapse" data-target=".navbar-collapse.in">
                                <router-link :to="{name: 'admin'}"><i class="fa fa-cog" aria-hidden="true"></i> {{ $t('Administration') }}</router-link>
                            </router-link>
                        </ul>
                    </div>
                </div>
            </div>
        </nav>

        <error ref="error"></error>

        <!-- APPLICATION -->
        <div id="view" class="container-fluid">
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
         $('#splash').delay(1000).fadeOut(500)
     },
     filters: {
         uppercase: function (val) {
             return val.toUpperCase()
         }
     },
     methods: {
         error: function (msg) {
             this.$refs.error.alert(msg)
         },
         set_lang: function (lang) {
             const route = Object.assign({}, this.$route)
             route.params.lang = lang
             this.$router.push(route)
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

 #view {
     font-family: 'Montserrat', Helvetica, Arial, sans-serif;
     position: absolute;
     top: 50px;
     bottom: 0px;
     width: 100%;
     overflow: auto;
 }

 @media (min-width: 768px){
     .innerscroll {
         height: 100%;
         overflow: hidden;
     }
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
