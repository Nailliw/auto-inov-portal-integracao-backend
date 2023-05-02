import pdb

from flask import request
from flask_restx import Resource, fields, Namespace

from api.application.solicitations.controller.solicitations_controller import SolicitationsController
from api.application.solicitations.repository.solicitations_repository import SolicitationRepository
from api.resources.celery_task import asynchronous
from api.utils.http_response import HttpResponse

# Namespace
solicitation_ns = Namespace(name='solicitation', description='Endpoint')

new_solciitation_payload = solicitation_ns.model(
    "NewSolicitationModel", {
        "user_id": fields.String(required=True),
        "username": fields.String(required=True),
    }
)


# Resource
class SolicitationsResource(Resource):
    def get(self):
        controller = SolicitationsController(response=HttpResponse())
        return controller.get_all_solicitations()

    @solicitation_ns.expect(new_solciitation_payload, validate=False)
    def post(self):
        controller = SolicitationsController(response=HttpResponse(), payload=request.get_json())
        task = asynchronous.apply_async((controller.create_solicitation(),))

        return {'task_id': task.id}


solicitation_ns.add_resource(SolicitationsResource, "")
