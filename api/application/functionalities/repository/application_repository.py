from api.service.postgres import AbstractRepository


class ApplicationRepository(AbstractRepository):
    def create_application(self, model):
        self.session.add(model)
        self.session.commit()

    def get_application(self, model, field):
        return self.session.query(model).filter_by(name=field).first()
