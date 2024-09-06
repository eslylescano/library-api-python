from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Book(db.Model):
    __tablename__= 'books'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    author_id = db.Column(db.Integer, nullable=False)
    published_year = db.Column(db.Integer)

    def __repr__(self):
        return f"<Book {self.title}>"