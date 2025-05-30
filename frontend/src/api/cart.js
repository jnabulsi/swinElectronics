import axios from 'axios'


export const addToCart = ({ productId }) =>
  axios.post('/api/cart', { productId })

export const getCart = () => axios.get('/api/cart')

export const removeFromCart = (productId) =>
  axios.delete(`/api/cart/${productId}`)

