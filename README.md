# REST API document


For database, create a model for Book and User. 
Each Book has a reference field 'added_by' reference to the User. 
Each User has a list of reference field book id referenced to the Book. 

Used MongoDB as database due to better scaling in a distribute environment. 
Easy to use and implement. 
it's fast and data consistency is not very important. 
and no complex queries is needed.

Used flask-restful to structure the application for better maintenance

## Install

    pip install -r requirements.txt

## Run the app

    python app.py

## Run the tests

    python test.py

# REST API


## Get all the availabe users

### Request

`GET /api/users`

    curl -i -H 'Accept: application/json' http://127.0.0.1:5000/api/users



## Create a new user

### Request

`POST /api/users/`

    curl -i -H 'Accept: application/json' -d 'name=Foo&status=new' http://localhost:7000/thing

### Request body

    { "first_name": "first_name", "last_name": "last_name", "email": "email", "password": "password", "books": [] }

## Get all the books

### Request

`GET /api/books`

    curl -i -H 'Accept: application/json' http://127.0.0.1:5000/api/books

## Get a single book

### Request

`GET /api/books/id`

    curl -i -H 'Accept: application/json' http://127.0.0.1:5000/api/books/61a5746caebb9239739a8f96

## Create a new book

### Request

`POST /api/books`

    curl -i -H 'Accept: application/json' http://127.0.0.1:5000/api/books

### Request body

    {
        "user_id": "61a56a765eb6cf68efab7ded",
        "book": {
            "title": "book2",
            "author": "author2",
            "isbn": "isbn2",
            "publication_date": "book1_date2"
        }
    }

## Update a book

### Request

`PUT /api/books/id`

    curl -i -H 'Accept: application/json' http://127.0.0.1:5000/api/books/61a5746caebb9239739a8f96

### Request body
    
    {
        "user_id": "61a56a765eb6cf68efab7ded",
        "book": {
            "title": "book4",
            "author": "author5",
            "isbn": "isbn6",
            "publication_date": "book1_date7"
        }
    }

## Delete a book

### Request

`DELETE /api/books/id`

    curl -i -H 'Accept: application/json' -X DELETE http://127.0.0.1:5000/api/books/61a5746caebb9239739a8f96
