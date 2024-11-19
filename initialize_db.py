from app import app
from extensions import db
from data_models import Author, Book

with app.app_context():
    db.create_all()
    print("Tables created successfully!")