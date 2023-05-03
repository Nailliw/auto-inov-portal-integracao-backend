from api.service.postgres import AbstractRepository


class FunctionalityRepository(AbstractRepository):
    def create_functionality(self, model):
        self.session.add(model)
        self.session.commit()

    def get_functionality(self, model, field):
        return self.session.query(model).filter_by(application_id=field).first()

    def get_funcionalities_by_application_id(self, model, field):
        return self.session.query(model).filter_by(application_id=field).all()