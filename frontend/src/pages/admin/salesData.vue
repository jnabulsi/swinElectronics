<template>
  <v-container class="py-6">
    <!-- Page Title -->
    <v-row justify="center" class="mb-4">
      <v-col cols="12" md="8" class="text-center">
        <h1 class="text-h4">Sales Data</h1>
      </v-col>
    </v-row>

    <!-- Date filters -->
    <v-row justify="center" class="mb-4">
      <v-col cols="12" md="6" class="d-flex justify-space-between align-center">
        <v-select :items="months" item-title="name" item-value="value" label="Month" v-model="selectedMonth"
          density="compact" style="max-width: 48%" />
        <v-select :items="years" item-title="title" item-value="value" label="Year" v-model="selectedYear"
          density="compact" style="max-width: 48%" />
      </v-col>
    </v-row>

    <!-- Sales List Wrapped in a Card -->
    <v-row justify="center">
      <v-col cols="12" md="6">
        <v-card elevation="2" class="pa-4">
          <v-card-title class="text-h6">Sales Summary</v-card-title>
          <v-divider class="mb-2" />

          <v-list>
            <v-list-item v-if="sales.length === 0">
              <v-list-item-title>No sales found for selected period.</v-list-item-title>
            </v-list-item>

            <v-list-item v-for="(item, index) in sales" :key="item.product_name"
              :class="{ 'border-b': index !== sales.length - 1 }" v-else>
              <v-list-item-title>{{ item.product_name }}</v-list-item-title>
              <v-list-item-subtitle>
                {{ item.quantity }} sold – ${{ item.total_price.toFixed(2) }}
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
import { ref, watch, onMounted } from 'vue'
import { getSalesData } from '@/api/sales'

const salesRaw = ref([])
const sales = ref([])
const totalQuantity = ref(0)
const totalValue = ref(0)

// Filtering
const selectedMonth = ref(0)  // All months
const selectedYear = ref(0)   // All years


const months = [
  { name: 'All', value: 0 },
  { name: 'January', value: 1 },
  { name: 'February', value: 2 },
  { name: 'March', value: 3 },
  { name: 'April', value: 4 },
  { name: 'May', value: 5 },
  { name: 'June', value: 6 },
  { name: 'July', value: 7 },
  { name: 'August', value: 8 },
  { name: 'September', value: 9 },
  { name: 'October', value: 10 },
  { name: 'November', value: 11 },
  { name: 'December', value: 12 }
]

const years = ref([])

function applyFilter() {
  const filtered = salesRaw.value.filter((item) => {
    const date = new Date(item.date)
    const matchesMonth = selectedMonth.value === 0 || (date.getMonth() + 1 === selectedMonth.value)
    const matchesYear = selectedYear.value === 0 || (date.getFullYear() === selectedYear.value)
    return matchesMonth && matchesYear
  })

  const grouped = {}
  filtered.forEach(item => {
    if (!grouped[item.product_name]) {
      grouped[item.product_name] = {
        product_name: item.product_name,
        quantity: 0,
        total_price: 0
      }
    }
    const price = item.price ?? 0
    grouped[item.product_name].quantity += item.quantity
    grouped[item.product_name].total_price += item.quantity * price
  })

  sales.value = Object.values(grouped)
  totalQuantity.value = sales.value.reduce((sum, item) => sum + item.quantity, 0)
  totalValue.value = sales.value.reduce((sum, item) => sum + item.total_price, 0).toFixed(2)
}

onMounted(async () => {
  const res = await getSalesData()
  salesRaw.value = res.data

  // Extract unique years from data and format
  const yearSet = new Set(res.data.map(item => new Date(item.date).getFullYear()))
  years.value = [
    { title: 'All', value: 0 },
    ...Array.from(yearSet)
      .sort((a, b) => b - a)
      .map(y => ({ title: y.toString(), value: y }))
  ]

  applyFilter()
})

watch([selectedMonth, selectedYear], applyFilter)
</script>
