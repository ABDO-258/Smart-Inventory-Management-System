#!/usr/bin/env python3
""" module for authentication"""

from datetime import timedelta
from flask import Blueprint, request, jsonify, make_response
from werkzeug.security import generate_password_hash, check_password_hash
from flask_jwt_extended import create_access_token
from flask_jwt_extended import jwt_required, get_jwt_identity
from .db import db

auth_bp = Blueprint('auth', __name__)

# Predefined user roles
USER_ROLES = ['Admin', 'Manager', 'Staff']

# Users Collection
users = db.users


# Register a new user with role
@auth_bp.route('/register', methods=['POST'])
def register():
    """route to register"""
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')
    role = data.get('role')

    # Validate role
    if role not in USER_ROLES:
        return jsonify({'msg': 'Invalid role'}), 400

    # Check if user exists
    if users.find_one({'username': username}):
        return jsonify({'msg': 'User already exists'}), 400

    # Validate required fields
    if not username or not password:
        return jsonify({'msg': 'Username and password are required'}), 400

    # Hash password and insert user
    hashed_password = generate_password_hash(password)
    users.insert_one(
        {'username': username,
         'password': hashed_password,
         'role': role}
         )

    return jsonify({'msg': 'User registered successfully'}), 201


# Login and get JWT
@auth_bp.route('/login', methods=['POST'])
def login():
    """route to login"""
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')

    # Find the user by username
    user = users.find_one({'username': username})
    if not user or not check_password_hash(user['password'], password):
        return jsonify({'msg': 'Invalid username or password'}), 401

    # Create JWT access token
    access_token = create_access_token(
        identity={'username': username,
                  'role': user['role']},
                  expires_delta=timedelta(hours=1)  # Token expires in 1 hour
                   )
    # Set token in a cookie (secure, httpOnly)
    response = make_response(jsonify({"msg": "Login successful"}))
    response.set_cookie('access_token', access_token,
                        httponly=True, secure=True)

    return response


# Protect a route
@auth_bp.route('/protected', methods=['GET'])
@jwt_required()
def protected():
    """a protected route """
    current_user = get_jwt_identity()
    return jsonify(logged_in_as=current_user), 200


# Role-based route for Admin
@auth_bp.route('/admin', methods=['GET'])
@jwt_required()
def admin():
    """route for admin"""
    current_user = get_jwt_identity()
    if current_user['role'] != 'Admin':
        return jsonify({"msg": "Admin access required"}), 403
    return jsonify(msg="Welcome Admin!"), 200
