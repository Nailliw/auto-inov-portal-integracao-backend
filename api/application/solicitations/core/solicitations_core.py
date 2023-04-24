from api.application.solicitations.repository.solicitatations_repository import SolicitationRepository


class SolicitationCore:
    def __init__(self, payload):
        self.payload = payload
        self.solicitation_repository = SolicitationRepository()

    def get_all_solicitation(self):
        return []
        # return self.solicitation_repository.get_solicitations(Solicitations)

    def create_solicitation(self):
        return True