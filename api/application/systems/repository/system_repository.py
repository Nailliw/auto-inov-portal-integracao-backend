from api.service.postgres import AbstractRepository


class SystemRepository(AbstractRepository):
    def get_systems(self, model, field):
        return self.session.query(model).order_by(field)