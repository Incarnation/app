from flask import Response, request
from db.models import Book, User
from flask_restful import Resource
from mongoengine.errors import FieldDoesNotExist, DoesNotExist, ValidationError, InvalidQueryError
from errors.errors import SchemaValidationError, InternalServerError, \
    UpdatingBookError, DeletingBookError, BookNotExistsError


class BooksApi(Resource):
    def get(self):
        books = Book.objects().to_json()
        return Response(books, mimetype="application/json", status=200)

    def post(self):
        try:
            body = request.get_json()
            user_id = body["user_id"]
            user = User.objects.get(id=user_id)
            book = Book(title=body["book"]["title"],
                        author=body["book"]["author"],
                        isbn=body["book"]["isbn"],
                        publication_date=body["book"]["publication_date"],
                        added_by=user)
            book.save()
            user.update(push__books=book)
            user.save()
            id = book.id
            return {'id': str(id)}, 200
        except (FieldDoesNotExist, ValidationError):
            raise SchemaValidationError
        except Exception as e:
            raise InternalServerError


class BookApi(Resource):
    def get(self, id):
        try:
            book = Book.objects.get(id=id).to_json()
            return Response(book, mimetype="application/json", status=200)
        except DoesNotExist:
            raise BookNotExistsError
        except Exception:
            raise InternalServerError

    def put(self, id):
        try:
            body = request.get_json()
            user_id = body["user_id"]
            book = Book.objects.get(id=id, added_by=user_id)
            Book.objects.get(id=id).update(title=body["book"]["title"],
                                           author=body["book"]["author"],
                                           isbn=body["book"]["isbn"],
                                           publication_date=body["book"]["publication_date"])
            return '', 200
        except InvalidQueryError:
            raise SchemaValidationError
        except DoesNotExist:
            raise UpdatingBookError
        except Exception:
            raise InternalServerError

    def delete(self, id):
        try:
            book = Book.objects.get(id=id)
            book.delete()
            return '', 200
        except DoesNotExist:
            raise DeletingBookError
        except Exception:
            raise InternalServerError
