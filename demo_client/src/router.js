import Vue from 'vue'
import Router from 'vue-router'

import Dashboard from './components/Dashboard'
import NewProcess from './components/NewProcess'
import ProcessDetail from './components/ProcessDetail'

Vue.use(Router)

export default new Router({
    mode: 'history',
    base: process.env.BASE_URL,
    routes: [
        {
            path: '/',
            name: 'Dashboard',
            component: Dashboard
        },
        {
            path: '/newProcess',
            name: 'NewProcess',
            component: NewProcess
        },
        {
            path: '/processDetail/:id',
            name: 'ProcessDetail',
            component: ProcessDetail
        },

    ]
})