<template>
    <div class="compra-form border-top mt-3">
      <div v-if="ventaConfirmada" class="alert alert-success mt-3">
        Compra confirmada!
      </div>
      <div v-else>
        <form @submit.prevent="submitCompra">
          <div class="mb-3">
            <label for="cantidad" class="form-label mt-2">Cantidad</label>
            <div class="d-flex justify-content-center">
                <input type="number" v-model="cantidad" id="cantidad" class="form-control w-50" min="1" required>
            </div>
          </div>
          <button type="submit" class="btn btn-success">Confirmar Compra</button>
          <button type="button" @click="cancelar" class="btn btn-secondary">Cancelar</button>
        </form>
      </div>
    </div>
  </template>
  
  <script setup>
  import { ref } from 'vue';
  import axios from 'axios';
  import { useStore } from 'vuex';
  
  const emit = defineEmits(['compra-completada', 'cancelar']);
  const props = defineProps({
    ejemplarId: Number
  });
  
  const cantidad = ref(1);
  const ventaConfirmada = ref(false);
  const store = useStore();
  
  const submitCompra = async () => {
    try {
      await axios.post('http://127.0.0.1:8000/api/ventas/', {
        cliente: store.state.user_id,
        ejemplar: props.ejemplarId,
        cantidad: cantidad.value
      }, {
        headers: {
          Authorization: `Token ${store.state.token}`
        }
      });
      emit('compra-completada');
      ventaConfirmada.value = true;
    } catch (error) {
      console.error('Error creating venta:', error);
    }
  };
  
  const cancelar = () => {
    emit('cancelar');
  };
  </script>
  
  <style scoped>
  
  </style>