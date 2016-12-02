import Vue from 'vue'

export default new Vue({
    methods: {
        getItems: function (cb, errorCb) {
            this.$http.get('shop/store/').then((response) => {
                cb(response.body)
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
            this.$http.post('shop/buy/', body).then((response) => {
                cb(cart)
            }, (response) => {
                errorCb()
            })
        },
        getHistory: function (cb, errorCb) {
            this.$http.get('shop/history/').then((response) => {
                cb(response.body)
            }, (response) => {
                errorCb()
            })
        },
        deletePurchase: function (purchase, cb, errorCb) {
            this.$http.delete('shop/purchases/' + purchase.id + '/').then((response) => {
                cb(purchase)
            }, (response) => {
                errorCb()
            })
        },
        printReceipt: function (purchase, cb, errorCb) {
            var body = {
                purchase_id: purchase.id
            }
            this.$http.post('shop/print-receipt/', body).then((response) => {
                cb(purchase)
            }, (response) => {
                errorCb()
            })
        }
    }
})
