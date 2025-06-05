<template>
  <v-container class="py-6">
    <!-- Page Title -->
    <v-row justify="center" class="mb-4">
      <v-col cols="12" md="8" class="text-center">
        <h1 class="text-h4">Checkout</h1>
      </v-col>
    </v-row>

    <!-- Checkout List Wrapped in a Card -->
    <v-row justify="center">
      <v-col cols="12" md="6">
        <v-card elevation="2" class="pa-4">
          <v-card-title class="text-h6">Checkout Summary</v-card-title>
          <v-divider class="mb-2" />

          <v-list two-line>
            <v-list-item v-for="(product, index) in products" :key="product.id"
              :class="{ 'border-b': index !== products.length - 1 }">
              <v-list-item-title>
                {{ product.title }} (Amount: {{ product.quantity }})
              </v-list-item-title>
              <v-list-item-subtitle>
                ${{ (product.price * product.quantity).toFixed(2) }}
              </v-list-item-subtitle>

            </v-list-item>
          </v-list>

          <v-divider class="my-4" />

          <div class="text-right">
            <div><strong>Total:</strong> ${{ total }}</div>
          </div>
        </v-card>
      </v-col>
    </v-row>
    <!-- Purchase Button -->
    <v-row justify="center" class="mt-6">
      <v-col cols="12" md="4" class="text-center">
        <v-btn color="primary" size="large" block @click="handlePurchase">
          Complete Purchase
        </v-btn>
      </v-col>
    </v-row>
  </v-container>
</template>

<script setup>
import { ref, onMounted } from 'vue'
import { getCart } from '@/api/cart'
import { getProductById } from '@/api/products'
import { completePurchase } from '@/api/orders'
import { useRouter } from 'vue-router'

const router = useRouter()
const total = ref(0)
const products = ref([])

onMounted(async () => {
  const cartRes = await getCart()

  // Fetch all products in parallel
  const enriched = await Promise.all(
    cartRes.data.map(async (item) => {
      const productRes = await getProductById(item.productId)
      return {
        ...productRes.data,
        quantity: item.quantity,
      }
    })
  )

  products.value = enriched

  total.value = enriched.reduce((sum, item) => sum + item.price * item.quantity, 0)
})

const handlePurchase = async () => {
  const res = await completePurchase()
  const orderId = res.data.id
  router.push(`/receipt/${orderId}`)
}
</script>
