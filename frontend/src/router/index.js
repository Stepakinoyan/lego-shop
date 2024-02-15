import { createRouter, createWebHistory } from 'vue-router'
import HomeView from '../views/HomeView.vue'
import Registry from '../components/Registry.vue'
import Login from '../components/Login.vue'
import Modal from '../components/Modal.vue'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: '/',
      component: HomeView
    },
    {
      path: '/signup',
      name: 'signup',
      component: Registry
    },
    {
      path: '/login',
      name: 'login',
      component: Login
    },
    {
      path: '/modal',
      name: 'modal',
      component: Modal
    }
  ]
})

export default router