from api.application.solicitations.repository.solicitatations_repository import SolicitationRepository
from api.orm.tables import Solicitation


class SolicitationCore:
    def __init__(self, payload):
        self.payload = payload
        self.solicitation_repository = SolicitationRepository()

    def get_all_solicitation(self):
        return self.solicitation_repository.get_all(model=Solicitation)

    def create_solicitation(self):
        new_solicitation = Solicitation(
            user_id=self.payload.get("user_id"),
            username=self.payload.get("username"),
        )
        self.solicitation_repository.create_solicitation(model=new_solicitation)
        return True
