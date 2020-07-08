import Vue from 'vue'
import Router from 'vue-router'
import VueResource from 'vue-resource'
import Login from '@/components/Login'
import Mine from '@/components/User/Mine'
import Experiment from '@/components/User/Experiment'
import ExperimentDetail from '@/components/User/ExperimentDetail'
import Jaccountbound from '@/components/User/Jaccountbound'
import Score from '@/components/User/Score'
import Ex1 from '@/components/User/Ex1'
import Ex2 from '@/components/User/Ex2'
import Ex3 from '@/components/User/Ex3'
import Ex4 from '@/components/User/Ex4'

Vue.use(Router)
Vue.use(VueResource)

export default new Router({
  // mode: 'history',
  routes: [
    {
      path: '/',
      name: 'Login',
      component: Login
    },
    {
      path: '/User/Mine',
      name: 'Mine',
      component: Mine
    },
    {
      path: '/User/Experiment',
      name: 'Experiment',
      component: Experiment
    },
    {
      path: '/User/ExperimentDetail',
      name: 'ExperimentDetail',
      component: ExperimentDetail
    },
    {
      path: '/User/Score',
      name: 'Score',
      component: Score
    },
    {
      path: '/User/Jaccountbound',
      name: 'Jaccountbound',
      component: Jaccountbound
    },
    {
      path: '/User/Ex1',
      name: 'Ex1',
      component: Ex1
    },
    {
      path: '/User/Ex2',
      name: 'Ex2',
      component: Ex2
    },
    {
      path: '/User/Ex3',
      name: 'Ex3',
      component: Ex3
    },
    {
      path: '/User/Ex4',
      name: 'Ex4',
      component: Ex4
    }
  ]
})
