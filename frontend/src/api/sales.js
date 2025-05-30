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


