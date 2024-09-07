#!/usr/bin/env python3
""" scribt for the main app"""

import os
from flask import Flask
from flask_jwt_extended import JWTManager
from .auth import auth_bp
from .products import products_bp


app = Flask(__name__)

# Configurations for JWT
# Change to environment variable in production
app.config['JWT_SECRET_KEY'] = os.getenv('JWT_SECRET_KEY', 'super-secret')
jwt = JWTManager(app)

app.register_blueprint(auth_bp)
app.register_blueprint(products_bp)


if __name__ == '__main__':
    app.run(debug=True)
