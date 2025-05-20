import salesData from '@/data/sales.json'
//import axios from 'axios'

// Real endpoints
// export const getSalesData = () => axios.get('/api/sales')

// FAKE get sales data
export const getSalesData = async () => {
  return {
    data: salesData
  }
}


// export const purchase = (productIds) => axios.post('/api/purchase', { productIds })

// FAKE purchase method
export const purchase = async (productIds) => {
  console.log('[Mock Purchase] Products:', productIds)
  return {
    data: { success: true }
  }
}

