from flask_restx import Resource, fields, Namespace

from api.application.solicitations.controller.solicitations_controller import SolicitationsController
from api.utils.http_response import HttpResponse

# Namespace
solicitation_ns = Namespace(name='solicitation', description='solicitation')

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
        controller = SolicitationsController(response=HttpResponse())
        return controller.get_all_solicitations()


solicitation_ns.add_resource(SolicitationsResource, "/")
