import axios from 'axios';

// Base URL for the Flask backend
const API_URL = process.env.REACT_APP_API_URL || 'http://localhost:5000';

// Create a new instance of axios with a custom config
const api = axios.create({
  baseURL: API_URL,
});

// Function to register a user
export const registerUser = (userData) => {
  return api.post('/register', userData);
};

// Function to login a user
export const loginUser = (userData) => {
  return api.post('/login', userData);
};

// Function to get all products
export const getAllProducts = () => {
  return api.get('/products');
};

// Function to create a new product
export const createProduct = (productData, token) => {
  return api.post('/products', productData, {
    headers: {
      Authorization: `Bearer ${token}`,
    },
  });
};

export default api;
