
import { createApp } from 'vue'
import Vuelidate from 'vuelidate'
import VueCookies from 'vue-cookies'
import App from './App.vue'
import router from './router'
import axios from 'axios';

const app = createApp(App)

axios.defaults.withCredentials = true;
axios.defaults.baseURL = 'http://127.0.0.1:8000/';
app.use(VueCookies)
app.use(Vuelidate)
app.use(router)

app.mount('#app')
