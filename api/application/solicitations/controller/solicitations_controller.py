from api import factory
from api.application.solicitations.controller.serializer import solicitation_serializer, get_all_solicitation
from api.application.solicitations.core.solicitations_core import SolicitationCore
from api.utils.http_response import HttpResponse
celery = factory.celery


class SolicitationsController:
    def __init__(self, response: HttpResponse, payload=''):
        self.response = response
        self.payload = payload

    def get_all_solicitations(self):
        core = SolicitationCore(payload=self.payload)

        return self.response.success(message="", data=get_all_solicitation(core.get_all_solicitation()))


# @celery.task()
def create_solicitation(payload):
    core = SolicitationCore(payload=payload)

    new_solicitation = core.create_solicitation()
    run_solicitation = core.run_solicitation()

    return solicitation_serializer(new_solicitation)
