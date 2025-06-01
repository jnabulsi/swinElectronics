<template>
  <v-app-bar app color="primary" dark>
    <!-- Logo / Home link -->
     <div class="d-flex align-center">
        <v-toolbar-title @click="goHome" class="cursor-pointer">
          SwinElectronic
        </v-toolbar-title>

        <template v-if="app.isLoggedIn && app.user">  
          <span class="ml-3" style="color: #BBDEFB; font-weight: bold; font-size: 1rem;">
            Hello, {{ app.user.name }}
          </span> 
        </template>
      </div>
    <v-spacer />
    
    <v-btn text to="/">Products</v-btn>
    <!-- User options (if logged in) -->
    <template v-if="app.isLoggedIn">
      <v-btn text to="/orders">Order History</v-btn>
      <v-btn text to="/cart">Shopping Cart</v-btn>

      <!-- Admin options -->
      <template v-if="app.isAdmin">
        <v-btn text to="/admin/addProduct">Add Product</v-btn>
        <v-btn text to="/admin/salesData">Sales Data</v-btn>
        <v-btn text to="/admin/editProducts">Edit Products</v-btn>
        <v-btn text @click="app.logout">Admin Logout</v-btn>
      </template>

      <template v-if="!app.isAdmin">
        <v-btn text @click="logOut">Logout</v-btn>
      </template>
    </template>

    <!-- Guest options (if not logged in) -->
    <template v-else>
      <v-btn text to="/login">Login</v-btn>
      <v-btn text to="/signup">Sign Up</v-btn>
    </template>
  </v-app-bar>
</template>

<script setup>
import { useRouter } from 'vue-router'
import { useAppStore } from '@/stores/app'

const router = useRouter()
const app = useAppStore()

const goHome = () => {
  router.push('/')
}

const logOut = () => {
  app.logout()
  router.push('/')
}

</script>

<style scoped>
.cursor-pointer {
  cursor: pointer;
}
</style>
