export default {
    get_products: function () {
        this.$http.get('shop/store/').then((response) => {
            this.items = response.body
        }, (response) => {
            this.$bus.$emit('error', 'Impossible to load items')
        })
    }
}
