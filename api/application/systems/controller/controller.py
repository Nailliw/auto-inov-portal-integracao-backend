from api.application.systems.core.core import SystemsCore


class SystemsController:
    def create_system(self):
        systems_core = SystemsCore()
        systems_core.create_system()
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

