<template>
    <br>
    <div class="prestamo-form border-top mt-3">
      <div v-if="prestamoConfirmado" class="alert alert-success mt-3">
        Préstamo confirmado!
      </div>
      <div v-else>
        <form @submit.prevent="submitPrestamo">
          <div class="mb-3">
            <label for="fechaDevolver" class="form-label mt-2">Fecha de Devolución</label>
            <div class="d-flex justify-content-center">
                <input 
                type="date" 
                v-model="fechaDevolver" 
                id="fechaDevolver" 
                class="form-control w-50" 
                required 
                :min="minDate"
                >
            </div>
          </div>
          <button type="submit" class="btn btn-warning">Confirmar Préstamo</button>
          <button type="button" @click="cancelar" class="btn btn-secondary">Cancelar</button>
        </form>
      </div>
    </div>
  </template>
  
  <script setup>
  import { ref, computed } from 'vue';
  import axios from 'axios';
  import { useStore } from 'vuex';
  
  const emit = defineEmits(['prestamo-completado', 'cancelar']);
  const props = defineProps({
    ejemplarId: Number
  });
  
  const fechaDevolver = ref('');
  const prestamoConfirmado = ref(false);
  const store = useStore();
  
  const minDate = computed(() => {
    const today = new Date();
    const day = String(today.getDate()).padStart(2, '0');
    const month = String(today.getMonth() + 1).padStart(2, '0');
    const year = today.getFullYear();
    return `${year}-${month}-${day}`;
  });
  
  const submitPrestamo = async () => {
    try {
      await axios.post('http://127.0.0.1:8000/api/prestamos/', {
        cliente: store.state.user_id,
        ejemplar: props.ejemplarId,
        FechaDevolver: fechaDevolver.value
      }, {
        headers: {
          Authorization: `Token ${store.state.token}`
        }
      });
      emit('prestamo-completado');
      prestamoConfirmado.value = true; 
    } catch (error) {
      console.error('Error creating prestamo:', error);
    }
  };
  
  const cancelar = () => {
    emit('cancelar');
  };
  </script>
  
  <style scoped>
  
  </style>
  