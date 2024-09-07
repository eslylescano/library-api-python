import unittest
from models.book import Book

class TestBookModel(unittest.TestCase):
    def test_book_creation(self):
        book = Book(title="The Catcher in the Rye", author_id=1, published_year=1951)
        self.assertEqual(book.title,"The Catcher in the Rye")
        self.assertEqual(book.author_id, 1)
        self.assertEqual(book.published_year, 1951)