import Vue from 'vue'

export default new Vue({
    methods: {
        getItems: function (cb, errorCb) {
            this.$http.get('shop/store/').then((response) => {
                var items = response.body
                cb(items)
            }, (response) => {
                errorCb()
            })
        },
        purchaseItems: function (cart, cb, errorCb) {
            this.$http.post('shop/buy/', cart).then((response) => {
                cb(cart)
            }, (response) => {
                errorCb()
            })
        }
    }
})
