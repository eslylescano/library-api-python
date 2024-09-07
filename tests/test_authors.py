# tests/test_authors.py
import unittest
from models.author import Author

class TestAuthorModel(unittest.TestCase):

    def test_author_creation(self):
        author = Author(name="J.K. Rowling", birth_year=1965)
        self.assertEqual(author.name, "J.K. Rowling")
        self.assertEqual(author.birth_year, 1965)
