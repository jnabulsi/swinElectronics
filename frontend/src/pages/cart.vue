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
        <ProductList :products="products" :show-remove-from-cart-button="true" @button-click="handleRemoveFromCart" />
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
import { useRouter } from 'vue-router'
import ProductList from '@/components/ProductList.vue'

import { getCart, removeFromCart } from '@/api/cart'
import { getProductById } from '@/api/products'

const router = useRouter()
const products = ref([])

const getImagePath = (filename) =>
  new URL(`../assets/${filename}`, import.meta.url).href

onMounted(async () => {
  const cartRes = await getCart()
  const enriched = []

  for (const item of cartRes.data) {
    const productRes = await getProductById(item.productId)
    enriched.push({
      ...productRes.data,
      quantity: item.quantity,
      image: getImagePath(productRes.data.image)
    })
  }

  products.value = enriched
})

const handleRemoveFromCart = async (product) => {
  await removeFromCart(product.id)
  products.value = products.value.filter(p => p.id !== product.id)
}

const goToCheckout = () => {
  router.push('/checkout')
}
</script>
