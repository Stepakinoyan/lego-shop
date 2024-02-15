<template>

<div class="btn-group dropstart">
  <button type="button" class="btn btn-primary dropdown-toggle" data-bs-toggle="dropdown" aria-expanded="false">
    Settings
  </button>
  <ul class="dropdown-menu">
    <li class="dropdown-item text-danger" @click="SignOut">Sign out</li>
  </ul>
</div>


</template>



<script>
import VueCookies from 'vue-cookies'
export default{
    computed: {
        SignOut(){
          VueCookies.remove('token')
          location.reload()
        }
    }
}

</script>