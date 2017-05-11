import Vue from 'vue'
import VueRouter from 'vue-router'
import Home from './components/Home'
import Shop from './components/Shop'
import History from './components/History'
import Stats from './components/Stats'
import Admin from './components/Admin'

Vue.use(VueRouter)
const routes = [
    {
        path: '/:lang/',
        name: 'home',
        component: Home
    },
    {
        path: '/:lang/shop',
        name: 'shop',
        component: Shop
    },
    {
        path: '/:lang/history',
        name: 'history',
        component: History
    },
    {
        path: '/:lang/stats',
        name: 'stats',
        component: Stats
    },
    {
        path: '/:lang/admin',
        name: 'admin',
        component: Admin
    },
    {
        path: '*',
        redirect: '/en/'
    }
]

export default new VueRouter({
    mode: 'history',
    routes: routes
})
