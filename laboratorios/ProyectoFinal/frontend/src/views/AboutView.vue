<template>
  <div class="container mt-4">
    <div v-if="ejemplar" class="row justify-content-center">
      <div class="col-3">
        <img :src="ejemplar.imagen" alt="Imagen del ejemplar" class="img-fluid" style="max-width: 100%; height: auto;">
      </div>
      
      <div class="col-5 bg-light border p-4 rounded">
        <div>
          <h3>{{ ejemplar.titulo }}</h3>
          <p class="text-start"><strong>Categoría:</strong> {{ ejemplar.nombre_categoria }}</p>
          <p class="text-start"><strong>Año:</strong> {{ ejemplar.año }}</p>
          <p class="text-start"><strong>Sinopsis:</strong> {{ ejemplar.sinopsis }}</p>
          <p class="text-start"><strong>Páginas:</strong> {{ ejemplar.paginas }}</p>
          <p class="text-start"><strong>Precio:</strong> $ {{ ejemplar.precio }}</p>
          <p class="text-start"><strong>Autores: </strong> 
            <template v-for="(autor, index) in ejemplar.nombre_autor" :key="index">
                <a :href="`/autor/${ejemplar.autor[index]}`">{{ autor }}</a><template v-if="index !== ejemplar.nombre_autor.length - 1"> · </template>
              </template>
          </p>
          <p class="text-start"><strong>Temas: </strong> 
            <template v-for="(tema, index) in ejemplar.nombre_tema" :key="index">
                {{ tema }}<template v-if="index !== ejemplar.nombre_tema.length - 1"> · </template>
              </template>
          </p>
          <div class="d-flex align-items-center">
            <button class="btn btn-primary" @click="goBack">Volver</button>
            <div v-if="isAuthenticated" class="ms-2">
              <button class="btn btn-success me-2" @click="addToCart(ejemplar)">Añadir al carrito</button>
              <button class="btn btn-success" @click="goToCart">Ver carrito</button>
            </div>
          </div>
        </div>
      </div>
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
import { ref, onMounted, computed } from 'vue'
import { useRoute, useRouter } from 'vue-router'
import axios from 'axios'
import { useStore } from 'vuex'

const route = useRoute()
const router = useRouter()
const store = useStore()

const ejemplar = ref(null)
const otrosEjemplares = ref([])
const isAuthenticated = computed(() => !!store.state.token)

const fetchEjemplar = async () => {
  const ejemplarId = route.params.id
  try {
    const response = await axios.get(`http://127.0.0.1:8000/api/ejemplares/${ejemplarId}/`)
    ejemplar.value = response.data

    const otherResponse = await axios.get('http://127.0.0.1:8000/api/ejemplares/')
    otrosEjemplares.value = otherResponse.data.filter(e => e.id !== parseInt(ejemplarId))
  } catch (error) {
    console.error('Error fetching ejemplar:', error)
  }
}

onMounted(fetchEjemplar)

const goBack = () => {
  router.back()
}

const goToCart = () => {
  router.push('/cart')
}

const addToCart = async (ejemplar) => {
  try {
    await store.dispatch('addToCart', ejemplar);
    alert('Ejemplar añadido al carrito');
  } catch (error) {
    console.error('Error adding ejemplar to cart:', error);
  }
};
</script>

<style>

</style>