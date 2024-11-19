
from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
from data_models import db, Author, Book


# Create an instance of the Flask application
app = Flask(__name__)


# Configure the SQLAlchemy database URI to use an SQLite database located at 'data/library.sqlite'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data/library.sqlite'

# Initialize the SQLAlchemy object with the Flask app instance
db.init_app(app)


@app.route('/add_author', methods=['GET', 'POST'])
def add_author():
    """
    Handles adding a new author to the database.

    - **GET Request**:
        Renders the `add_author.html` template with a form to collect information about an author.
        The form includes fields for:
            - Name (required)
            - Birthdate (required)
            - Date of Death (optional)

    - **POST Request**:
        Processes the submitted form data to add a new author to the database.
        - Retrieves the following fields from the form:
            - `name`: Name of the author (required).
            - `birthdate`: Author's date of birth (required).
            - `date_of_death`: Author's date of death (optional).
        - Creates an instance of the `Author` model.
        - Saves the new author to the database using SQLAlchemy.
        - Displays a success message if the operation is successful.
        - Rolls back the transaction and displays an error message if an exception occurs.

    Returns:
        str: Renders the `add_author.html` template.
        - If a POST request succeeds, includes a `success_message` in the rendered template.
    """
    success_message = None  # To store success feedback

    if request.method == 'POST':
        # Get form data
        name = request.form['name']
        birthdate = request.form['birthdate']
        date_of_death = request.form.get('date_of_death', None)  # Optional field

        # Create a new Author instance
        new_author = Author(name=name, birth_date=birthdate, date_of_death=date_of_death)

        # Add the new author to the database
        try:
            db.session.add(new_author)
            db.session.commit()
            success_message = f"Author '{name}' was successfully added!"
        except Exception as e:
            db.session.rollback()
            success_message = f"An error occurred: {str(e)}"

    # Render the form with success message (if POST succeeded)
    return render_template('add_author.html', success_message=success_message)


@app.route('/add_book', methods=['GET', 'POST'])
def add_book():
    """
    Handles adding a new book to the database.

    - GET Request: Renders the `add_book.html` template with a dropdown list of authors.
    - POST Request: Processes the form data and saves the new book to the database.
    """
    success_message = None  # To store feedback after form submission

    if request.method == 'POST':
        # Get form data
        title = request.form['title']
        isbn = request.form['isbn']
        publication_year = request.form['publication_year']
        author_id = request.form['author_id']

        # Create a new Book instance
        new_book = Book(
            title=title,
            isbn=isbn,
            publication_year=publication_year,
            author_id=author_id
        )

        # Add the book to the database
        try:
            db.session.add(new_book)
            db.session.commit()
            success_message = f"Book '{title}' was successfully added!"
        except Exception as e:
            db.session.rollback()
            success_message = f"An error occurred: {str(e)}"

    # Query all authors for the dropdown menu
    authors = Author.query.all()

    # Render the template with authors and success message
    return render_template('add_book.html', authors=authors, success_message=success_message)


 
  