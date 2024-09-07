import React, { useEffect, useState } from 'react';
import { getAllProducts } from './api';

const Products = () => {
  const [products, setProducts] = useState([]);

  useEffect(() => {
    const fetchProducts = async () => {
      try {
        const response = await getAllProducts();
        setProducts(response.data);
      } catch (error) {
        console.error('Error fetching products:', error);
      }
    };

    fetchProducts();
  }, []);

  return (
    <div>
      <h2>Products List</h2>
      <ul>
        {products.map((product) => (
          <li key={product._id}>
            {product.name} - {product.description}
          </li>
        ))}
      </ul>
    </div>
  );
};

export default Products;
 