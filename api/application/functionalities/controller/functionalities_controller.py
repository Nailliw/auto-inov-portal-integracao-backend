from api.application.functionalities.core.functionalities_core import FunctionalitiesCore
from api.utils.http_response import HttpResponse


class FunctionalitiesController:
    def __init__(self, response: HttpResponse, payload=''):
        self.response = response
        self.payload = payload

    def verify_status(self):
        core = FunctionalitiesCore(payload=self.payload)
        response = core.verify_status()
        return self.response.success(message="", data=response)

    def perform_recycling(self):
        core = FunctionalitiesCore(payload=self.payload)
        return core.perform_recycling()
