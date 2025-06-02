<template> 
  <v-container class="d-flex align-center justify-center" style="height: 100vh;">
    <v-card class="pa-6" min-width="400">
      <v-card-title class="text-h5">Sign Up</v-card-title>

      <v-card-text>
        <!-- automatically sets 'valid' to true only if all fields are valid -->
        <v-form @submit.prevent="handleSignup" ref="form" v-model="valid"> 
          <v-text-field :rules="[rules.required, rules.name]" label="Name" v-model="name" prepend-inner-icon="mdi-account" ></v-text-field>

          <v-text-field :rules="[rules.required, rules.email]" label="Email" v-model="email" type="email" prepend-inner-icon="mdi-email" />

          <v-text-field :rules="[rules.required, rules.age]" label="Age" v-model="age" type="age" prepend-inner-icon="mdi-cake" />

          <v-text-field :rules="[rules.required, rules.address]" label="Address" v-model="address" type="address" prepend-inner-icon="mdi-home" />

          <v-text-field :rules="[rules.required, rules.pw]" label="Password" v-model="password" type="password" prepend-inner-icon="mdi-lock" />

          <v-text-field :rules="[rules.required, rules.match]" label="Confirm Password" v-model="confirmPassword" type="password" prepend-inner-icon="mdi-lock-check" />
          <!-- show success msg and direct to log in -->
          <v-btn type="submit" color="primary" block class="mt-4" :disabled="!isFormValid" >Create Account</v-btn>
        </v-form>
      </v-card-text>
    </v-card>
  </v-container>
</template>

<script setup>
import { ref, computed } from 'vue'
import { useAppStore } from '@/stores/app'
import { useRouter } from 'vue-router'

const name = ref('')
const email = ref('')
const age = ref('')
const address = ref('')
const password = ref('')
const confirmPassword = ref('')
const form = ref(null)
const valid = ref(false)

// Value changes based on the updates on the text field values
const isFormValid = computed(() => valid.value)

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
  age: value =>
    (!!value && Number.isInteger(Number(value)) && Number(value) < 110 && Number(value) > 0 )|| "Age must be a number and be under 110",
  address: value =>
    (!!value && value.length >= 5) || "Address must be at least 5 characters long",
}

const handleSignup = () => {
  app.signup(name.value, email.value, password.value, Number(age.value), address.value)
  router.push('/')
}
</script>
