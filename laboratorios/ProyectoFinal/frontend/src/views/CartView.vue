<template>
  <div class="container mt-4">
    <h2 class="text-white">Mi Carrito</h2><br>
    <div v-if="cartItems.length" class="row d-flex justify-content-center">
      <div class="col-md-8">
        <div v-for="item in cartItems" :key="item.id" class="card mb-3">
          <div class="card-body">
            <img :src="item.imagen" class="card-img-top" alt="Imagen de {{ item.titulo }}" style="max-height: 200px; object-fit: cover;">
            <h5 class="card-title">{{ item.titulo }}</h5>
            <p class="card-text">{{ item.sinopsis }}</p>
            <p class="card-text">Precio: ${{ item.precio }}</p>
            <button @click="setActiveItem(item.id, 'compra')" class="btn btn-success">Comprar</button>
            <button @click="setActiveItem(item.id, 'prestamo')" class="btn btn-warning">Prestar</button>
            <button @click="removeFromCart(item.id)" class="btn btn-danger">Eliminar</button>
            <CompraForm v-if="activeItem.id === item.id && activeItem.type === 'compra'" :ejemplarId="item.id" @compra-completada="fetchCartItems" @cancelar="clearActiveItem"/>
            <PrestamoForm v-if="activeItem.id === item.id && activeItem.type === 'prestamo'" :ejemplarId="item.id" @prestamo-completado="fetchCartItems" @cancelar="clearActiveItem"/>
          </div>
        </div>
      </div>
    </div>
    <div class="alert alert-warning mt-3" role="alert" v-else>
      No existen ejemplares en el carrito!
    </div>
  </div>
</template>

<script setup>
import { ref, computed, onMounted } from 'vue';
import axios from 'axios';
import { useStore } from 'vuex';
import CompraForm from '@/components/CompraForm.vue';
import PrestamoForm from '@/components/PrestamoForm.vue';

const cartItems = ref([]);
const store = useStore();
const activeItem = ref({ id: null, type: '' });

const fetchCartItems = async () => {
  try {
    const response = await axios.get('http://127.0.0.1:8000/api/carritos/', {
      headers: {
        Authorization: `Token ${store.state.token}`
      }
    });

    if (response.data && response.data.length > 0) {
      const carrito = response.data[0];
      const ejemplares = carrito.ejemplar;

      if (Array.isArray(ejemplares)) {
        cartItems.value = ejemplares;
      } else {
        console.error('Error: ejemplares no es un array');
        cartItems.value = [];
      }
    } else {
      cartItems.value = [];
    }

  } catch (error) {
    console.error('Error fetching cart items:', error);
    cartItems.value = [];
  }
};

const setActiveItem = (itemId, type) => {
  activeItem.value = { id: itemId, type };
};

const clearActiveItem = () => {
  activeItem.value = { id: null, type: '' };
};

const removeFromCart = async (itemId) => {
  try {
    await axios.patch(`http://127.0.0.1:8000/api/carritos/${store.state.user_id}/`, {
      ejemplar_id: itemId
    }, {
      headers: {
        Authorization: `Token ${store.state.token}`
      }
    });
    await fetchCartItems();
  } catch (error) {
    console.error('Error removing from cart:', error);
  }
};

onMounted(fetchCartItems);
</script>

<style scoped>

</style>