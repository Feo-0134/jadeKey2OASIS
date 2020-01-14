import Vue from 'vue'
import Router from 'vue-router'

import NewProcess from './components/NewProcess'


Vue.use(Router)

export default new Router({
    mode: 'history',
    base: process.env.BASE_URL,
    routes: [
        {
            path: '/newProcess',
            name: 'New Process',
            component: NewProcess
        },
    ]
})