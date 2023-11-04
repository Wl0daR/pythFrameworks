<template>
    <div>
      <h2>Dodaj Nowy Samochód</h2>
      <form @submit="addCar">
        <label>Marka:</label>
        <input v-model="newCar.brand" required>
        <label>Model:</label>
        <input v-model="newCar.model" required>
        <label>Rok produkcji:</label>
        <input v-model="newCar.year" type="number" required>
        <label>Pojemność silnika (cm³):</label>
        <input v-model="newCar.engineCapacity" type="number" required>
        <label>Rodzaj silnika:</label>
        <select v-model="newCar.engineType" required>
          <option value="benzyna">Benzyna</option>
          <option value="diesel">Diesel</option>
          <option value="hybryda">Hybryda</option>
          <option value="elektryczny">Elektryczny</option>
        </select>
        <label>Skrzynia biegów:</label>
        <select v-model="newCar.gear" required>
          <option value="manualny">Manualny</option>
          <option value="automatyczny">Automatyczny</option>
        </select>
        <label>Napęd:</label>
        <select v-model="newCar.drive_train" required>
          <option value="przednionapęd">Przedni napęd</option>
          <option value="tylnionapęd">Tylni napęd</option>
          <option value="napęd4x4">Napęd 4x4</option>
        </select>
        <label>Liczba drzwi:</label>
        <input v-model="newCar.doors" type="number" required>
  
        <button type="submit" @click="addCar">Dodaj Samochód</button>
      </form>
    </div>
  </template>
  
  <script>
  import axios from 'axios';
  
  export default {
    data() {
      return {
        newCar: {
          brand: "",
          model: "",
          year: 2023,
          engineCapacity: 1500,
          engineType: "benzyna",
          gear: "manualny",
          drive_train: "przednionapęd",
          doors: 4
        }
      };
    },
    methods: {
      addCar() {
        axios
          .post('/api/cars/', this.newCar)
          .catch(error => {
            console.error('Błąd podczas dodawania samochodu:', error);
          });
      }
    }
  };
  </script>
  