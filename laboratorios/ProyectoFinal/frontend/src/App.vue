<template>
  <navbar-component-vue/>
  <div class="container">
    <router-view/>
    <footer-component-vue/>
  </div>
</template>

<script setup>
  import FooterComponentVue from './components/FooterComponent.vue'
  import NavbarComponentVue from './components/NavbarComponent.vue'
  import { onMounted } from 'vue'
  import { useStore } from 'vuex';

  const store = useStore();

  onMounted(() => {
    store.commit('initializeStore');
  });
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
}

nav {
  padding: 30px;
}

nav a {
  font-weight: bold;
  color: #2c3e50;
}

nav a.router-link-exact-active {
  color: #42b983;
}
</style>
