from extensions import db


class Author(db.Model):
    """
    Represents an author in the library database.

    Attributes:
        id (int): The unique identifier for the author (Primary Key).
        name (str): The full name of the author. This field is required.
        birth_date (date): The author's date of birth. This field is required.
        date_of_death (date, optional): The author's date of death. If not provided, it is assumed the author is still alive.

    Methods:
        __repr__(): Returns a detailed string representation of the Author instance for debugging.
        __str__(): Returns a user-friendly string representation of the Author instance.
    """
    # Define the table name (optional, defaults to the class name)
    __tablename__ = 'authors'
    
    # Attributes (columns)
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)  # Auto-incrementing PK
    name = db.Column(db.String(100), nullable=False)  # Name (String, required)
    birth_date = db.Column(db.Date, nullable=False)  # Birth date (Date, required)
    date_of_death = db.Column(db.Date, nullable=True)  # Date of death (Date, optional)

    # Customize string representation
    def __repr__(self):
        """Returns a detailed string representation of the Author instance for debugging."""
        return f"<Author(id={self.id}, name='{self.name}', birth_date={self.birth_date}, date_of_death={self.date_of_death})>"
    
    def __str__(self):
        """Returns a user-friendly string representation of the Author instance."""
        return f"Author: {self.name} (Born: {self.birth_date}, Died: {self.date_of_death or 'N/A'})"


class Book(db.Model):
    """
        Represents a book in the library database.

        Attributes:
            id (int): The unique identifier for the book (Primary Key).
            isbn (str): The ISBN of the book. This field is required.
            title (str): The title of the book. This field is required.
            publication_year (int): The year the book was published. This field is optional.
            author_id (int): The foreign key that connects the book to an author. This field is required.
        Methods:
            __repr__(): Returns a detailed string representation of the Book instance for debugging.
            __str__(): Returns a user-friendly string representation of the Book instance.
        """
    __tablename__ = 'books'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), nullable=False)
    isbn = db.Column(db.String(13), nullable=False, unique=True)
    publication_year = db.Column(db.Integer, nullable=True)
    author_id = db.Column(db.Integer, db.ForeignKey('authors.id'), nullable=False)

    # Relationship with Author
    author = db.relationship('Author', backref=db.backref('books', lazy=True))

    @property
    def cover_url(self):
        """
        Returns the URL for the book's cover image using the Open Library Covers API.
        Falls back to a default cover image if the ISBN is missing or invalid.
        """
        if self.isbn:
            return f"https://covers.openlibrary.org/b/isbn/{self.isbn}-L.jpg"
        return "/static/default-cover.png"

