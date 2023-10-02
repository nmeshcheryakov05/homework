import time
from Tests.test_base import TestBase


class TestMain(TestBase):

    def test_assign_request_to_yourself(self):
        # логинимся 1м пользователем
        self.APP.web_main.login_test_user1()
        # создаем заявку
        self.APP.create_new_request.create_new_request_with_sample()
        # записываем номер заявки
        request = self.APP.edit_request.get_request_number()
        # выходим с текущего пользователя
        self.APP.web_main.logout()
        # логинимся 1м боссом
        self.APP.web_main.login_test_boss1()
        # прямой переход в созданную заявку
        self.APP.any_page.go_to_request(request)
        # назначение заявки на себя
        self.APP.edit_request.assign_request_to_yourself()
        time.sleep(1)
        # проверка исполнителя заявки
        assert self.APP.edit_request.get_contractor() == 'Boss1 Test'