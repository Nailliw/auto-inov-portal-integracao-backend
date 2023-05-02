from api.application.solicitations.controller.serializer import solicitation_serializer, get_all_solicitation
from api.application.solicitations.core.solicitations_core import SolicitationCore
from api.utils.http_response import HttpResponse


class SolicitationsController:
    def __init__(self, response: HttpResponse, payload=''):
        self.response = response
        self.payload = payload

    def get_all_solicitations(self):
        core = SolicitationCore(payload=self.payload)

        return self.response.success(message="", data=get_all_solicitation(core.get_all_solicitation()))

    def create_solicitation(self):
        core = SolicitationCore(payload=self.payload)
        response = core.create_solicitation()

        return self.response.success(message="Solicitação criada com sucesso", data=solicitation_serializer(response))
