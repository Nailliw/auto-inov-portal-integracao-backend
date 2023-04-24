from api.service.postgres import AbstractRepository


class SolicitationRepository(AbstractRepository):
    def get_solicitations(self, model, field):
        return self.session.query(model).order_by()

    def create_solicitation(self, model):
        try:
            self.session.add(model)
            self.session.commit()
        finally:
            self.session.close()
            return True
