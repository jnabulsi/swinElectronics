<template>
  <v-container class="py-6">
    <!-- Page Title -->
    <v-row justify="center" class="mb-4">
      <v-col cols="12" md="8" class="text-center">
        <h1 class="text-h4">Shopping Cart</h1>
      </v-col>
    </v-row>

    <!-- Cart Items -->
    <v-row justify="center">
      <v-col cols="12" md="8">
        <ProductList :products="products" show-remove-from-cart-button="true" @button-click="handleRemoveFromCart" />
      </v-col>
    </v-row>

    <!-- Checkout Button -->
    <v-row justify="center" class="mt-6">
      <v-col cols="12" md="4" class="text-center">
        <v-btn color="primary" size="large" block @click="goToCheckout">
          Go to Checkout
        </v-btn>
      </v-col>
    </v-row>
  </v-container>
</template>

<script setup>
import { ref, onMounted } from 'vue'
// TODO: Replace fake data in cart.json with data from api
import productsData from '@/data/cart.json'
import ProductList from '@/components/ProductList.vue'
import { useRouter } from 'vue-router'

const router = useRouter()
const products = ref([])

const getImagePath = (filename) =>
  new URL(`../assets/${filename}`, import.meta.url).href

onMounted(() => {
  products.value = productsData.map((product) => ({
    ...product,
    image: getImagePath(product.image),
  }))
})

const handleRemoveFromCart = (product) => {
  console.log('Remove from cart:', product)
  // TODO: Remove logic
}

const goToCheckout = () => {
  router.push('/checkout')
}
</script>
