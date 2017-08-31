<template>
    <div class="container">
        <div class="logo"><img src="/static/logo_full.png"/></div>
        <h1 class="page-header"><center>{{ event }}</center></h1>
        <div class="row">
            <div class="section col-md-4">
                <router-link :to="{name: 'shop'}" tag="a" class="halfwidth btn btn-info">
                    <i class="icon fa fa-shopping-basket"></i>
                    <br />
                    <div class="description">{{ $t('Shop') }}</div>
                </router-link>
            </div>
            <div class="section col-md-4">
                <router-link :to="{name: 'history'}" tag="a" class="halfwidth btn btn-info">
                    <i class="icon fa fa-history"></i>
                    <br />
                    <div class="description">{{ $t('History') }}</div>
                </router-link>
            </div>
            <div class="section col-md-4">
                <router-link :to="{name: 'stats'}" tag="a" class="halfwidth btn btn-info">
                    <i class="icon fa fa-line-chart"></i>
                    <br />
                    <div class="description">{{ $t('Stats') }}</div>
                </router-link>
            </div>
        </div>
    </div>
</template>

<script>
 export default {
     name: 'home',
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
     }
 }
</script>

<style scoped>
 .section {
     text-align: center;
 }

 .halfwidth {
     padding-top: 2em;
     width: 50%;
 }

 .icon {
     font-size: 4em;
 }

 .description {
     font-size: 1.5em;
     font-weight: bold;
     margin-top: 2em;
 }

 .logo {
     text-align: center;
     max-width: 100%;
 }

 .logo img {
     max-width: 100%;
 }
</style>
