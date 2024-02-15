<template>
<button type="button" class="btn btn-primary" data-bs-toggle="modal" data-bs-target="#exampleModal" @click="GetUserProducts()">
  Cart
</button>

<div class="modal fade" id="exampleModal" tabindex="-1" aria-labelledby="exampleModalLabel" aria-hidden="true">
  <div class="modal-dialog modal-lg">
    <div class="modal-content">
      <div class="modal-header">
        <h1 class="modal-title fs-5" id="exampleModalLabel">Cart</h1>
        <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
      </div>
      <div class="modal-body">
        <ul class="list-group" v-for="(product, index) in products">
            <li class="list-group-item" style="display: flex; justify-content: space-around;">
                    <h4>{{ product['product']['name'] }}</h4>
                    <h5 class="mt-1">{{ product['product']['formattedAmount'] }}</h5>
                    <button class="btn btn-danger" @click="DeleteProduct(product['id'], index)">Delete</button>    
            </li>
        </ul>

      </div>
      <div class="modal-footer">
        <button type="button" class="btn btn-secondary" data-bs-dismiss="modal">Close</button>
      </div>
    </div>
  </div>
</div>

</template>

<script>
import axios from 'axios';
import VueCookies from 'vue-cookies'

export default {
  data() {
    return {
      showElement: false,
      token: VueCookies.get("token"),
      products: []
    }
  },

  methods: {
    GetUserProducts(){
        axios.post(`/cart/get_user_products`, {"action" : "dashboard"}, {headers: {Authorization: 'Bearer ' + this.token}}) 
                .then((res) => {
                    this.products = res.data
                })
                .catch((error) => {
                        console.error(error);
                })

    },
    DeleteProduct(id, product){
      this.products.splice(product, 1);
      axios.delete(`/cart/delete_user_product?id=${id}`, {headers: {Authorization: 'Bearer ' + this.token}}) 
                .then((res) => {
                    console.log("Товар удален")
                })
                .catch((error) => {
                        console.error(error);
      })
    }
  },
}
</script>