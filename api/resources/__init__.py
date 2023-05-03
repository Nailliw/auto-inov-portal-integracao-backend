"""Initialization module of Resources."""
# Flask based imports
from flask import Blueprint

# Api based imports
from flask_restx import Api

from api.config import Config

# Resources based imports
from api.resources.main import api as main
from api.resources.payloads import api as ns1
from api.resources.solicitation_ns import solicitation_ns

blueprint = Blueprint('api', __name__, url_prefix='/api')

# API instantiation
api = Api(blueprint,
          title=Config.TITLE,
          version=Config.VERSION,
          description=Config.DESCRIPTION)

# Namespaces registration
api.add_namespace(main, path='')
api.add_namespace(ns1, path='')
api.add_namespace(solicitation_ns, path='')
