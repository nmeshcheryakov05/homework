from Tests.test_base import TestBase
import pytest
import allure


@allure.epic('G1')
@allure.feature('API')
@allure.story('Проверки заявок API')
class TestApiRequests(TestBase):

    @allure.title('Тест на добавление двух согласующих, первый согласует, второй отклоняет заявку')
    def test_request_approvers_assign_cancel(self):
        # Присваивание логина и пароля User1
        login = self.APP.group_data.users['user1']['log']
        password = self.APP.group_data.users['user1']['pass']
        # Запись времени текущего ПК
        description = f"API Test request {self.APP.time.get_date_time_for_sql_increased_x_days()}"
        # Получение токена
        self.APP.api_token.get_token(login, password)
        # Тело запроса
        body = {
            "Department": {"Id": 38},
            "Category": {"Id": 489},
            "RequestType": {"Id": 2552},
            "JobType": {"Id": 13728},
            "Description": description,
            "Approvers": [
                {"Id": 179904,
                 "IsUserAdded": True},
                {"Id": 179903,
                 "IsUserAdded": True}
            ]
        }
        # Выполнение запроса и запись его копии в переменную
        response = self.APP.api_requests.post_requests(body)
        # Получение номера заявки
        requestid = response['Id']
        # Получение времени последнего изменения заявки
        lastmodifieddate = response['LastModifiedDate']
        # Присваивание логина и пароля Boss1
        login = self.APP.group_data.users['boss1']['log']
        password = self.APP.group_data.users['boss1']['pass']
        # Получение токена
        self.APP.api_token.get_token(login, password)
        # Тело запроса
        body = {
            "lastModifiedDate": lastmodifieddate,
            "bidAction": 2
        }
        # Выполнение запроса и запись его копии в переменную
        response = self.APP.api_requests.put_requests_id(body, requestid)
        # Получение времени последнего изменения заявки
        lastmodifieddate = response['LastModifiedDate']
        # Присваивание логина и пароля Boss2
        login = self.APP.group_data.users['boss2']['log']
        password = self.APP.group_data.users['boss2']['pass']
        # Получение токена
        self.APP.api_token.get_token(login, password)
        # Тело запроса
        body = {
            "LastModifiedDate": lastmodifieddate,
            "BidAction": 3
        }
        # Выполнение запроса и запись его копии в переменную
        response = self.APP.api_requests.put_requests_id(body, requestid)
        # Получение статусов согласующих
        firstapproverstatus = self.APP.api_requests.get_approver_status('Boss1', response)
        secondapproverstatus = self.APP.api_requests.get_approver_status('Boss2', response)

        # Проверяем статусы согласующих и заявки
        assert firstapproverstatus == 3
        assert secondapproverstatus == 4
        assert response['Status'] == 5

    @allure.title('Тест на добавление двух согласующих, первый отклоняет, второй согласует заявку')
    def test_request_approvers_cancel_assign(self):
        # Присваиваение логина и пароля User1
        login = self.APP.group_data.users['user1']['log']
        password = self.APP.group_data.users['user1']['pass']
        # Получение времени текущего ПК
        description = f"API Test request {self.APP.time.get_date_time_for_sql_increased_x_days()}"
        # Получение токена
        self.APP.api_token.get_token(login, password)
        # Тело запроса
        body = {
            "Department": {"id": 38},
            "Category": {"id": 489},
            "RequestType": {"id": 2552},
            "JobType": {"id": 13728},
            "Description": description,
            "Approvers": [
                {"Id": 179904,
                 "IsUserAdded": True},
                {"Id": 179903,
                 "IsUserAdded": True}
            ]
        }
        # Выполнение запроса и запись его копии в переменную
        response = self.APP.api_requests.post_requests(body)
        # Получение номера заявки
        requestid = response['Id']
        # Получение времени последнего изменения заявки
        lastmodifieddate = response['LastModifiedDate']
        # Присваивание логина и пароля Boss1
        login = self.APP.group_data.users['boss1']['log']
        password = self.APP.group_data.users['boss1']['pass']
        # Получение токена
        self.APP.api_token.get_token(login, password)
        # Тело запроса
        body = {
            "LastModifiedDate": lastmodifieddate,
            "BidAction": 3
        }
        # Выполнение запроса и запись его копии в переменную
        response = self.APP.api_requests.put_requests_id(body, requestid)
        # Получение времени последнего изменения заявки
        lastmodifieddate = response['LastModifiedDate']
        # Присваивание логина и пароля Boss2
        login = self.APP.group_data.users['boss2']['log']
        password = self.APP.group_data.users['boss2']['pass']
        # Получение токена
        self.APP.api_token.get_token(login, password)
        # Тело запроса
        body = {
            "LastModifiedDate": lastmodifieddate,
            "BidAction": 2
        }
        # Выполнение запроса и запись его копии в переменную
        response = self.APP.api_requests.put_requests_id(body, requestid)
        # Получение статусов согласующих
        firstapproverstatus = self.APP.api_requests.get_approver_status('Boss1', response)
        secondapproverstatus = self.APP.api_requests.get_approver_status('Boss2', response)

        # Проверяем статусы согласующих и заявки
        assert firstapproverstatus == 4
        assert secondapproverstatus == 3
        assert response['Status'] == 6

    @allure.title('Тест на взятие заявки на себя с последующей сдачей и оценкой работы инициатором')
    def test_user_rates_request_user(self):
        # Присваивание логина и пароля User1
        login = self.APP.group_data.users['user1']['log']
        password = self.APP.group_data.users['user1']['pass']
        # Получение времени текущего ПК
        description = f"API Test request {self.APP.time.get_date_time_for_sql_increased_x_days()}"
        # Получение токена
        self.APP.api_token.get_token(login, password)
        # Тело запроса
        body = {
            "Department": {"id": 38},
            "Category": {"id": 489},
            "RequestType": {"id": 2552},
            "JobType": {"id": 13728},
            "Description": description
        }
        # Выполнение запроса и запись его копии в переменную
        response = self.APP.api_requests.post_requests(body)
        # Получение номера заявки
        requestid = response['Id']
        # Получение времени последнего изменения заявки
        lastmodifieddate = response['LastModifiedDate']
        # Присваивание логина и пароля User3
        login = self.APP.group_data.users['user3']['log']
        password = self.APP.group_data.users['user3']['pass']
        # Получение токена
        self.APP.api_token.get_token(login, password)
        # Тело запроса
        body = {
            "LastModifiedDate": lastmodifieddate,
            "BidAction": 9
        }
        # Выполнение запроса и запись его копии в переменную
        response = self.APP.api_requests.put_requests_id(body, requestid)
        # Получение времени последнего изменения заявки
        lastmodifieddate = response['LastModifiedDate']
        # Тело запроса
        body = {
            "LastModifiedDate": lastmodifieddate,
            "BidAction": 5
        }
        # Выполнение запроса и запись его копии в переменную
        response = self.APP.api_requests.put_requests_id(body, requestid)
        # Получение времени последнего изменения заявки
        lastmodifieddate = response['LastModifiedDate']
        # Присваивание логина и пароля User1
        login = self.APP.group_data.users['user1']['log']
        password = self.APP.group_data.users['user1']['pass']
        # Получение токена
        self.APP.api_token.get_token(login, password)
        # Тело запроса
        body = {
            "LastModifiedDate": lastmodifieddate,
            "BidAction": 7,
            "description": "test",
            "Rating": 4
        }
        # Выполнение запроса и запись его копии в переменную
        response = self.APP.api_requests.put_requests_id(body, requestid)

        # Проверяем статус заявки
        assert response['Status'] == 9
        