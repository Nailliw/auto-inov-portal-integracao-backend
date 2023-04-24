from api.application.solicitations.core.solicitations_core import SolicitationCore
from api.utils.http_response import HttpResponse


class SolicitationsController:
    def __init__(self, response: HttpResponse, payload=''):
        self.response = response
        self.payload = payload

    def get_all_solicitations(self):
        core = SolicitationCore(payload=self.payload)

        return self.response.success(message="", data=core.get_all_solicitation())

    def create_solicitation(self):
        core = SolicitationCore(payload=self.payload)

        return self.response.success(message="Solicitação criada com sucesso", data=core.create_solicitation())
