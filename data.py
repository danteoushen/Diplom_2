class Urls:
    URL = 'https://stellarburgers.nomoreparties.site/'

class API:
    CREATE_USER = '/api/auth/register'
    LOGIN_USER = '/api/auth/login'
    DELETE_USER = '/api/auth/user'
    ORDER = '/api/orders'


class Ingredients:
    VALID_INGREDIENTS = {
        "ingredients": ["61c0c5a71d1f82001bdaaa6d", "61c0c5a71d1f82001bdaaa6f"]
    }

    INVALID_INGREDIENTS = {
        "ingredients": ["61c0c5a71d1", "61c0c5a71d1f"]
    }

    WITHOUT_INGREDIENTS = {
        "ingredients": []
    }


class Responses:
    REQUIRED_FIELD = "Email, password and name are required fields"
    USER_EXIST = 'User already exists'
    INVALID_DATA = "email or password are incorrect"
    SERVER_ERROR = "Internal Server Error"
    NOT_AUTHORIZED = "You should be authorised"
    EMPTY_ORDER = "Ingredient ids must be provided"

