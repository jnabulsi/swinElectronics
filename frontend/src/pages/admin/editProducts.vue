<template>
  <v-container class="py-6">
    <!-- Page Title -->
    <v-row justify="center" class="mb-4">
      <v-col cols="12" md="8" class="text-center">
        <h1 class="text-h4">Edit Products</h1>
      </v-col>
    </v-row>

    <!-- Products List -->
    <v-row justify="center">
      <v-col cols="12" md="8">
        <v-card elevation="2" class="pa-4">
          <v-card-title class="text-h6">Products</v-card-title>
          <v-divider class="mb-2" />

          <v-list>
            <v-list-item v-for="(item, index) in products" :key="item.id"
              :class="{ 'border-b': index !== products.length - 1 }">
              <v-list-item-title>{{ item.title }}</v-list-item-title>
              <v-list-item-subtitle>
                Price: ${{ typeof item.price === 'number' ? item.price.toFixed(2) : item.price }}
              </v-list-item-subtitle>

              <v-list-item-subtitle>Description: {{ item.description }}</v-list-item-subtitle>
              <v-list-item-subtitle>Image: {{ item.image }}</v-list-item-subtitle>
              <v-list-item-subtitle>Category: {{ item.category }}</v-list-item-subtitle>
              <v-list-item-subtitle>On Sale: {{ item.onSale ? 'Yes' : 'No' }}</v-list-item-subtitle>
              <v-list-item-subtitle>Vendor: {{ item.vendor }}</v-list-item-subtitle>


              <template #append>
                <v-btn color="primary" @click="openEditModal(item)">Edit</v-btn>
              </template>
            </v-list-item>
          </v-list>
        </v-card>
      </v-col>
    </v-row>

    <!-- Edit Modal -->
    <v-dialog v-model="editDialog" max-width="500">
      <v-card>
        <v-card-title>Edit Product</v-card-title>
        <v-card-text>
          <v-text-field label="Title" v-model="editForm.title" />
          <v-text-field label="Price" v-model="editForm.price" type="number" />
          <v-textarea label="Description" v-model="editForm.description" />
          <v-text-field label="Image Filename" v-model="editForm.image" />
          <v-text-field label="Category" v-model="editForm.category" />
          <v-text-field label="Vendor" v-model="editForm.vendor" />
          <v-switch label="On Sale" v-model="editForm.onSale" />
        </v-card-text>
        <v-card-actions>
          <v-spacer />
          <v-btn text @click="editDialog = false">Cancel</v-btn>
          <v-btn color="primary" @click="saveChanges">Save</v-btn>
        </v-card-actions>
      </v-card>
    </v-dialog>

  </v-container>
</template>

<script setup>
import { ref, onMounted } from 'vue'
import { getProducts, updateProduct } from '@/api/products'

const products = ref([])
const editDialog = ref(false)
const selectedProduct = ref(null)
const editForm = ref({
  title: '',
  price: 0,
  description: '',
  image: '',
  category: '',
  vendor: '',
  onSale: false,
})

onMounted(async () => {
  const res = await getProducts()
  products.value = res.data
})

const openEditModal = (product) => {
  selectedProduct.value = product
  editForm.value = { ...product } // shallow copy to allow editing
  editDialog.value = true
}
const saveChanges = async () => {
  editForm.value.price = parseFloat(editForm.value.price)
  await updateProduct(selectedProduct.value.id, editForm.value)
  Object.assign(selectedProduct.value, editForm.value)
  editDialog.value = false
}


</script>
