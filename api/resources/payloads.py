from flask_restx import Namespace, fields, Resource

# Namespaces

api = Namespace(name='example', description='Example')

# Payloads
@api.route("/")
class Myclass(Resource):
    def get(self):
        return {}
# Headers
