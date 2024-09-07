# routes/author_routes.py
from flask import Blueprint, jsonify, request
from models.author import Author, db

author_bp = Blueprint('author_bp', __name__)

@author_bp.route('/authors', methods=['GET'])
def get_authors():
    authors = Author.query.all()
    return jsonify([{'id': author.id, 'name': author.name, 'birth_year': author.birth_year} for author in authors])

@author_bp.route('/authors/<int:author_id>', methods=['GET'])
def get_author(author_id):
    author = Author.query.get(author_id)
    if not author:
        return jsonify({'message': 'Author not found'}), 404
    return jsonify({'id': author.id, 'name': author.name, 'birth_year': author.birth_year})

@author_bp.route('/authors', methods=['POST'])
def create_author():
    data = request.get_json()
    new_author = Author(name=data['name'], birth_year=data['birth_year'])
    db.session.add(new_author)
    db.session.commit()
    return jsonify({'message': 'Author created'}), 201

@author_bp.route('/authors/<int:author_id>', methods=['PUT'])
def update_author(author_id):
    author = Author.query.get(author_id)
    if not author:
        return jsonify({'message': 'Author not found'}), 404

    data = request.get_json()
    author.name = data['name']
    author.birth_year = data['birth_year']
    db.session.commit()
    return jsonify({'message': 'Author updated'})

@author_bp.route('/authors/<int:author_id>', methods=['DELETE'])
def delete_author(author_id):
    author = Author.query.get(author_id)
    if not author:
        return jsonify({'message': 'Author not found'}), 404
    
    db.session.delete(author)
    db.session.commit()
    return jsonify({'message': 'Author deleted'})
