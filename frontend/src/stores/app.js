import { defineStore } from 'pinia'

export const useAppStore = defineStore('app', {
  state: () => ({
    isLoggedIn: false,
    isAdmin: false,
  }),

  actions: {
    login(email, password) {
      // TODO: Replace with actual API call
      this.isLoggedIn = true
      this.isAdmin = email === 'admin' && password === 'admin' // fake admin check
    },

    signup(name, email, password) {
      // TODO: Replace with actual API call
      this.isLoggedIn = true
      this.isAdmin = false
    },

    logout() {
      // TODO: Replace with actual API call
      this.isLoggedIn = false
      this.isAdmin = false
    },
  },
  persist: true,
})

