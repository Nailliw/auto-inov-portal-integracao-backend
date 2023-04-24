import datetime

from api.application.functionalities.repository.application_repository import ApplicationRepository
from api.application.functionalities.repository.functionality_repository import FunctionalityRepository
from api.orm.tables import Application, Functionality


class FunctionalitiesCore:
    def __init__(self, payload):
        self.functionality_repository = FunctionalityRepository()
        self.application_repository = ApplicationRepository()
        self.payload = payload

    def verify_status(self):
        applications = self.application_repository.get_all(Application)
        lista = []
        date_now = datetime.datetime.now().strftime("%m/%d/%Y, %H:%M:%S")
        for app in applications:
            if app.name == "SINEP":
                status_sinep = self.verify_status_sinep(app.id)
                lista.append({"name": "SINEP", "status": status_sinep, "date": date_now})

            if app.name == "SIOPI":
                status_atm = self.verify_status_atm()
                lista.append({"name": "SIOPI", "status": status_atm, "date": date_now})

            if app.name == "SICTD":
                status_atm = self.verify_status_atm()
                lista.append({"name": "SICTD", "status": status_atm, "date": date_now})

        return lista

    def verify_status_sinep(self, _id):
        func = self.functionality_repository.get_functionality(model=Functionality, field=_id)
        if func:
            return True
        else:
            return False

    def verify_status_atm(self):
        return False

    def perform_recycling(self):
        application = self.application_repository.get_application(model=Application,
                                                                  field="SINEP")

        if not application:
            raise Exception

        # func = [item.name for item in application.functionalities if item.name == self.payload.get("functionality")]
        #
        # if not func:
        #     raise Exception
        return self.execute_recycling(application.name)

    def execute_recycling(self, name):
        return "Executando Reciglagem do " + name
