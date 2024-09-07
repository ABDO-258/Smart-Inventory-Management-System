import './App.css';
import React, { useState } from 'react';
import Login from './Login';
import Products from './Products';
import Register from './Register';

function App() {
  const [token, setToken] = useState(null);


  return (
    <div className="App">
      <h1>Inventory Management System</h1>
      {!token ? <Login setToken={setToken} /> : <Products />}
      <Register />
    </div>
  );
}

export default App;
