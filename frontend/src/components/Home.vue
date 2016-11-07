<template>
    <div class="container">
        <h1 class="page-header">Welcome to raposfly</h1>
        <p>
            You can directly access the shop:<br />
            <router-link to="/shop" tag="a" class="btn btn-info" style="width: 150px;">Shop</router-link>
        </p>
        <p>
            Or see the history from:<br />
            <router-link to="/history" tag="a" class="btn btn-info" style="width: 150px;">History</router-link>
        </p>
    </div>
</template>

<script>
 export default {
     name: 'home'
 }
</script>
