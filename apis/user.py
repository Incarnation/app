from flask import Response, request
from db.models import User
from flask_restful import Resource
from mongoengine.errors import FieldDoesNotExist, NotUniqueError, ValidationError
from errors.errors import SchemaValidationError, UserAlreadyExistsError, InternalServerError


class UserApi(Resource):
    def get(self):
        users = User.objects().to_json()
        return Response(users, mimetype="application/json", status=200)

    def post(self):
        try:
            body = request.get_json()
            user = User(**body)
            user.save()
            id = user.id
            response = {'id': str(id), "status": 'OK',
                        'message': "user has been created"}
            return Response(response, mimetype="application/json", status=201)
        except (FieldDoesNotExist, ValidationError):
            raise SchemaValidationError
        except NotUniqueError:
            raise UserAlreadyExistsError
        except Exception as e:
            raise InternalServerError
