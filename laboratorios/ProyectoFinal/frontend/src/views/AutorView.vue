<template>
    <div class="container mt-4">
      <div v-if="autor" class="row justify-content-center">
        <div class="col-3">
          <img :src="autor.imagen" alt="Imagen del ejemplar" class="img-fluid" style="max-width: 100%; height: auto;">
        </div>
        
        <div class="col-5 bg-light p-4 text-align-left rounded">
          <div>
            <h3>{{ autor.nombre }}</h3>
            <p class="text-start"><strong>Nacionalidad:</strong> {{ autor.nacionalidad }}</p>
            <p class="text-start"><strong>Biografía:</strong> {{ autor.biografia }}</p>
            <button class="btn btn-primary" @click="goBack">Volver</button>
          </div>
        </div>
      </div>
  
      <div v-if="autor && autorEjemplares.length" class="mt-5">
        <h3 class="text-white">Más ejemplares de <strong>{{ autor.nombre }}</strong></h3><br>
        <div class="row">
          <div class="col-md-3 mb-4" v-for="ejemplar in autorEjemplares" :key="ejemplar.id">
            <div class="card">
              <img :src="ejemplar.imagen" class="card-img-top" alt="Imagen de {{ ejemplar.titulo }}" style="max-height: 200px; object-fit: cover;">
              <div class="card-body">
                <h5 class="card-title">{{ ejemplar.titulo }}</h5>
                <p class="card-text">{{ ejemplar.nombre_categoria }}</p>
                <a :href="`/ejemplar/${ejemplar.id}`" class="btn btn-info">Ver detalles</a>
              </div>
            </div>
          </div>
        </div>
      </div>
      <div v-else-if="autor" class="alert alert-warning mt-3">
        No hay más ejemplares disponibles de <strong>{{ autor.nombre }}</strong>.
      </div>

      <div v-if="otrosEjemplares.length" class="mt-5">
        <h3 class="text-white">Otros ejemplares</h3><br>
        <div class="row">
          <div class="col-md-3 mb-4" v-for="ejemplar in otrosEjemplares" :key="ejemplar.id">
            <div class="card">
              <img :src="ejemplar.imagen" class="card-img-top" alt="Imagen de {{ ejemplar.titulo }}" style="max-height: 200px; object-fit: cover;">
              <div class="card-body">
                <h5 class="card-title">{{ ejemplar.titulo }}</h5>
                <p class="card-text">{{ ejemplar.nombre_categoria }}</p>
                <a :href="`/ejemplar/${ejemplar.id}`" class="btn btn-info">Ver detalles</a>
              </div>
            </div>
          </div>
        </div>
      </div>
      <div v-else class="alert alert-warning mt-3">
        No hay otros ejemplares disponibles.
      </div>
    </div>
  </template>
  
  <script setup>
  import { ref, onMounted } from 'vue'
  import { useRoute, useRouter } from 'vue-router'
  import axios from 'axios'
  
  const route = useRoute()
  const router = useRouter()
  
  const autor = ref(null)
  const otrosEjemplares = ref([])
  const autorEjemplares = ref([])
  
  const fetchAutor = async () => {
    const autorId = Number(route.params.id)
    try {
      const response = await axios.get(`http://127.0.0.1:8000/api/autores/${autorId}/`)
      autor.value = response.data
  
      const otherResponse = await axios.get('http://127.0.0.1:8000/api/ejemplares/')
      otrosEjemplares.value = otherResponse.data.filter(ejemplar => !ejemplar.autor.includes(autorId))
      autorEjemplares.value = otherResponse.data.filter(ejemplar => ejemplar.autor.includes(autorId))
    } catch (error) {
      console.error('Error fetching ejemplar:', error)
    }
  }
  
  onMounted(fetchAutor)
  
  const goBack = () => {
    router.back()
  }
  </script>
  
  <style>
  
  </style>