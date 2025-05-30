import axios from 'axios'

export const getProducts = () => axios.get('/api/products')

export const getProductById = (id) => axios.get(`/api/products/${id}`)

export const addProduct = (product) => axios.post('/api/products', product)

export const updateProduct = (id, data) => axios.put(`/api/products/${id}`, data)
