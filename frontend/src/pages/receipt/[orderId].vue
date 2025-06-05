<template>
  <v-container class="py-6">
    <v-row justify="center">
      <v-col cols="12" md="6">
        <v-card class="pa-4" elevation="2">
          <v-card-title class="text-h5">Payment Completed</v-card-title>
          <v-divider class="my-2" />

          <v-list>
            <v-list-item v-for="item in order?.items || []" :key="item.productId">
              <v-list-item-title>
                Product: {{
                  products.find(p => p.id === item.productId)?.title || `ID ${item.productId}`
                }}
              </v-list-item-title>
              <v-list-item-subtitle>Quantity: {{ item.quantity }}</v-list-item-subtitle>
            </v-list-item>
          </v-list>

          <v-divider class="my-2" />
          <div class="text-right">
            <div><strong>Total Paid:</strong> ${{ order?.total.toFixed(2) }}</div>
            <div><strong>Order ID:</strong> {{ order?.id }}</div>
            <div><strong>Time:</strong> {{ order?.timestamp }}</div>
          </div>
        </v-card>
      </v-col>
    </v-row>
  </v-container>
</template>

<script setup>
import { onMounted, ref } from 'vue'
import { useRoute } from 'vue-router'
import axios from 'axios'

const route = useRoute()
const order = ref(null)
const products = ref([])

onMounted(async () => {
  const [orderRes, productsRes] = await Promise.all([
    axios.get(`/api/orders/${route.params.orderId}`),
    axios.get('/api/products')
  ])
  order.value = orderRes.data
  products.value = productsRes.data
})
</script>
