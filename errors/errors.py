class InternalServerError(Exception):
    pass


class SchemaValidationError(Exception):
    pass


class BookAlreadyExistsError(Exception):
    pass


class UserAlreadyExistsError(Exception):
    pass


class UpdatingBookError(Exception):
    pass


class DeletingBookError(Exception):
    pass


class BookNotExistsError(Exception):
    pass


class EmailAlreadyExistsError(Exception):
    pass


errors = {
    "InternalServerError": {
        "message": "Something went wrong",
        "status": 500
    },
    "SchemaValidationError": {
        "message": "Request is missing required fields",
        "status": 400
    },
    "UserAlreadyExistsError": {
        "message": "User already exists",
        "status": 400
    },
    "BookAlreadyExistsError": {
        "message": "Book already exists",
        "status": 400
    },
    "UpdatingBookError": {
        "message": "Updating book error",
        "status": 403
    },
    "DeletingBookError": {
        "message": "Deleting book error",
        "status": 403
    },
    "BookNotExistsError": {
        "message": "Book with given id doesn't exists",
        "status": 400
    },
    "EmailAlreadyExistsError": {
        "message": "User with given email address already exists",
        "status": 400
    }
}
