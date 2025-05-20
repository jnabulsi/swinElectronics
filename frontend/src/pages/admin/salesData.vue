<template>
  <v-container class="py-6">
    <!-- Page Title -->
    <v-row justify="center" class="mb-4">
      <v-col cols="12" md="8" class="text-center">
        <h1 class="text-h4">Sales Data</h1>
      </v-col>
    </v-row>
    <!-- Sales List Wrapped in a Card -->
    <v-row justify="center">
      <v-col cols="12" md="6">
        <v-card elevation="2" class="pa-4">
          <v-card-title class="text-h6">Sales Summary</v-card-title>
          <v-divider class="mb-2" />

          <v-list>
            <v-list-item v-for="(item, index) in sales" :key="item.id"
              :class="{ 'border-b': index !== sales.length - 1 }">
              <v-list-item-title>{{ item.title }}</v-list-item-title>
              <v-list-item-subtitle>
                {{ item.quantity }} sold – ${{ (item.quantity * item.price).toFixed(2) }}
              </v-list-item-subtitle>
            </v-list-item>
          </v-list>

          <v-divider class="my-4" />

          <div class="text-right">
            <div><strong>Total Items Sold:</strong> {{ totalQuantity }}</div>
            <div><strong>Total Sales Value:</strong> ${{ totalValue }}</div>
          </div>
        </v-card>
      </v-col>
    </v-row>
  </v-container>
</template>

<script setup>
import { ref, onMounted } from 'vue'
import { getSalesData } from '@/api/sales'

const sales = ref([])
const totalQuantity = ref(0)
const totalValue = ref(0)

onMounted(async () => {
  const res = await getSalesData()
  sales.value = res.data

  totalQuantity.value = sales.value.reduce((sum, item) => sum + item.quantity, 0)
  totalValue.value = sales.value.reduce((sum, item) => sum + item.quantity * item.price, 0).toFixed(2)
})
</script>
