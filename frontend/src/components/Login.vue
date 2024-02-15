<template>
    <div class="container d-flex justify-content-center align-items-center" style="height: 100vh;">
      <form class="d-flex flex-column w-100" @submit.prevent="LoginUser">
      <h1 class="h3 mb-3 fw-normal">Login</h1>
  
      <div class="form-floating">
        <input type="email" class="form-control" id="floatingInput" placeholder="name@example.com" v-model="username">
        <label for="floatingInput">Email address</label>
      <div data-lastpass-icon-root="true"></div></div>
      <div class="form-floating">
        <input type="password" class="form-control" id="floatingPassword" placeholder="Password" v-model="password">
        <label for="floatingPassword">Password</label>
          <div data-lastpass-icon-root="true" ></div>
      </div>
  
      <button class="btn btn-primary w-100 py-2" type="submit">Login</button>
    </form>
    </div>
  
  </template>
  
<!-- <script src="https://unpkg.com/vue-cookies@1.8.3/vue-cookies.js"></script> -->
<script>
  import axios from 'axios';
  import VueCookies from 'vue-cookies'
  
    export default {
      data(){
        return {
              username: "",
              password: ""          
        }
      },
      methods: {
        LoginUser(e) {
          e.preventDefault()

          const data = new URLSearchParams();
  
          data.append("username", this.username)
          data.append("password", this.password)
  
          axios.post(`/auth/jwt/login`, data) 
                  .then((res) => {
                          let token = res["data"]["access_token"]
                          // document.cookie = `token=${token}; expires=3600`;
                          localStorage.setItem('token', token);
                          VueCookies.set('token', token, 3600)
                          this.$router.push('/')
                  })
                  .catch((error) => {
                          console.error(error);
                  });
        }
  
        
      }
    }
  
  </script>