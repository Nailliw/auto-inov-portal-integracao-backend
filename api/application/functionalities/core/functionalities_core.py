import datetime

from api.application.functionalities.repository.application_repository import ApplicationRepository
from api.application.functionalities.repository.functionality_repository import FunctionalityRepository
from api.orm.tables import Application, Functionality
from api.utils.ssh_connection import SSH


class FunctionalitiesCore:
    def __init__(self, payload):
        self.ssh = None
        self.functionality_repository = FunctionalityRepository()
        self.application_repository = ApplicationRepository()
        self.payload = payload

    def verify_status(self):
        applications = self.application_repository.get_all(Application)
        lista = []

        for app in applications:
            lista.append(self.verify_system_status(ip=app.ip, system_name=app.name))
        return lista

    def verify_system_status(self, ip, system_name):
        date_now = datetime.datetime.now().strftime("%m/%d/%Y, %H:%M:%S")
        self.ssh = SSH(hostname=ip, username='p686199', password='WH0riZ0N')

        return {"name": "system_name", "status": True, "date": date_now}



    def verify_status_sinep(self, _id):
        func = self.functionality_repository.get_functionality(model=Functionality, field=_id)
        if func:
            return True
        else:
            return False

    def verify_status_atm(self):
        return False

    def perform_recycling(self):
        application = self.application_repository.get_application(model=Application, field="SINEP")

        if not application:
            raise Exception

        return self.execute_recycling(application.name)

    def execute_recycling(self, name):
        return "Executando Reciglagem do " + name
