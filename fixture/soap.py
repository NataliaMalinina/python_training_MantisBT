
from suds.client import Client
from suds import WebFault
from models.projects import Projects

class SoapHelper:

    def __init__(self, app):
        self.app = app

    def can_login(self, username, password):
        client = Client(self.app.config['web']['baseUrl'] + "/api/soap/mantisconnect.php?wsdl")
            #"http://localhost/mantisbt-1.2.20/api/soap/mantisconnect.php?wsdl")
        try:
            client.service.mc_login(username, password)
            return True
        except WebFault:
            return False

    def get_list_from_soap(self, username, password):
        client = Client(self.app.config['web']['baseUrl'] + "/api/soap/mantisconnect.php?wsdl")
        try:
            projects = client.service.mc_projects_get_user_accessible(username, password)
            return projects
        except WebFault:
            return False


