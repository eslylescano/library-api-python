from flask import request, jsonify

def auth_middleware():
    token = request.headers.get('Authorization')
    if not token or token != "Bearer token":
        return jsonify({'message': 'Unauthorized'}), 401
