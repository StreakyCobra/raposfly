<template>
    <div class="container">
        <h1 class="page-header">{{ $t('Welcome to raposfly') }}</h1>
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
            <router-link to="/history" tag="a" class="btn btn-info" style="width: 150px;">{{ $t('Stats') }}</router-link>
        </p>
    </div>
</template>

<script>
 export default {
     name: 'home'
 }
</script>
