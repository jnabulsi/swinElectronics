<template>
  <v-container class="py-6">
    <!-- Page Title -->
    <v-row justify="center" class="mb-4">
      <v-col cols="12" md="8" class="text-center">
        <h1 class="text-h4">Add Product</h1>
      </v-col>
    </v-row>

    <!-- Product Form -->
    <v-row justify="center">
      <v-col cols="12" md="6">
        <v-form v-model="formValid" @submit.prevent="handleAddProduct" ref="formRef">
          <v-text-field v-model="title" label="Title" :rules="[requiredRule]" />

          <v-text-field v-model.number="price" label="Price" type="number"
            :rules="[requiredRule, positiveNumberRule]" />

          <v-textarea v-model="description" label="Description" :rules="[requiredRule]" />

          <v-text-field v-model="image" label="Image filename (e.g. monitor.jpg)" :rules="[requiredRule]" />

          <v-text-field v-model="category" label="Category" :rules="[requiredRule]" />

          <v-btn type="submit" color="primary" block class="mt-4" :disabled="!formValid">
            Add Product
          </v-btn>
        </v-form>
      </v-col>
    </v-row>
  </v-container>
</template>

<script setup>
import { ref } from 'vue'
import { addProduct } from '@/api/products'

const formRef = ref(null)
const formValid = ref(false)

const title = ref('')
const price = ref(null)
const description = ref('')
const image = ref('')
const category = ref('')

// Validation rules
const requiredRule = (v) => !!v || 'This field is required'
const positiveNumberRule = (v) => v > 0 || 'Price must be greater than 0'

const handleAddProduct = async () => {
  if (!formRef.value?.validate()) return

  const product = {
    title: title.value,
    price: price.value,
    description: description.value,
    image: image.value,
    category: category.value,
  }

  try {
    const res = await addProduct(product)
    console.log('Product submission response:', res)

    alert('Product submitted!')

    formRef.value.reset()
  } catch (err) {
    console.error('Failed to add product:', err)
    alert('Failed to submit product')
  }
}
</script>
