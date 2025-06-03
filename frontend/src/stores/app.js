import { defineStore } from 'pinia'
import { signup, login } from '@/api/account'

export const useAppStore = defineStore('app', {
  state: () => ({
    isLoggedIn: false,
    isAdmin: false,
    user: null, // storing user obj
  }),

  actions: {
    // login(email, password) {
    //   // TODO: Replace with actual API call
    //   this.isLoggedIn = true
    //   this.isAdmin = email === 'admin' && password === 'admin' // fake admin check
    // },

    async login(email, password){
      try{
        const resp = await login({email, password})
        this.user = resp.data
        this.isLoggedIn = true
        this.isAdmin = false
      } catch(error) {
        console.log(error.response.data)
        throw error
      }
    },

    async signup(name, email, password, age, address) {
      try {
        const resp = await signup({ name, email, password, age, address })
        console.log("this is the response:", resp)
        console.log("user name:", resp)
        console.log("user email:", resp)
        console.log("user pw:", resp)

        this.user = resp.data
        this.isLoggedIn = true
        this.isAdmin = false
        
      } catch (error) {
        console.log(error.response.data)
        throw error
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

