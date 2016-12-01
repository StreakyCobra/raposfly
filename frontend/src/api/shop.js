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
        purchaseItems: function (cart, receipt, cb, errorCb) {
            var body = {
                orders: cart.map((entry) => ({
                    item_id: entry.item.id,
                    quantity: entry.quantity
                })),
                receipt: receipt
            }
            console.log(body)
            this.$http.post('shop/buy/', body).then((response) => {
                cb(cart)
            }, (response) => {
                errorCb()
            })
        }
    }
})
