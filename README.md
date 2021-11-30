# app

Python flask project test

Run the project by running the command
pip install -r requirements.txt

and run the test by running
python test.py


Create a model for Book and User
Each Book has a reference field 'added_by' reference to the User 
Each User has a list of reference field book id referenced to the Book
Used MongoDB as database due to better scaling in a distribute environment
Easy to use and implement. it's fast and data consistency is not very important
and no complex queries is needed

Used flask-restful to structure the application for better maintenance 
