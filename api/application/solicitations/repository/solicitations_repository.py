from api.orm.tables import Solicitation
from api.service.postgres import AbstractRepository


class SolicitationRepository(AbstractRepository):
    def get_solicitations(self, model, field):
        return self.session.query(model).order_by()

    def create_solicitation(self, model):
        self.session.add(model)
        self.session.commit()

    def update_task_id_solicitation(self, solicitation_id, task_id):
        self.session.query(Solicitation).filter(Solicitation.id == solicitation_id).update({"task_id": task_id})
