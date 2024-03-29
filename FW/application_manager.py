from Data.group_data import GroupData
from FW.api.g1_requests.requests import Requests
from FW.api.token import Token
from FW.api.work_normative.work_normative import WorkNormative
from FW.web.account.login import Login
from FW.web.any_page import AnyPage
from FW.web.driver_Instance import DriverInstance
from FW.web.requests.create_request import CreateRequest
from FW.web.requests.edit_request import EditRequest
from FW.web.requests.request_list import RequestList
from FW.work_with_time import WorkWithTime


class ApplicationManager:
    group_data = GroupData

    def __init__(self):
        self.driver_instance = DriverInstance()

        self.any_page = AnyPage(self)
        self.api_token = Token(self)
        self.api_requests = Requests(self)
        self.api_work_normative = WorkNormative(self)
        self.time = WorkWithTime()
        self.login = Login(self)
        self.create_request = CreateRequest(self)
        self.edit_request = EditRequest(self)
        self.request_list = RequestList(self)
