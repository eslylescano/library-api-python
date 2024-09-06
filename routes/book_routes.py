from flask import Blueprint, jsonify, request
from models.book import Book, db

book_bp = Blueprint('book_bp',__name__)

@book_bp.route('/books',methods=['GET'])
def get_books():
    books = Book.query.all()
    return jsonify([{'id':book.id,'title':book.title,'author_id':book.author_id}  for book in books])

@book_bp.route('/books/<int:book_id>',methods=['GET'])
def get_book(book_id):
    book = Book.query.get(book_id)
    if not book:
        return jsonify({'message':'Book not found'}),404
    return jsonify({id:book.id,'title':book.title,'author_id':book.author_id})

@book_bp.route('/books/<int:book_id>',methods=['GET'])
def get_bopok(book_id):
    book = Book.query.get(book_id)
    if not book:
        return jsonify({'message':'Book not found'}),404
    return jsonify({'id':book.id,'title':book.title,'author_id':book.author_id})

@book_bp.route('/books', methods=['POST'])
def create_book():
    data = request.get_json()
    new_book = Book(title=data['title'], author_id=data['author_id'], published_year=data['published_year'])
    db.session.add(new_book)
    db.session.commit()
    return jsonify({'message': 'Book created'}), 201

@book_bp.route('/books/<int:book_id>', methods=['PUT'])
def update_book(book_id):
    book = Book.query.get(book_id)
    if not book:
        return jsonify({'message': 'Book not found'}), 404

    data = request.get_json()
    book.title = data['title']
    book.author_id = data['author_id']
    book.published_year = data['published_year']
    db.session.commit()
    return jsonify({'message': 'Book updated'})

@book_bp.route('/books/<int:book_id>', methods=['DELETE'])
def delete_book(book_id):
    book = Book.query.get(book_id)
    if not book:
        return jsonify({'message': 'Book not found'}), 404
    
    db.session.delete(book)
    db.session.commit()
    return jsonify({'message': 'Book deleted'})