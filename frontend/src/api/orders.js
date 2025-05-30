import axios from 'axios'

export const getOrders = () => axios.get('/api/orders')

export const completePurchase = () => axios.post('/api/orders/checkout')
