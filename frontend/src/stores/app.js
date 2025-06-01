import { defineStore } from 'pinia'
import { signup } from '@/api/account'

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

    async signup(name, email, password) {
      // TODO: Replace with actual API call
      try {
        const resp = await signup({ name, email, password })
        this.isLoggedIn = true
        this.isAdmin = false
        return resp.data
      } catch (error) {
        console.log(error.resp.data)
        alert(JSON.stringify(error.resp.data))
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

