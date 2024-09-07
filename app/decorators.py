#!/usr/bin/env python3
""" scribt for the main app"""

from functools import wraps
from flask import jsonify
from flask_jwt_extended import get_jwt_identity


def role_required(*roles):
    """Decorator to restrict access based on user roles."""
    def wrapper(fn):
        @wraps(fn)
        def decorator(*args, **kwargs):
            current_user = get_jwt_identity()
            if current_user['role'] not in roles:
                return jsonify({
                    "msg": (
                        "You don't have permission to perform this action."
                    )
                }), 403
            return fn(*args, **kwargs)
        return decorator
    return wrapper
