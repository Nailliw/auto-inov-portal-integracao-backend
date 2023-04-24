"""Entrypoint of the main API Resources."""
# Useful to simulate a long action
from time import sleep

# Flask based imports


# Application based imports
from flask import request
from flask_restx import Namespace, Resource, fields

from api import factory

# Empty name is required to have the desired url path
from api.application.functionalities.controller.functionalities_controller import FunctionalitiesController
from api.application.solicitations.controller.solicitations_controller import SolicitationsController
from api.application.systems.controller.controller import SystemsController
from api.utils.http_response import HttpResponse

api = Namespace(name='', description='Main API namespace.')


# Get the celery instance
celery = factory.celery


@celery.task()
def asynchronous(name):
    """Async long task method."""
    sleep(5)
    return {'async': name}


asynchronous = asynchronous


@api.route('/hello/<name>')
@api.doc(params={'name': 'The name of the person to return hello.'})
class HelloWorld(Resource):
    """HelloWorld resource class."""

    def get(self, name):
        """Get method."""
        return {'hello': name}


@api.route('/bye/<name>')
@api.doc(params={'name': 'The name of the person to return bye.'})
class ByeWorld(Resource):
    """ByeWorld resource class."""

    def get(self, name):
        """Get method."""
        # Asynchronous long task that we don't need to know the output
        asynchronous.apply_async((name,))
        return {'bye': name}


class SystemsResource(Resource):
    def post(self):
        controller = SystemsController()
        task = asynchronous.apply_async((controller.create_system(),))
        return {'task_id': task.id}

    def get(self):
        controller = SystemsController()
        return controller.create_system()


class FunctionalitiesResource(Resource):
    def get(self):
        controller = FunctionalitiesController(response=HttpResponse())
        resp = controller.verify_status()
        return resp[0]

    def post(self):
        controller = FunctionalitiesController(response=HttpResponse(), payload=request.get_json())
        return controller.perform_recycling()


class SistemaResource(Resource):
    def get(self, system):
        return [
            {
                "camada": "JBOSS",
                "actions": ['STOP', 'START', 'RESTART', 'RECICLAGEM']
            },
            {
                "camada": "NGINX",
                "actions": ['STOP', 'START', 'RESTART', 'RECICLAGEM']
            },

        ]


# namespaces
api.add_resource(SystemsResource, "system")
api.add_resource(FunctionalitiesResource, "/functionality")
api.add_resource(SistemaResource, "/system-actions/<system>")

