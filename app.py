from flask import Flask
from flask_restful import Api
from db.db import initialize_db
from routes.routes import initialize_routes
from errors.errors import errors

app = Flask(__name__)
api = Api(app, errors=errors)

initialize_db(app)
initialize_routes(api)

if __name__ == '__main__':
    app.run(debug=True)
