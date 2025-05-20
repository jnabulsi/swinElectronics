<template>
  <v-container class="py-6">
    <!-- Page Title -->
    <v-row justify="center" class="mb-4">
      <v-col cols="12" md="8" class="text-center">
        <h1 class="text-h4">Browse Products</h1>
      </v-col>
    </v-row>

    <!-- Search + Filters -->
    <v-row justify="center" class="mb-4">
      <v-col cols="12" md="4">
        <v-text-field v-model="searchQuery" label="Search Products" prepend-inner-icon="mdi-magnify" clearable />
      </v-col>
      <v-col cols="12" md="4">
        <v-select v-model="selectedCategory" :items="categories" label="Filter by Category" clearable />
      </v-col>
    </v-row>

    <!-- Product List -->
    <v-row justify="center">
      <v-col cols="12" md="8">
        <ProductList :products="filteredProducts" :showAddToCartButton="true" @button-click="handleAddToCart" />
      </v-col>
    </v-row>
  </v-container>
</template>

<script setup>
import { ref, computed, onMounted } from 'vue'
// TODO: Replace fake data in products.json with data from api
import productsData from '@/data/products.json'
import ProductList from '@/components/ProductList.vue'

const products = ref([])
const searchQuery = ref('')
const selectedCategory = ref(null)
const categories = ref([])


const getImagePath = (filename) => {
  return new URL(`../assets/${filename}`, import.meta.url).href
}

onMounted(() => {
  products.value = productsData.map((product) => ({
    ...product,
    image: getImagePath(product.image),
  }))

  const uniqueCategories = [...new Set(products.value.map(p => p.category))]
  categories.value = uniqueCategories
})

const filteredProducts = computed(() => {
  return products.value.filter((p) => {
    const matchesSearch = p.title.toLowerCase().includes(searchQuery.value.toLowerCase())
    const matchesCategory = !selectedCategory.value || p.category === selectedCategory.value
    return matchesSearch && matchesCategory
  })
})

const handleAddToCart = (product) => {
  console.log('Add to cart:', product)
  // TODO: Add to cart logic
}
</script>
