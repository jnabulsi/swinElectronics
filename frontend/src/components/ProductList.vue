<template>
  <v-container class="py-8" style="max-width: 600px;">
    <v-card v-for="product in products" :key="product.id" class="mb-4">
      <v-chip v-if="product.onSale" color="green" text-color="white" size="large"
        style="position: absolute; top: 8px; right: 8px; z-index: 1;">
        On Sale
      </v-chip>
      <v-img :src="product.image" height="200px" />

      <v-card-title class="d-flex justify-space-between align-center">
        <span class="text-h6">{{ product.title }}</span>
        <span v-if="showRemoveFromCartButton" class="text-h9">Quantity: {{ product.quantity }}</span>
      </v-card-title>

      <v-card-subtitle class="text-subtitle-1">
        ${{ product.price.toFixed(2) }}
      </v-card-subtitle>

      <v-card-text>
        {{ product.description }}
        <div v-if="showOrderDate && product.date" class="text-caption mt-2">
          Purchased on: {{ product.date }}
        </div>
      </v-card-text>

      <v-card-text v-if="app.isAdmin">
        Vendor: {{ product.vendor }}
      </v-card-text>


      <v-card-actions v-if="showAddToCartButton && app.isLoggedIn">
        <v-btn color="primary" block @click="$emit('button-click', product)">
          Add To Cart
        </v-btn>
      </v-card-actions>
      <v-card-actions v-if="showRemoveFromCartButton">
        <v-btn color="red" block @click="$emit('button-click', product)">
          Remove From Cart
        </v-btn>
      </v-card-actions>

    </v-card>
  </v-container>
</template>

<script setup>
import { useAppStore } from '@/stores/app'
const app = useAppStore()
defineProps({
  products: Array,
  showAddToCartButton: Boolean,
  showRemoveFromCartButton: Boolean,
  showOrderDate: Boolean
})
</script>
