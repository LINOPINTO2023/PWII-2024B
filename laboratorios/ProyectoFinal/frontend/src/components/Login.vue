<template>
    <div class="container-fluid d-flex mt-5 mb-5 justify-content-center align-items-center">
    <div class="bg-white p-4 rounded shadow">
      <form @submit.prevent="submitForm" class="mx-auto">
        <h4 class="text-center mb-4">Inicio de Sesion</h4>
        <div class="mb-3">
          <label class="form-label">Email</label>
          <input v-model="email" type="email" placeholder="Ingresa tu email" class="form-control">
          <small v-if="errors.email" class="text-danger">{{ errors.email }}</small>
        </div>
        <div class="mb-3">
          <label class="form-label">Password</label>
          <input v-model="password" type="password" placeholder="Ingresa tu contraseña" class="form-control">
          <small v-if="errors.password" class="text-danger">{{ errors.password }}</small>
        </div>
        <button type="submit" class="btn btn-primary w-100">Ingresar</button>
      </form>
    </div>
  </div>
</template>

<script>
import axios from 'axios';
const axiosInstance = axios.create({
  baseURL: 'http://127.0.0.1:8000/api/',
  headers: {
    'Authorization': 'Token dcf9db5025fd0d9487a994d1a62b76abb5445970'
  }
});
    export default{
        name: 'Login',
        data(){
            return{
                email:'',
                password:'',
                errors:{
                    email:'',
                    password:'',
                    wrong_credentials:''
                }
            }
        },
        computed:{
            
        },
        methods:{
            isValidForm(){
                let valid=true;
                if(!this.email){
                    this.errors.email = 'El campo nop puede ser blanco'
                }else{
                    this.errors.email = "";
                }
                if(!this.password){
                    this.errors.password = 'El campo no puede estar en blanco'
                }else{
                    this.errors.password = '';
                }
                if(this.errors.email || this.errors.password){
                    valid = false;
                }
                return valid;
            },
            submitForm(){
                if(this.isValidForm()){
                    axiosInstance.post('login/',{email:this.email, password:this.password}, {withCredentials:true})
                    .then(response => {
                        console.log(response.data.user);
                        console.log(response.data.token); 
                        const user = response.data.user;
                        const token = response.data.token;
                        
                        if (user && user.id && token) {
                        this.$store.commit('setToken', { token, user_id: user.id, username: user.username});
                        this.$router.push('/');
                        } else {
                        console.error("User ID or token is missing in the response.");
                        }
                    })
                    .catch(error => {
                        console.log(error);
                    })
                }

            }
            
        }
    }
</script>

<style>
body {
  background: linear-gradient(90deg, rgba(2,0,36,1) 0%, #246df5 100%);
  font-family: 'Poppins', sans-serif;
}
</style>
