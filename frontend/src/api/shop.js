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
            var body = cart.map((entry) => ({
                item_id: entry.item.id,
                quantity: entry.quantity
            }))
            this.$http.post('shop/buy/', body).then((response) => {
                cb(cart)
            }, (response) => {
                errorCb()
            })
        }
    }
})
