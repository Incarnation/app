# app


Python flask project test

Run the project by running the command
pip install -r requirements.txt
and
python app.py

and run the test by running
python test.py

APIs
GET - to get all the users available 
http://127.0.0.1:5000/api/users

POST - to create a new user
http://127.0.0.1:5000/api/users

json body
{
    "first_name": "first_name",
    "last_name": "last_name",
    "email": "email",
    "password": "password",
    "books": []
}

GET - to get all the books available
http://127.0.0.1:5000/api/books

GET - get a single book with the book id as url parameter
http://127.0.0.1:5000/api/books/61a5746caebb9239739a8f96

DELETE - delete a single book with the book id as url parameter
http://127.0.0.1:5000/api/books/61a5746caebb9239739a8f96

PUT - update a single book with book id as url parameter
http://127.0.0.1:5000/api/books/61a5746caebb9239739a8f96
{
    "user_id": "61a56a765eb6cf68efab7ded",
    "book": {
        "title": "book4",
        "author": "author5",
        "isbn": "isbn6",
        "publication_date": "book1_date7"
    }
}


Create a model for Book and User
Each Book has a reference field 'added_by' reference to the User.
Each User has a list of reference field book id referenced to the Book.
Used MongoDB as database due to better scaling in a distribute environment.
Easy to use and implement. it's fast and data consistency is not very important.
and no complex queries is needed.

Used flask-restful to structure the application for better maintenance 
