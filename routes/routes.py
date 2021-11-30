from apis.book import BooksApi, BookApi
from apis.user import UserApi


def initialize_routes(api):
    api.add_resource(BooksApi, '/api/books')
    api.add_resource(BookApi, '/api/books/<id>')
    api.add_resource(UserApi, '/api/users')
