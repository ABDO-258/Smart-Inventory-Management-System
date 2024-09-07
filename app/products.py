#!/usr/bin/env python3
""" route for products CRUD"""

from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required
from .models.product import Product
from .decorators import role_required
from .db import db

products_bp = Blueprint('products', __name__)


@products_bp.route('/products', methods=['POST'])
@jwt_required()
@role_required('Admin', 'Manager')
def create_product():
    """ route to create a product"""
    data = request.get_json()
    name = data.get('name')
    description = data.get('description')
    price = data.get('price')
    quantity = data.get('quantity')

    if not name or not price or not quantity:
        return jsonify({"msg": "Invalid product data"}), 400

    product = Product(
        name=name,
        description=description,
        price=price,
        quantity=quantity
        )
    product.save()

    return jsonify({'msg': 'Product created successfully',
                    'product': product.__dict__}), 201


# Get a product by ID
@products_bp.route('/products/<product_id>', methods=['GET'])
@jwt_required()
@role_required('Admin', 'Manager')
def get_product(product_id):
    """route to get a product by id """
    product = Product.find_by_id(product_id)
    if not product:
        return jsonify({"msg": "Product not found"}), 404

    return jsonify(product.__dict__), 200


# Update a product by ID
@products_bp.route('/products/<product_id>', methods=['PUT'])
@jwt_required()
@role_required('Admin', 'Manager')
def update_product(product_id):
    """Update a product by ID"""
    data = request.get_json()
    product = Product.find_by_id(product_id)
    if not product:
        return jsonify({"msg": "Product not found"}), 404

    product.name = data.get('name', product.name)
    product.description = data.get('description', product.description)
    product.price = data.get('price', product.price)
    product.quantity = data.get('quantity', product.quantity)

    product.save()

    return jsonify({'msg': 'Product updated successfully',
                    'product': product.__dict__}), 200


# Delete a product by ID
@products_bp.route('/products/<product_id>', methods=['DELETE'])
@jwt_required()
@role_required('Admin', 'Manager')
def delete_product(product_id):
    """route to delete a product"""
    product = Product.find_by_id(product_id)
    if not product:
        return jsonify({"msg": "Product not found"}), 404

    Product.delete(product_id)
    return jsonify({'msg': 'Product deleted successfully'}), 200


# Get all products
@products_bp.route('/products', methods=['GET'])
@jwt_required()
def get_all_products():
    # """ rout to list all product"""
    # products = Product.find_all()
    # return jsonify([product.__dict__ for product in products]), 200
    """Route to list all products with pagination."""
    try:
        page = int(request.args.get('page', 1))
        per_page = int(request.args.get('per_page', 10))
    except ValueError:
        return jsonify({'msg': 'Invalid pagination parameters.'}), 400

    try:
        products = db.products.find().skip((
            page - 1) * per_page).limit(per_page)
        products_list = [Product.from_dict(
            product).__dict__ for product in products]
    except Exception as e:
        return jsonify({'msg': f'Error retrieving products: {e}'}), 500

    return jsonify(products_list), 200


@products_bp.route('/products/search', methods=['GET'])
@jwt_required()
def search_products():
    """Route to search for products by name."""
    query = request.args.get('q', '')
    if not query:
        return jsonify({'msg': 'Search query is required.'}), 400

    try:
        products = db.products.find({"name": {"$regex": query,
                                              "$options": "i"}})
        products_list = [Product.from_dict(
            product).__dict__ for product in products]
    except Exception as e:
        return jsonify({'msg': f'Error searching products: {e}'}), 500

    return jsonify(products_list), 200
