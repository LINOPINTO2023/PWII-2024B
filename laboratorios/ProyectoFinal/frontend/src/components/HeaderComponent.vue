<template>
    <section class="mt-5 text-center mx-auto">
        <img class="img-fluid" src="@/assets/img/fondo.png" alt="">
        <div class="mt-3">
            <button type="button" class="btn btn-info" v-for="categoria in categorias" :key="categoria.id" 
            @click="getCategoria(categoria.id, categoria.nombre)">{{ categoria.nombre }}</button>
        </div>
        <hr>
    </section>
</template>

<script setup>
    import axios from 'axios'
    import { ref, defineEmits, onMounted } from 'vue'

    const categorias = ref([])
    const categoriaID = ref(null)
    const categoriaNombre = ref(null)

    const emit = defineEmits(['getCategoriaID'])

    const getCategoria = (id, nombre) => {
        emit('getCategoriaID', id, nombre)
    }

    onMounted(() => {
        axios.get('http://127.0.0.1:8000/api/categorias/')
            .then(response => {
                categorias.value = response.data
            })
            .catch(error => {
                console.log(error)
            })
    })
</script>

<style>
    button {
        margin-right: 5px;
    }
    button + button, button:first-child {
        margin-left: 5px;
    }
    @media (max-width: 768px) {
        button {
            width: 100%;
            margin: 0 0 5px !important;
            box-sizing: border-box
        }
    }
</style>