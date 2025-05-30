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
        <v-card v-for="order in orders" :key="order.id" class="mb-6 pa-4">
          <v-card-title class="text-h6">
            Order #{{ order.id }} — {{ new Date(order.timestamp).toLocaleString() }}
          </v-card-title>
          <v-divider class="mb-2" />

          <v-list>
            <v-list-item v-for="item in order.items" :key="item.productId" class="d-flex justify-space-between">
              <div>
                {{ item.title }} (x{{ item.quantity }})
              </div>
              <div>
                ${{ (item.price * item.quantity).toFixed(2) }}
              </div>
            </v-list-item>
          </v-list>

          <v-divider class="my-2" />
          <div class="text-right">
            <strong>Total: ${{ order.total.toFixed(2) }}</strong>
          </div>
        </v-card>
      </v-col>
    </v-row>
  </v-container>
</template>

<script setup>
import { ref, onMounted } from 'vue'
import { getOrders } from '@/api/orders'
import { getProductById } from '@/api/products'

const orders = ref([])

onMounted(async () => {
  const res = await getOrders()

  const enriched = await Promise.all(
    res.data.map(async (order) => {
      const enrichedItems = await Promise.all(
        order.items.map(async (item) => {
          const productRes = await getProductById(item.productId)
          return {
            ...item,
            title: productRes.data.title,
            price: productRes.data.price,
          }
        })
      )

      return {
        ...order,
        items: enrichedItems
      }
    })
  )

  orders.value = enriched
})
</script>
