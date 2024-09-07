from flask import Flask
from config import Config
from models.book import db
from routes.book_routes import book_bp
from routes.author_routes import author_bp
from routes.customer_routes import customer_bp

app = Flask(__name__)
app.config.from_object(Config)
app.register_blueprint(book_bp)
app.register_blueprint(author_bp)
app.register_blueprint(customer_bp)

db.init_app(app)

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)