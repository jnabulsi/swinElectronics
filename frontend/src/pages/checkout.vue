<template>
  <v-container class="py-6">
    <!-- Page Title -->
    <v-row justify="center" class="mb-4">
      <v-col cols="12" md="8" class="text-center">
        <h1 class="text-h4">Checkout</h1>
      </v-col>
    </v-row>

    <!-- Item Titles -->
    <v-row justify="center">
      <v-col cols="12" md="6">
        <v-list two-line>
          <v-list-item v-for="product in cartData" :key="product.id">
            <v-list-item-title>{{ product.title }}</v-list-item-title>
            <v-list-item-subtitle>${{ product.price.toFixed(2) }}</v-list-item-subtitle>
          </v-list-item>
        </v-list>
      </v-col>
    </v-row>
    <!-- Total Price -->
    <v-row justify="center" class="mt-4">
      <v-col cols="12" md="4" class="text-right">
        <strong>Total:</strong> ${{ total }}
      </v-col>
    </v-row>

    <!-- Purchase Button -->
    <v-row justify="center" class="mt-6">
      <v-col cols="12" md="4" class="text-center">
        <v-btn color="primary" size="large" block @click="purchase">
          Complete Purchase
        </v-btn>
      </v-col>
    </v-row>
  </v-container>
</template>

<script setup>
import { ref, onMounted } from 'vue'
// TODO: Replace fake data in cart.json with data from api
import cartData from '@/data/cart.json'

const total = ref(0)

onMounted(() => {
  total.value = cartData.reduce((sum, item) => sum + item.price, 0).toFixed(2)
})

const purchase = () => {
  console.log('Purchase submitted:', cartItems.value)
  // TODO: Hook up real purchase logic or confirmation
}
</script>
