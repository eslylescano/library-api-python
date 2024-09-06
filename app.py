from flask import Flask
from config import Config
from models.book import db
from routes.book_routes import book_bp

app = Flask(__name__)
app.config.from_object(Config)
app.register_blueprint(book_bp)

db.init_app(app)

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)