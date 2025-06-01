<template>
  <v-container class="d-flex align-center justify-center" style="height: 100vh;">
    <v-card class="pa-6" min-width="400">
      <v-card-title class="text-h5">Sign Up</v-card-title>

      <v-card-text>
        <v-form @submit.prevent="handleSignup">
          <v-text-field :rules="[rules.required, rules.name]" label="Name" v-model="name" prepend-inner-icon="mdi-account" ></v-text-field>

          <v-text-field :rules="[rules.required, rules.email]" label="Email" v-model="email" type="email" prepend-inner-icon="mdi-email" />

          <v-text-field :rules="[rules.required, rules.pw]" label="Password" v-model="password" type="password" prepend-inner-icon="mdi-lock" />

          <v-text-field :rules="[rules.required, rules.match]" label="Confirm Password" v-model="confirmPassword" type="password" prepend-inner-icon="mdi-lock-check" />
          <!-- show success msg and direct to log in -->
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

// Defining rules for the data field
const rules = {
  required: value => !!value || 'Field is required',
  name: value =>
    /^[a-zA-Z\s']+$/.test(value) || "Name must only contain letters, spaces or apostrophes",
  email: value =>
    /.+@.+\..+/.test(value) || "E-mail must be valid",
  pw: value => 
    (value && value.length >= 8) || "Password must be at least 8 characters",
  match: value =>
    (value == password.value) || "Password must match",
}

const handleSignup = () => {
  if (password.value !== confirmPassword.value) {
    alert('Passwords do not match')
    return
  }

  app.signup(name.value, email.value, password.value)
  router.push('/')
}
</script>
