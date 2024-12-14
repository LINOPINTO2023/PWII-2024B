<template>
  <header-component-vue @getCategoriaID="categoriaID"/>
  <div class="mb-5" v-if="categoriaReceived">
    <h3 class="text-white">Ejemplares de la categoría {{ categoriaReceived }}</h3>
    <button class="btn btn-lg btn-warning" @click="resetFilter">Mostrar todos los ejemplares</button>
    <div class="alert alert-warning mt-3" role="alert" v-if="filteredEjemplares.length === 0">
      No existen ejemplares de la categoría <strong>{{ categoriaReceived }}</strong>
    </div>
  </div>

  <div>
    <div class="row row-cols-1 row-cols-md-4 g-4">
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
</template>

<script setup>
  import axios from 'axios'
  import HeaderComponentVue from '@/components/HeaderComponent.vue'
  import { ref, onMounted } from 'vue'

  const ejemplares = ref([])
  const filteredEjemplares = ref([])
  const categoriaReceived = ref(null)

  const categoriaID = (categoriaID, categoriaNombre) => {
    categoriaReceived.value = categoriaNombre
    if(categoriaID){
      filteredEjemplares.value = ejemplares.value.filter((ejemplar) => ejemplar.categoria === categoriaID)
    } else {
      filteredEjemplares.value = ejemplares.value
    }
  }
  const resetFilter = () => {
    categoriaReceived.value = null
    filteredEjemplares.value = ejemplares.value
  }

  onMounted(() => {
    axios.get('http://127.0.0.1:8000/api/ejemplares/')
      .then(response => {
        ejemplares.value = response.data
        filteredEjemplares.value = ejemplares.value
      })
      .catch(error => {
        console.log(error)
      })
  })
</script>
