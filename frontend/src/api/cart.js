// import axios from 'axios'


// eventually addToCart will be:
// export const addToCart = ({ productId}) =>
//   axios.post('/api/cart', { productId })


// fake async wrapper for addToCart
export const addToCart = async ({ productId }) => {
  console.log('[Mock] Added to cart:', { productId })
  return {
    data: { success: true }
  }
}

//remove this when api is connected
// Simulated cart state (IDs only)
let cartItems = [
  { productId: 1, quantity: 1 },
  { productId: 2, quantity: 2 },
]


// Use this when the endpoint is there
//export const getCart = () => axios.get('/api/cart')

// Get cart: returns IDs and quantities
export const getCart = async () => {
  return {
    data: cartItems
  }
}

// Use this when the endpoint is there
//export const removeFromCart = (productId) =>
//axios.delete(`/api/cart/${productId}`)

// Remove from cart (by product ID)
export const removeFromCart = async (productId) => {
  cartItems = cartItems.filter((item) => item.productId !== productId)
  console.log('[Mock] Removed from cart:', productId)
  return {
    data: { success: true }
  }
}


