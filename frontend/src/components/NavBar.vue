<script setup>
import Carticon from '../components/icons/Carticon.vue'
import Settings from '../components/Settings.vue'
import GithubIcon from '../components/icons/GithubIcon.vue'
import Modal from '../components/Modal.vue'
import { RouterLink } from 'vue-router'
</script>

<!-- <SettingsIcon/> -->
<template>
      <nav class="navbar navbar-expand-lg bg-body-tertiary">
        <div class="container-fluid">
          <a class="navbar-brand" href="#">
            <a href="https://github.com/Stepakinoyan" class="profile" target="_blank"><GithubIcon/></a>
          </a>
          <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarTogglerDemo02" aria-controls="navbarTogglerDemo02" aria-expanded="false" aria-label="Toggle navigation">
            <span class="navbar-toggler-icon"></span>
          </button>
          <div class="collapse navbar-collapse" id="navbarTogglerDemo02">
            <ul class="navbar-nav ms-auto mb-2 mb-lg-0">
              <li class="nav-item" v-if="token" v-show="true">
                <div class="d-flex">
                  <a class="nav-link m-1"><Modal/></a>
                  <a class="nav-link m-1"><Settings/></a>
                </div>
                
              </li>
              <li v-if="token == undefined" v-show="true"> 
                <form class="d-flex mt-1" role="search">
                  <RouterLink to="/login" class="btn btn-outline-success">Login</RouterLink>
                  <RouterLink to="/signup" class="btn btn-outline-success">Sign up</RouterLink>  
                </form>
              </li>
            </ul>
          </div>
        </div>
      </nav>
</template>

<script>
import VueCookies from 'vue-cookies'

export default {
  data(){
    return {
      token: VueCookies.get('token'),
    }
  }
}

</script>