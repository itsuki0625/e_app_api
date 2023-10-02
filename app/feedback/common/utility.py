"""app/feedback/common/__init__.py
"""

from flask import jsonify

def err_response(error):
    """err_response
    """
    return jsonify({
        "code": error.code,
        "name": error.name,
        "description": error.description,
    })