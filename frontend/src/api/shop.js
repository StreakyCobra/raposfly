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
        }
    }
})
