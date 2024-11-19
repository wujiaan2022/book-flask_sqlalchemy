from app import app
from extensions import db
from data_models import Author, Book
from sqlalchemy import inspect

import os
os.makedirs('data', exist_ok=True)

with app.app_context():
    db.create_all()
    print("Database tables created successfully!")

    # Use the SQLAlchemy inspector to get the table names
    inspector = inspect(db.engine)
    tables = inspector.get_table_names()
    print("Tables in the database:", tables)