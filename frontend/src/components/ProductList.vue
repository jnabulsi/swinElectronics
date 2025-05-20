<template>
  <v-container class="py-8" style="max-width: 600px;">
    <v-card v-for="product in products" :key="product.id" class="mb-4">
      <v-img :src="product.image" height="200px" />

      <v-card-title class="text-h6">
        {{ product.title }}
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

      <v-card-actions v-if="showAddToCartButton">
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
defineProps({
  products: Array,
  showAddToCartButton: Boolean,
  showRemoveFromCartButton: Boolean,
  showOrderDate: Boolean
})
</script>
