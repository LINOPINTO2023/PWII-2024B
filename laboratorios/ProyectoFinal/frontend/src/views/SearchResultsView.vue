<template>
    <div>
        <div class="mb-5" v-if="searchText">
            <br>
            <h3 class="text-white">Resultados de búsqueda para "{{ searchText }}"</h3>
            <button class="btn btn-lg btn-warning" @click="goToHome">Mostrar todos los ejemplares</button>
            <div v-if="filteredEjemplares.length === 0" class="alert alert-warning mt-3">
                No se encontraron ejemplares.
            </div>
        </div>
    <div>
        <div class="row row-cols-1 row-cols-md-3 g-4">
            <div class="col" v-for="ejemplar in filteredEjemplares" :key="ejemplar.id">
                <div class="card text-center" style="border: 2px solid gray;">
                    <img :src="ejemplar.imagen" class="card-img-top" alt="Imagen de {{ ejemplar.titulo }}" style="max-height: 200px; object-fit: cover;">
                <div class="card-body">
                    <h5 class="card-title">{{ ejemplar.titulo }}</h5>
                    <h6 class="card-subtitle mb-2 text-body-secondary">
                    <template v-for="(nombre, index) in ejemplar.nombre_autor" :key="index">
                        {{ nombre }}
                        <template v-if="index !== ejemplar.nombre_autor.length - 1">,</template>
                    </template>
                    </h6>
                    <p class="card-text">{{ ejemplar.nombre_categoria }}</p>
                    <a :href="`/ejemplar/${ejemplar.id}`" class="btn btn-info">Ver detalles</a>
                </div>
                <div class="card-footer text-danger">
                    Precio: $ {{ ejemplar.precio }}
                </div>
                </div>
            </div>
        </div>
      </div>
    </div>
  </template>
  
  <script setup>
  import { ref, onMounted, watch } from 'vue'
  import { useRoute, useRouter } from 'vue-router'
  import axios from 'axios'
  
  const route = useRoute()
  const router = useRouter()
  const searchText = ref(route.query.q || '')
  const filteredEjemplares = ref([])
  
  const fetchResults = async () => {
    if (searchText.value) {
      try {
        const response = await axios.get('http://127.0.0.1:8000/api/ejemplares/', {
          params: { search: searchText.value }
        })
        filteredEjemplares.value = response.data
      } catch (error) {
        console.log(error)
      }
    }
  }
  
  onMounted(fetchResults)
  
  watch(() => route.query.q, (newQuery) => {
    searchText.value = newQuery || ''
    fetchResults()
  })
  
  const goToHome = () => {
    router.push('/')
  }
  </script>