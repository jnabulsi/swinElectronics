import axios from 'axios'

// Create account
export const signup = ({ name, email, password, age, address }) => axios.post(`/api/signup`, { name, email, password, age, address })

// Log into account
// export const login = ({ email, password }) => axios.post(`/api/login`, { email, password })