from api.service.postgres import AbstractRepository


class SolicitationRepository(AbstractRepository):
    def get_solicitations(self, model, field):
        return self.session.query(model).order_by()
