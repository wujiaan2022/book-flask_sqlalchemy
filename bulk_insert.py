from app import app
from extensions import db
from data_models import Author, Book
from datetime import datetime  # Import datetime for date conversion

# Sample data for authors
authors_data = [
    {"name": "Jane Austen", "birth_date": "1775-12-16", "date_of_death": "1817-07-18"},
    {"name": "Mark Twain", "birth_date": "1835-11-30", "date_of_death": "1910-04-21"},
    {"name": "Charles Dickens", "birth_date": "1812-02-07", "date_of_death": "1870-06-09"},
    {"name": "Mary Shelley", "birth_date": "1797-08-30", "date_of_death": "1851-02-01"},
    {"name": "George Orwell", "birth_date": "1903-06-25", "date_of_death": "1950-01-21"},
]

# Sample data for books
books_data = [
    {"title": "Pride and Prejudice", "isbn": "9780141199078", "publication_year": 1813, "author_name": "Jane Austen"},
    {"title": "Adventures of Huckleberry Finn", "isbn": "9780142437179", "publication_year": 1884, "author_name": "Mark Twain"},
    {"title": "A Tale of Two Cities", "isbn": "9780486406510", "publication_year": 1859, "author_name": "Charles Dickens"},
    {"title": "Frankenstein", "isbn": "9780486282114", "publication_year": 1818, "author_name": "Mary Shelley"},
    {"title": "1984", "isbn": "9780451524935", "publication_year": 1949, "author_name": "George Orwell"},
]


# Helper function to convert string to date
def parse_date(date_str):
    if date_str:  # Check if the string is not None
        return datetime.strptime(date_str, "%Y-%m-%d").date()
    return None  # Return None for empty or missing dates


# Bulk insert function
def bulk_insert():
    with app.app_context():
        # Insert authors
        authors = []
        for data in authors_data:
            author = Author(
                name=data["name"],
                birth_date=parse_date(data["birth_date"]),
                date_of_death=parse_date(data["date_of_death"])
            )
            authors.append(author)
        db.session.add_all(authors)
        db.session.commit()

        # Insert books
        for data in books_data:
            # Find the corresponding author
            author = Author.query.filter_by(name=data["author_name"]).first()
            if author:
                book = Book(
                    title=data["title"],
                    isbn=data["isbn"],
                    publication_year=data["publication_year"],
                    author_id=author.id
                )
                db.session.add(book)
        db.session.commit()

        print("Authors and books have been added successfully!")


# Run the bulk insertion
if __name__ == "__main__":
    bulk_insert()

