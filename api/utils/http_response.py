class HttpResponse:
    """
    Response structures.
    """

    @staticmethod
    def success(message: str, data="Done"):
        status_code = 200
        response = {
            "data": data,
            "message": message,
            "code": status_code,
            "success": True,
        }
        print(response)
        return response, status_code

    @staticmethod
    def created(message: str, data):
        status_code = 201
        response = {
            "data": data,
            "message": message,
            "code": status_code,
            "success": True,
        }
        print(response)
        return response, status_code

    @staticmethod
    def failed(message: str, data=None, status_code: int = 400):
        response = {
            "data": data,
            "message": message,
            "code": status_code,
            "success": False,
        }
        print(response)
        return response, status_code

    @staticmethod
    def unauthorized(message: str, data=None, status_code: int = 403):
        response = {
            "data": data,
            "message": message,
            "code": status_code,
            "success": True,
        }
        print(response)
        return response, status_code

    @staticmethod
    def conflict(message: str, data=None, status_code: int = 409):
        response = {
            "data": data,
            "message": message,
            "code": status_code,
            "success": True,
        }
        print(response)
        return response, status_code

    @staticmethod
    def internal_error(message: str, status_code: int = 500):
        response = {"message": message, "code": status_code, "success": False}
        print(response)
        return response, status_code

    @staticmethod
    def custom(message: str, status_code: int, success: bool):
        response = {"message": message, "code": status_code, "success": success}
        print(response)
        return response, status_code
