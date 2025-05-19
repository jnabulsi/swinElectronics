<template>
  <v-container class="d-flex align-center justify-center" style="height: 100vh;">
    <v-card class="pa-6" min-width="400">
      <v-card-title class="text-h5">Sign Up</v-card-title>

      <v-card-text>
        <v-form @submit.prevent="handleSignup">
          <v-text-field label="Name" v-model="name" prepend-inner-icon="mdi-account" required />

          <v-text-field label="Email" v-model="email" type="email" prepend-inner-icon="mdi-email" required />

          <v-text-field label="Password" v-model="password" type="password" prepend-inner-icon="mdi-lock" required />

          <v-text-field label="Confirm Password" v-model="confirmPassword" type="password"
            prepend-inner-icon="mdi-lock-check" required />

          <v-btn type="submit" color="primary" block class="mt-4">Create Account</v-btn>
        </v-form>
      </v-card-text>
    </v-card>
  </v-container>
</template>

<script setup>
import { ref } from 'vue'
import { useAppStore } from '@/stores/app'
import { useRouter } from 'vue-router'

const name = ref('')
const email = ref('')
const password = ref('')
const confirmPassword = ref('')

const app = useAppStore()
const router = useRouter()

const handleSignup = () => {
  if (password.value !== confirmPassword.value) {
    alert('Passwords do not match')
    return
  }

  app.signup(name.value, email.value, password.value)

  router.push('/')
}
</script>
