<template>
    <div class="container mt-5">
            <div class="row">
                    <div class="d-flex">
                            <input class="form-control" v-model="q"/>
                            <button class="btn btn-primary" @click="GetDataSearch(q)">Search</button>
                    </div>
                    <div class="row row-cols-1 row-cols-md-3 g-4 mx-auto">
                      <div class="col" v-for="item in data">
                              <div class="card h-100">
                                <img :src="item['listingImages'][0]['url']" class="card-img-top border" alt="...">
                                <div class="card-body">
                                  <h5 class="card-title">{{ item['name'] }}</h5>
  
                                  <p class="card-text">Discover the full list of the LEGO sets released in the last 2 months</p>
                                  <div class="row">
                                        <div class="col border text-center">
                                                <h5 class="card-text mt-1">{{ item['rating'] }}</h5>
                                                <h5>Stars</h5>
                                        </div>          
                                        <div class="col border text-center">
                                                <h5 class="card-text mt-1">{{ item['ageRange'] }}</h5>
                                                <h5>Age</h5>
                                        </div>    
                                        <div class="col border text-center">
                                                <h5 class="card-text mt-1">{{ item['pieceCount'] }}</h5>
                                                <h5>Pieces</h5>
                                        </div>                           
                                  </div>

                                  <!-- <p class="card-text">Discover the full list of the LEGO sets released in the last 2 months</p> -->
                                  <button class="btn btn-primary m-1" :disabled="isDisabled" @click="AddToCart(item['id'])">Add to cart</button>
                                </div>
                              </div>
                      </div>
    
                    </div>

            </div>
    </div>

</template>



<script>
import axios from 'axios';
import VueCookies from 'vue-cookies'
  export default {
    data(){
      return {
         q: "",
         data: this.GetDataSearch(),
         token: VueCookies.get("token"),
      }
    },
    methods: {
        GetDataSearch(q = ""){
                axios.post(`/lego/products/search?q=${q}`)
                .then((res) => {
                        this.data = res.data
                })
                .catch((error) => {
                        console.error(error);
                });
        },
        AddToCart(id){
                
                axios.post(`/cart/add_to_cart?id=${id}`, {"action" : "dashboard"}, {headers: {Authorization: 'Bearer ' + this.token}})
   
                .then((res) => {
                        console.log(res.data)
                })
                .catch((error) => {
                        console.error(error);
                });
        },
     },
     computed: {
                isDisabled() {
                        if (this.token) {
                                return false
                        }else{
                                return true
                        }
                }
        }
        
    
    
  }

</script>

<style>
.card-img-top {
    height: 15vw;
    object-fit: contain;
}



</style>