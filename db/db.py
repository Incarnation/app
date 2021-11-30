from flask_mongoengine import MongoEngine

# hardcoding for demo purpose
CONNECTION_STRING = "mongodb+srv://eric_test:eric_test@cluster0.cj42y.mongodb.net/sample_db?retryWrites=true&w=majority"

db = MongoEngine()


def initialize_db(app):
    app.config['DEBUG'] = True
    app.config['MONGODB_HOST'] = CONNECTION_STRING
    db.init_app(app)
