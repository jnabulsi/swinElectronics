<template>
  <v-container class="d-flex align-center justify-center" style="height: 100vh;">
    <v-card class="pa-6" min-width="400" max-width="900">
      <v-card-title class="text-h5">Login</v-card-title>
      <v-card-text>
        <v-form @submit.prevent="handleLogin">
          <v-text-field label="Email" v-model="email" type="email" required prepend-inner-icon="mdi-email" />

          <v-text-field label="Password" v-model="password" type="password" required prepend-inner-icon="mdi-lock" />

          <v-btn type="submit" color="primary" block class="mt-4">Login</v-btn>
        </v-form>
      </v-card-text>
    </v-card>
  </v-container>
</template>

<script setup>
import { ref } from 'vue'
import { useAppStore } from '@/stores/app'
import { useRouter } from 'vue-router'

const email = ref('')
const password = ref('')

const app = useAppStore()
const router = useRouter()

const handleLogin = () => {
  app.login(email.value, password.value)

  router.push('/')
}
</script>
