from api.application.functionalities.repository.application_repository import ApplicationRepository
from api.application.functionalities.repository.functionality_repository import FunctionalityRepository
from api.application.solicitations.repository.solicitations_repository import SolicitationRepository
from api.application.solicitations.repository.users_repository import UserRepository
from api.orm.tables import Solicitation, User, Application, Functionality


class SolicitationCore:
    def __init__(self, payload):
        self.payload = payload
        self.solicitation_repository = SolicitationRepository()
        self.user_repository = UserRepository()
        self.application_repository = ApplicationRepository()
        self.functionaties_repository = FunctionalityRepository()

    def get_all_solicitation(self):
        return self.solicitation_repository.get_all(model=Solicitation)

    def create_solicitation(self):
        user = self.user_repository.get_user_by_id(self.payload.get("user_id"))

        if not user:
            user_model = User(
                id=self.payload.get("user_id"),
                login=self.payload.get("user_id"),
                name=self.payload.get("username")
            )
            self.user_repository.create_user(user_model)

        new_solicitation = Solicitation(
            user_id=self.payload.get("user_id"),
            username=self.payload.get("username"),
        )

        self.solicitation_repository.create_solicitation(model=new_solicitation)

        return new_solicitation

    def run_solicitation(self):
        system = self._get_application()
        actions = self._get_actions(system.id)

        return system, actions

    def _get_application(self):
        application = self.application_repository.get_application(Application, field=self.payload.get("application"))

        if not application:
            raise Exception

        return application

    def _get_actions(self, application_id):
        return [item.name for item in self.functionaties_repository.get_funcionalities_by_application_id(
            Functionality, application_id) if item.name in self.payload.get("actions")]
