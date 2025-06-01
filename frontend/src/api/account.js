import axios from 'axios'

// Create account
export const signup = ({ name, email, password }) => axios.post(`/api/signup`, { name, email, password })