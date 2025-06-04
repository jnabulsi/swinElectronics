<template>
  <v-container class="py-6">
    <!-- Page Title -->
    <v-row justify="center" class="mb-4">
      <v-col cols="12" md="8" class="text-center">
        <h1 class="text-h4">Order History</h1>
      </v-col>
    </v-row>

    <!-- Orders List -->
    <v-row justify="center">
      <v-col cols="12" md="8">
        <ProductList :products="products" :show-order-date="true" />
      </v-col>
    </v-row>
  </v-container>
</template>
<script setup>
import { ref, onMounted } from 'vue'
import ProductList from '@/components/ProductList.vue'
import { getOrders } from '@/api/orders'

const products = ref([])

onMounted(async () => {
  const res = await getOrders()
  products.value = res.data
})
</script>
