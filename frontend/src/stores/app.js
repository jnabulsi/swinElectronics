import { defineStore } from 'pinia'
import { signup } from '@/api/account'

export const useAppStore = defineStore('app', {
  state: () => ({
    isLoggedIn: false,
    isAdmin: false,
    user: null, // storing user obj
  }),

  actions: {
    login(email, password) {
      // TODO: Replace with actual API call
      this.isLoggedIn = true
      this.isAdmin = email === 'admin' && password === 'admin' // fake admin check
    },

    async signup(name, email, password) {
      // TODO: Replace with actual API call
      try {
        const resp = await signup({ name, email, password })
        this.user = resp.data
        this.isLoggedIn = true
        this.isAdmin = false
        
      } catch (error) {
        console.log(error.response.data)
      }
    },

    logout() {
      // TODO: Replace with actual API call
      this.isLoggedIn = false
      this.isAdmin = false
    },
  },
  persist: true,
})

