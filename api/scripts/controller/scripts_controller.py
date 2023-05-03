from api.scripts.core.sinep_core import SinepCore


class ScriptsController:
    def __init__(self, application, actions):
        self.application = application
        self.actions = actions

    def define_application_actions(self):
        application = self.application

        if application == "SINEP":
            SinepCore().init_action(self.actions)
