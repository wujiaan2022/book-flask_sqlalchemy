from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from data_models import db, Author, Book


# Create an instance of the Flask application
app = Flask(__name__)


# Configure the SQLAlchemy database URI to use an SQLite database located at 'data/library.sqlite'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data/library.sqlite'

# Initialize the SQLAlchemy object with the Flask app instance
db.init_app(app)


@app.route('/add_author', methods = ['Get', 'Post'])
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

 
  