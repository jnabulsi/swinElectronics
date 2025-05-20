import productsData from '@/data/products.json'
// import axios from 'axios'

//eventually getProducts will be 
// export const getProducts = () => axios.get('/api/products')


// fake async wrapper
export const getProducts = async () => {
  // Simulate async call for now
  return {
    data: productsData
  }
}

// helper to get a product by ID

// the real one
// export const getProductById = (id) => axios.get(`/api/products/${id}`)

export const getProductById = async (id) => {
  const product = productsData.find(p => p.id === id)
  return { data: product }
}

// Real addProduct to be used when endpoint is there
//export const addProduct = (product) => axios.post('/api/products', product)

// Fake add a new product (does nothing for now)
export const addProduct = async (product) => {
  console.log('[Mock] Product submitted:', product)
  return {
    data: { success: true }
  }
}



