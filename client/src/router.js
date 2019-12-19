import Vue from 'vue'
import Router from 'vue-router'

import DashBoard from './components/DashBoard'
import Comment from './components/Comment'


Vue.use(Router)

export default new Router({
    mode: 'history',
    base: process.env.BASE_URL,
    routes: [
        {
            path: '/',
            name: 'DashBoard',
            component: DashBoard
        },
        {
            path: '/:id/cmt',
            name: 'Comment',
            component: Comment
        },
    ]
})