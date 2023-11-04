import { createApp } from 'vue'
import App from './App.vue'
import axios from 'axios';
import Vue from 'vue';
import router from './router';

Vue.prototype.$http = axios;
createApp(App).mount('#app')
new Vue({
    render: h => h(App),
    router 
  }).$mount('#app');
