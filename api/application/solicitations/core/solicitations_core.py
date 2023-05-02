import time

from api.application.solicitations.repository.solicitations_repository import SolicitationRepository
from api.application.solicitations.repository.users_repository import UserRepository
from api.orm.tables import Solicitation, User


class SolicitationCore:
    def __init__(self, payload):
        self.payload = payload
        self.solicitation_repository = SolicitationRepository()
        self.user_repository = UserRepository()

    def get_all_solicitation(self):
        return self.solicitation_repository.get_all(model=Solicitation)

    def create_solicitation(self):
        time.sleep(10)
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
