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
import ProductList from '@/components/ProductList.vue'

// Import API functions
import { getProducts } from '@/api/products'
import { addToCart } from '@/api/cart'

const products = ref([])
const searchQuery = ref('')
const selectedCategory = ref(null)
const categories = ref([])

const getImagePath = (filename) => {
  return new URL(`../assets/${filename}`, import.meta.url).href
}

onMounted(async () => {
  try {
    const res = await getProducts()
    products.value = res.data.map((product) => ({
      ...product,
      image: getImagePath(product.image)
    }))

    const uniqueCategories = [...new Set(products.value.map(p => p.category))]
    categories.value = uniqueCategories
  } catch (error) {
    console.error('Failed to load products:', error)
  }
})

const filteredProducts = computed(() => {
  return products.value.filter((p) => {
    const matchesSearch = p.title.toLowerCase().includes(searchQuery.value.toLowerCase())
    const matchesCategory = !selectedCategory.value || p.category === selectedCategory.value
    return matchesSearch && matchesCategory
  })
})

const handleAddToCart = async (product) => {
  try {
    await addToCart({
      productId: product.id,
    })
    console.log('Added to cart:', product.title)
  } catch (error) {
    console.error('Failed to add to cart:', error)
    alert('Could not add item to cart.')
  }
}
</script>
