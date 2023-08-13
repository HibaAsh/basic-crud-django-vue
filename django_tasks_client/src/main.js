import { createApp, } from 'vue'
import App from './App.vue'
import axios from 'axios'
// import axios
// import axios from 'axios'
// import Vue from 'vue'

const app = createApp(App)
// app.use(axios, {
//     baseUrl: 'https://localhost.com/',
// })
app.config.globalProperties.$http = axios;
app.mount("#app")

