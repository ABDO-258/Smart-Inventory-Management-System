#!/usr/bin/env python3
""" script for product model"""

from typing import Optional, List
from bson.objectid import ObjectId
from pymongo.results import UpdateResult, InsertOneResult, DeleteResult
from ..db import db


class Product:
    """Product model"""
    def __init__(self, name: str, description: str, price: float,
                  quantity: int, _id: Optional[str] = None):
        self.name = name
        self.description = description
        self.price = price
        self.quantity = quantity
        self._id = _id

    @staticmethod
    def to_dict(product: 'Product') -> dict:
        """Convert product to dict for MongoDB storage."""
        return {
            "name": product.name,
            "description": product.description,
            "price": product.price,
            "quantity": product.quantity  
        }

    @staticmethod
    def from_dict(data: dict) -> Optional['Product']:
        """Create product object from dict."""
        if not data:
            return None
        return Product(
            name=data.get('name', ''),
            description=data.get('description', ''),
            price=data.get('price', 0.0),
            quantity=data.get('quantity', 0),
            _id=str(data.get('_id')) if data.get('_id') else None
        )

    def save(self) -> 'Product':
        """Save product to the database."""
        product_data = Product.to_dict(self)
        if self._id:  # Check if _id is already set
            result: UpdateResult = db.products.update_one(
                {'_id': ObjectId(self._id)},
                {'$set': product_data}
            )
            if result.modified_count == 0:
                raise Exception("No document was updated.")
        else:
            result: InsertOneResult = db.products.insert_one(product_data)
            self._id = str(result.inserted_id)  # Convert ObjectId to string
        return self

    @staticmethod
    def find_by_id(product_id: str) -> Optional['Product']:
        """Find product by id."""
        try:
            data = db.products.find_one({'_id': ObjectId(product_id)})
        except Exception as e:
            print(f"Error finding product by id: {e}")
            return None
        return Product.from_dict(data)

    @staticmethod
    def find_all() -> List['Product']:
        """Return all products."""
        return [Product.from_dict(product) for product in db.products.find()]

    @staticmethod
    def delete(product_id: str) -> DeleteResult:
        """Delete product by id."""
        try:
            return db.products.delete_one({'_id': ObjectId(product_id)})
        except Exception as e:
            print(f"Error deleting product: {e}")
            raise
