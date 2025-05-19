<template>
  <v-container class="d-flex justify-center">
    <v-container class="py-8" style="max-height: 80vh; overflow-y: auto;" max-width="600">
      <v-card v-for="product in products" :key="product.id" class="mb-4">
        <v-img :src="product.image" height="200px" />

        <v-card-title class="text-h6">
          {{ product.title }}
        </v-card-title>

        <v-card-subtitle class="text-subtitle-1">
          ${{ product.price.toFixed(2) }}
        </v-card-subtitle>

        <v-card-text>
          {{ product.description }}
        </v-card-text>

        <v-card-actions>
          <v-btn color="primary" block>Add to Cart</v-btn>
        </v-card-actions>
      </v-card>
    </v-container>
  </v-container>
</template>

<script setup>
import { ref, onMounted } from 'vue'
import productsData from '@/data/products.json'


const products = ref([])

const getImagePath = (filename) => {
  return new URL(`../assets/${filename}`, import.meta.url).href
}

onMounted(() => {
  products.value = productsData.map((product) => ({
    ...product,
    image: getImagePath(product.image),
  }))
})
</script>
