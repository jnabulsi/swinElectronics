import axios from 'axios'

// modify the following
export const signup = ({ name, email, password }) => axios.post(`/api/signup`, { name, email, password })
