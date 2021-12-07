# REST API document

Framework choice:
* Chose Flask and Flask-RESTful as the REST API framework
* Easy to setup and simple to use
* Has built-in development server, debugger, unit test support, templating, secure cookies and RESTful request dispatching

* used Flask-RESTful as a extension to structure the REST APIs
* it has a feature call resourceful routing which provide a simple way to access the HTTP methods. for example, each function can be treated as a Resource. each Resource is a * class that inherits from the Resource class of flask_restful. once the resouce is created and defined we can add method such as GET, POST, PUT, DELETE, etc

* Flask-RESTful also provide a mechanism where I can use ORM models or custom classes as response data.


* For database, I used MongoDB as database due to better scaling capability in a distribute environment.
* it's easy to use and implement. and there is not very complex query needed in this scenario. 
* and data consistency is not a must have in this scenario.
* Create a model for Book and User. 
* Each Book has a reference field 'added_by' reference to the User. 
* Each User has a list of reference field book id referenced to the Book. 

## Improvements can be made:
* Add authentication and authorization to the REST APIs
* Add all environment variables to a seperated file
* use a database that is resided in the same network when deploy to to the cloud (AWS, Google Cloud, Azure, etc)
* instead of using Mongdb Altas
* Manage all the secrets keys using Cloud secret/key management(AWS, Google Cloud, Azure, etc)
* Add dockerfile for containerization
* Add Jenksfile for CICD deployment 
* When deploy to the Cloud, create seperated environments for Test, Beta, Production, etc


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
