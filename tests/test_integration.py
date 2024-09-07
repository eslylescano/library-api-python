import unittest
import json
from app import app, db
from models.book import Book
from models.author import Author
from models.customer import Customer

class LibraryIntegrationTest(unittest.TestCase):

    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

        with app.app_context():
            db.create_all()

    def tearDown(self):
        with app.app_context():
            db.session.remove()
            db.drop_all()

    def test_get_books(self):
        response = self.app.get('/books', headers={'Authorization': 'Bearer token'})
        self.assertEqual(response.status_code, 200)

    def test_create_author(self):
        response = self.app.post('/authors', 
                                 data=json.dumps({
                                     'name': 'Test Author', 
                                     'birth_year': 1970
                                 }),
                                 content_type='application/json',
                                 headers={'Authorization': 'Bearer token'})
        self.assertEqual(response.status_code, 201)

    def test_create_customer(self):
        response = self.app.post('/customers', 
                                 data=json.dumps({
                                     'name': 'John Doe', 
                                     'email': 'john@example.com'
                                 }),
                                 content_type='application/json',
                                 headers={'Authorization': 'Bearer token'})
        self.assertEqual(response.status_code, 201)
