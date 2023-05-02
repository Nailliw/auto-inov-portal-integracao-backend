from api.orm.tables import User
from api.service.postgres import AbstractRepository


class UserRepository(AbstractRepository):
    def create_user(self, model):
        self.session.add(model)
        self.session.commit()

    def get_user_by_id(self, user_id):
        return self.session.query(User).filter(User.id == user_id)
