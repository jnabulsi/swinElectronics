import { defineStore } from 'pinia'
import { signup, login } from '@/api/account'

export const useAppStore = defineStore('app', {
  state: () => ({
    isLoggedIn: false,
    isAdmin: false,
    account: null,
  }),

  actions: {
    async login(email, password) {
      try {
        const resp = await login({ email, password })
        this.account = resp.data
        this.isLoggedIn = true

        if (this.account && this.account.isAdmin == true) {
          this.isAdmin = true
        } else {
          this.isAdmin = false
        }
      } catch (error) {
        console.log(error.response.data)
        throw error
      }
    },

    async signup(name, email, password, address) {
      try {
        const resp = await signup({ name, email, password, address })

        this.user = resp.data
        this.isLoggedIn = true
        this.isAdmin = false

      } catch (error) {
        console.log(error.response.data)
        throw error
      }
    },

    logout() {
      this.isLoggedIn = false
      this.isAdmin = false
    },
  },
  persist: true,
})

