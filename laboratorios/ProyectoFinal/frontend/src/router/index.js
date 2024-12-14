import { createRouter, createWebHistory } from 'vue-router'
import HomeView from '../views/HomeView.vue'
import AboutView from '../views/AboutView.vue'
import SearchResultsView from '../views/SearchResultsView.vue'
import AutorView from '@/views/AutorView.vue'
import CartView from '@/views/CartView.vue'
import Signup from '@/components/Signup.vue'
import Login from '@/components/Login.vue'

const routes = [
  { path: '/', name: 'home', component: HomeView },
  {
    path: '/ejemplar/:id',
    name: 'EjemplarDetail',
    component: AboutView
  },
  {
    path: '/autor/:id',
    name: 'AutorDetail',
    component: AutorView
  },
  { path: '/search', name: 'search', component: SearchResultsView },
  { path: '/cart', component: CartView },
  {
    path: '/signup',
    name: 'Signup',
    component: Signup
  },
  {
    path: '/login',
    name: 'Login',
    component: Login
  },
]

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes
})

export default router
