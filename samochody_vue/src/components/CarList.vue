<template>
    <div>
      <h2>Lista Samochodów</h2>
      <ul>
        <li v-for="car in cars" :key="car.id">{{ car.brand }} - {{ car.model }}</li>
      </ul>
    </div>
  </template>
  
  <script>

  
  export default {
    data() {
      return {
        cars: []
      };
    },
    mounted() {
    this.$http.get('/api/cars/')
        .then(response => {
            this.cars = response.data;
        })
        .catch(error => {
            console.error(error);
        });
    }
  };
  </script>
  