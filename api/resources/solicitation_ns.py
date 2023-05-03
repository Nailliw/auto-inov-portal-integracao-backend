from flask import request
from flask_restx import Resource, fields, Namespace

from api.application.solicitations.controller.solicitations_controller import SolicitationsController, \
    create_solicitation
from api.utils.http_response import HttpResponse

# Namespace
solicitation_ns = Namespace(name='solicitation', description='Endpoint')

new_solicitation = solicitation_ns.model(
    "NewSolicitationModel", {
        "user_id": fields.String(required=True),
        "username": fields.String(required=True),
        "application": fields.String(required=True),
        "actions": fields.List(fields.String)
    }
)


# Resource
class SolicitationsResource(Resource):
    def get(self):
        controller = SolicitationsController(response=HttpResponse())
        return controller.get_all_solicitations()

    @solicitation_ns.expect(new_solicitation, validate=False)
    def post(self):
        # task = create_solicitation.delay(request.get_json())

        task = create_solicitation(request.get_json())
        return {'task_id': task.id}


solicitation_ns.add_resource(SolicitationsResource, "")
