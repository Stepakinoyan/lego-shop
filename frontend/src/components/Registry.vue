<template>
  <div class="container d-flex justify-content-center align-items-center" style="height: 100vh;">
    <form class="d-flex flex-column w-100" @submit.prevent="RegisterUser">
    <h1 class="h3 mb-3 fw-normal">Sign up</h1>

    <div class="form-floating">
      <input type="email" class="form-control" id="floatingInput" placeholder="name@example.com" v-model="email">
      <label for="floatingInput">Email address</label>
    <div data-lastpass-icon-root="true"></div></div>
    <div class="form-floating">
      <input type="password" class="form-control" id="floatingPassword" placeholder="Password" v-model="password">
      <label for="floatingPassword">Password</label>
        <div data-lastpass-icon-root="true" ></div>
    </div>

    <button class="btn btn-primary w-100 py-2" type="submit">Sign up</button>
  </form>
  </div>

</template>


<script>
import axios from 'axios';


  export default {
    data(){
      return {
            email: "",
            password: ""          
      }
    },
    methods: {
      RegisterUser(e) {
        e.preventDefault()

        let data = {
            email: this.email,
            password: this.password,
            is_active: true,
            is_superuser: false,
            is_verified: false
        }

        axios.post(`/auth/register`, data) 
                .then((res) => {
                    this.$router.push('login')
                })
                .catch((error) => {
                        console.error(error);
                });
      }

      
    }
  }

</script>