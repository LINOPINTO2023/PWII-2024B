<template>
    <header class="p-3 text-bg-dark">
        <div class="container">
            <div class="d-flex flex-column flex-lg-row align-items-center justify-content-between">
                <ul class="nav mb-2 mb-lg-0">
                    <li class="nav-item"><a href="/" class="nav-link px-2 text-white">Home</a></li>
                </ul>
                <form class="d-flex col-lg-4 mb-3 mb-lg-0 justify-content-center justify-content-lg-center" role="search" @submit.prevent="getSearch">
                    <input type="text" class="form-control form-control-dark me-1" style="max-width: 350px;" placeholder="Search..." aria-label="Search" v-model="searchText">
                    <button type="submit" class="btn btn-success">Buscar</button>
                </form>
                <div class="text-end">
                    <template v-if="!isAuthenticated">
                        <router-link type="button" to="/login">
                            <button type="button" class="btn btn-outline-light me-2">Login</button>
                        </router-link>
                        <router-link to="/signup">
                            <button type="button" class="btn btn-warning">Sign-up</button>
                        </router-link>
                    </template>
                    <template v-else>
                        <span class="text-white me-3">Bienvenido, <strong>{{ userName }}</strong>!</span>
                        <button type="button" class="btn btn-outline-light me-2" @click="logout">Logout</button>
                    </template>
                </div>
            </div>
        </div>
    </header>
</template>
  
<script setup>
import Logout from './Logout.vue';
import { ref, computed, onMounted } from 'vue'
import { useRouter } from 'vue-router'
import { useStore } from 'vuex'

const searchText = ref('')
const router = useRouter()
const store = useStore()

const isAuthenticated = computed(() => store.state.isAuthenticated)
const userName = computed(() => store.getters.username)

const getSearch = () => {
  if (searchText.value.trim()) {
    router.push({ name: 'search', query: { q: searchText.value } })
  }
}
const logout = async () => {
  await store.dispatch('logout')
  router.push('/')
}
onMounted(() => {
  store.commit('initializeStore')
})
</script>