import ordersData from '@/data/orders.json'
//import axios from 'axios'

// Use this when the endpoint is there
//export const getOrders = () => axios.get('/api/orders')

// TO BE REMOVED
// Get order history (products + purchase date)
export const getOrders = async () => {
  const enrichedOrders = ordersData.map((product) => ({
    ...product,
    // Simulate image path resolution here if needed
    image: new URL(`../assets/${product.image}`, import.meta.url).href
  }))

  return {
    data: enrichedOrders
  }
}
