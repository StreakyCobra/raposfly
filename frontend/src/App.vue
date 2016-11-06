<template>
    <div>

        <!-- NAVBAR -->
        <nav class="navbar navbar-inverse navbar-fixed-top">
            <div class="container">
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
                            <router-link to="/shop">Shop</router-link>
                        </router-link>
                        <router-link to="/history" tag="li" active-class="active" exact data-toggle="collapse" data-target=".navbar-collapse.in">
                            <router-link to="/history">History</router-link>
                        </router-link>
                    </ul>
                    <div class="navbar-right">
                        <ul class="nav navbar-nav">
                            <li><a href="//backend.raposfly.io/admin"><i class="fa fa-cog" aria-hidden="true"></i> Admin</a></li>
                        </ul>
                    </div>
                </div>
            </div>
        </nav>

        <!-- APPLICATION -->
        <div id="view" style="padding-top: 50px;">
            <router-view></router-view>
        </div>

    </div>
</template>

<script>
 import Shop from './components/Shop'
 import Cart from './components/Cart'

 var $ = require('jquery')

 export default {
     name: 'app',
     components: {
         Shop,
         Cart
     },
     mounted: function () {
         $('#splash').delay(1000).fadeOut(1000)
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
</style>
