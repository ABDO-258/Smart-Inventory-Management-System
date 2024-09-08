import React from 'react';
import { Link } from 'react-router-dom';
import './Home.css';

const Home = () => {
    return (
        <div className="home">
            {/* Navigation Bar */}
            <header className="navbar">
                <div className="logo">
                    <i className="fas fa-building"></i> SIMS
                </div>
                <nav className="nav-links">
                    <Link to="/">Home</Link>
                    <Link to="/dashboard">Dashboard</Link>
                    <Link to="/products">Products</Link>
                </nav>
                <div className="auth-buttons">
                    <Link to="/signup" className="signup-btn">Sign Up</Link>
                    <Link to="/signin" className="signin-btn">Sign In</Link>
                </div>
            </header>

            {/* Main Content */}
            <main className="main-content">
                <h1>Smart Inventory Management System</h1>
                <p>Track youre products</p>
                <p>What are you waiting for?</p>
                <Link to="/start-tracking" className="start-btn">Start Tracking</Link>
            </main>

            {/* Footer 
            <footer className="footer">
                <div className="footer-logo">
                    <i className="fas fa-building"></i> SIMS
                </div>
                <p>SIMS © 2024</p>
                <div className="social-icons">
                    <i className="fab fa-facebook"></i>
                    <i className="fab fa-youtube"></i>
                    <i className="fab fa-twitter"></i>
                    <i className="fab fa-linkedin"></i>
                </div>
            </footer>*/}
        </div>
    );
};

export default Home;