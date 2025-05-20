<template>
  <v-container class="py-6">
    <!-- Page Title -->
    <v-row justify="center" class="mb-4">
      <v-col cols="12" md="8" class="text-center">
        <h1 class="text-h4">Sales Data</h1>
      </v-col>
    </v-row>

    <!-- Sales List -->
    <v-row justify="center">
      <v-col cols="12" md="6">
        <v-list two-line>
          <v-list-item v-for="item in sales" :key="item.id">
            <v-list-item-content>
              <v-list-item-title>{{ item.title }}</v-list-item-title>
              <v-list-item-subtitle>
                {{ item.quantity }} sold – ${{ (item.quantity * item.price).toFixed(2) }} </v-list-item-subtitle>
            </v-list-item-content>
          </v-list-item>
        </v-list>
      </v-col>
    </v-row>

    <!-- Totals -->
    <v-row justify="center" class="mt-4">
      <v-col cols="12" md="6" class="text-right">
        <div><strong>Total Items Sold:</strong> {{ totalQuantity }}</div>
        <div><strong>Total Sales Value:</strong> ${{ totalValue }}</div>
      </v-col>
    </v-row>
  </v-container>
</template>

<script setup>
import { ref, onMounted } from 'vue'
import salesData from '@/data/sales.json'

const sales = ref([])
const totalQuantity = ref(0)
const totalValue = ref(0)

onMounted(() => {
  sales.value = salesData

  totalQuantity.value = sales.value.reduce((sum, item) => sum + item.quantity, 0)
  totalValue.value = sales.value.reduce((sum, item) => sum + item.quantity * item.price, 0).toFixed(2)
})
</script>
