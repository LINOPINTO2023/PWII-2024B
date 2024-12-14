<template>
  <div  class="text-end">
    
    <div class="text-end">
      <div v-if="!isLoggedIn">
          <button type="button" class="btn btn-outline-light me-2"><a href="/login" class="nav-link px-2 text-white">Login</a></button>
          <button type="button" class="btn btn-warning"><a href="/Signup" class="nav-link px-2 text-white">Sign-up</a></button>
      </div>    
      <div v-if="isLoggedIn">
          <button @click="cerrarSesion" type="button" class="btn btn-outline-light me-2"><a href="/about" class="nav-link px-2 text-white">cerrar sesion</a></button>  
      </div>           
    </div>
  </div>
</template>

<script>

export default{
  name:'Logout',
  computed:{isLoggedIn() {
                return !!localStorage.getItem('token');
            }
        },
        methods:{
          cerrarSesion(){
            this.$store.dispatch('logout');
            this.$router.push('/')
          }
        }

}
</script>