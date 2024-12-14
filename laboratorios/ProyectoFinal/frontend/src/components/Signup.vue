<template>
    <div class="container-fluid d-flex justify-content-center align-items-center mt-5 mb-5">
    <div class="bg-white p-4 rounded shadow" style="max-width: 100%; width: 100%; max-width: 400px;">
      <form @submit.prevent="submitForm" class="mx-auto">
        <h4 class="text-center mb-4">Register</h4>
        <div class="mb-3">
          <label for="username" class="form-label">Usuario</label>
          <input v-model="username" id="username" type="text" placeholder="Ingresa tu nombre de usuario" class="form-control">
          <small v-if="errors.username" class="text-danger">{{ errors.username }}</small>
        </div>
        <div class="mb-3">
          <label for="password" class="form-label">Ingresa Contraseña</label>
          <input v-model="password" id="password" type="password" placeholder="Ingresa tu contraseña" class="form-control">
          <small v-if="errors.password" class="text-danger">{{ errors.password }}</small>
        </div>
        <div class="mb-3">
          <label for="password2" class="form-label">Repite tu contraseña</label>
          <input v-model="password2" id="password2" type="password" placeholder="Repite tu contraseña" class="form-control">
          <small v-if="errors.password2" class="text-danger">{{ errors.password2 }}</small>
        </div>
        <div class="mb-3">
          <label for="email" class="form-label">Email</label>
          <input v-model="email" id="email" type="email" placeholder="Ingresa tu email" class="form-control">
          <small v-if="errors.email" class="text-danger">{{ errors.email }}</small>
        </div>
        <div class="mb-3">
          <label for="first_name" class="form-label">Nombres</label>
          <input v-model="first_name" id="first_name" type="text" placeholder="Ingresa tu nombre" class="form-control">
          <small v-if="errors.first_name" class="text-danger">{{ errors.first_name }}</small>
        </div>
        <div class="mb-3">
          <label for="last_name" class="form-label">Apellidos</label>
          <input v-model="last_name" id="last_name" type="text" placeholder="Ingresa tu apellido" class="form-control">
          <small v-if="errors.last_name" class="text-danger">{{ errors.last_name }}</small>
        </div>
        <div class="mb-3">
          <label for="dni" class="form-label">DNI</label>
          <input v-model="dni" id="dni" type="text" placeholder="Ingresa tu DNI" class="form-control">
          <small v-if="errors.dni" class="text-danger">{{ errors.dni }}</small>
        </div>
        <div class="mb-3">
          <label for="direccion" class="form-label">Direccion</label>
          <input v-model="direccion" id="direccion" type="text" placeholder="Ingresa tu direccion" class="form-control">
          <small v-if="errors.direccion" class="text-danger">{{ errors.direccion }}</small>
        </div>
        <div class="mb-3">
          <label for="telefono" class="form-label">Telefono</label>
          <input v-model="telefono" id="telefono" type="text" placeholder="Ingresa tu telefono" class="form-control">
          <small v-if="errors.telefono" class="text-danger">{{ errors.telefono }}</small>
        </div>
        <button type="submit" class="btn btn-primary w-100">Signup to the system</button>
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
        name:'Signup',
        data(){
            return{
                username:'',
                password:'',
                password2:'',
                email:'',
                first_name:'',
                last_name:'',
                dni:'',
                direccion:'',
                telefono:'',
                errors:{
                    email:'',
                    password:'',
                    password2:'',
                    email:'',
                    first_name:'',
                    last_name:'',
                    dni:'',
                    direccion:'',
                    telefono:'',
                    wrong_credentials:''
                }
            }
        },
        computed:{

        },
        methods:{
            isValidForm(){
                let valid=true;
                if(!this.username){this.errors.username = 'El campo no puede estar vacio'}
                else{this.errors.username = '';}

                if(!this.password){this.errors.password = 'El campo no puede estar en blanco'}
                else{this.errors.password = '';}

                if(this.password && this.password2 && this.password != this.password2)
                {this.errors.password2 = 'Password incorrecto';}
                else{this.errors.password2 = '';}

                if(!this.email){this.errors.email = 'El campo no puede estar en blanco'}
                else{this.errors.email = "";}

                if(!this.first_name){this.errors.first_name = 'El campo no puede estar vacio'}
                else{this.errors.first_name = ''}

                if(!this.last_name){this.errors.last_name = 'El campo no puede estar vacio'}
                else{this.errors.last_name = ''}

                if(!this.dni){this.errors.dni = 'El campo no puede estar vacio'}
                else{this.errors.dni = ''}

                //if(!this.telefono){this.errors.telefono = 'El campo no puede estar vacio'}
                //else{this.errors.telefono = ''}

                if(this.errors.username || this.errors.password || this.errors.password2 || this.errors.email ||
                    this.errors.first_name || this.errors.last_name || this.errors.dni || this.errors.telefono){valid = false;}

                return valid;
            },
            submitForm(){
                if(this.isValidForm){
                    axiosInstance.post('usuarios/',{
                        username:this.username, 
                        password:this.password, 
                        email:this.email, 
                        first_name:this.first_name, 
                        last_name:this.last_name, 
                        dni:this.dni, 
                        direccion:this.direccion, 
                        telefono:this.telefono
                    })
                    .then(response =>{
                        console.log(response.data.user);
                        this.username = '';
                        this.password = '';
                        this.password2 = '';
                        this.email = '';
                        this.first_name = '';
                        this.last_name = '';
                        this.dni = '';
                        this.direccion = '';
                        this.telefono = '';
                    })
                    .catch(error => {
                        console.log(error.response.data);
                        if(error.response.data.username){
                            this.errors.username = error.response.data.username.join('');
                        }
                        else{
                            this.errors.username = "";
                        }
                    })
                }

            }
            
        }
    }
</script>

<style>

</style>
