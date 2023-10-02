from FW.web.G1_requests.edit_request import EditRequest
from FW.web.any_page import AnyPage
from FW.web.driver_Instance import DriverInstance
from FW.web.main.main import Main
from FW.web.G1_requests.create_new_request import CreateNewRequest


class ApplicationManager:

    def __init__(self):
        self.driver_instance = DriverInstance()
        self.web_main = Main(self)
        self.create_new_request = CreateNewRequest(self)
        self.edit_request = EditRequest(self)
        self.any_page = AnyPage(self)
