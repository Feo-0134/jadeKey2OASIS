import Vue from 'vue'
import Router from 'vue-router'

import Dashboard from './components/Dashboard'
import NewProcess from './components/NewProcess'
import ProcessDetail from './components/ProcessDetail'
import Login from './components/Login'
import AccessCell from './components/AccessCell'
import PreviousComments from './components/PreviousComments'

Vue.use(Router)

export default new Router({
    mode: 'history',
    base: process.env.BASE_URL,
    routes: [
        {
            path: '/login',
            name: 'Login',
            component: Login
        },
        {
            path: '/',
            name: 'AccessCell',
            component: AccessCell
        },
        {
            path: '/previousComments',
            name: 'PreviousComments',
            component: PreviousComments
        },
        {
            path: '/dashboard',
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