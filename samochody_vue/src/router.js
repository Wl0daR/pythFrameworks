import Vue from 'vue';
import VueRouter from 'vue-router';
import CarList from './components/CarList.vue';
import AddCar from './components/AddCar.vue';

Vue.use(VueRouter);

const routes = [
  { path: '/', component: CarList },
  { path: '/add-car', component: AddCar }
];

const router = new VueRouter({
  routes,
});

export default router;
