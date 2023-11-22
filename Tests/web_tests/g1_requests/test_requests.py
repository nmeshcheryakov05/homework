from Tests.pre_conditions import PreConditions
import allure


@allure.epic('G1')
@allure.feature('WEB')
@allure.story('Проверки заявок WEB')
class TestRequests(PreConditions):

    @allure.title('Тест на добавление двух согласующих, первый согласует, второй отклоняет заявку')
    def test_request_approvers_assign_cancel(self):
        # Открытие главной страницы
        self.APP.any_page.open_main_page()
        # Авторизация User1
        self.APP.login.g1_login_log_pas()
        # Переход к заявкам
        self.APP.any_page.go_to_requests()
        # Клик по кнопке создания новой заявки
        self.APP.request_list.create_new_default_request()
        # Выбор норматива "Тестовый_Тип_1"
        self.APP.create_request.gandiva_test_department_choose()
        self.APP.create_request.software_category_choose()
        self.APP.create_request.ms_gandiva_type_choose()
        self.APP.create_request.test_type_one_job_type_choose()
        # Создание описания
        self.APP.create_request.test_description()
        # Добавление согласующих
        for result in range(2):
            result += 1
            self.APP.create_request.add_coordinator('boss', result)
        # Сохранение заявки
        self.APP.edit_request.save_request()
        # Получение номера заявки
        request = self.APP.edit_request.get_request_number()
        # Выход с текущего пользователя
        self.APP.login.logout()
        # Авторизация Boss1
        self.APP.login.g1_login_log_pas(self.APP.group_data.users['boss1']['log'], self.APP.group_data.
                                        users['boss1']['pass'])
        # Прямой переход к заявке
        self.APP.any_page.go_to_request_with_request_number(request)
        # Согласование заявки
        self.APP.edit_request.approve_request_to_yourself()
        # Получение статуса первого согласующего
        firstapproover = self.APP.edit_request.get_coordinator_status(self.APP.group_data.users_id['boss1']['id'])
        # Выход с текущего пользователя
        self.APP.login.logout()
        # Авторизация Boss2
        self.APP.login.g1_login_log_pas(self.APP.group_data.users['boss2']['log'], self.APP.group_data.
                                        users['boss2']['pass'])
        # Прямой переход к заявке
        self.APP.any_page.go_to_request_with_request_number(request)
        # Отклонение заявки
        self.APP.edit_request.cancel_request()
        # Получение статуса второго согласующего
        secondapproover = self.APP.edit_request.get_coordinator_status(self.APP.group_data.users_id['boss2']['id'])

        # Проверяем статусы согласующих и заявки
        assert self.APP.edit_request.get_request_status() == 'Отклонена'
        assert 'Согласовано' in firstapproover
        assert 'Отклонено' in secondapproover

    @allure.title('Тест на добавление двух согласующих, первый отклоняет, второй согласует заявку')
    def test_request_approvers_cancel_assign(self):
        # Открытие главной страницы
        self.APP.any_page.open_main_page()
        # Авторизация User1
        self.APP.login.g1_login_log_pas()
        # Переход к заявкам
        self.APP.any_page.go_to_requests()
        # Клик по кнопке создания заявки
        self.APP.request_list.create_new_default_request()
        # Выбор норматива "Тестовый_Тип_1"
        self.APP.create_request.gandiva_test_department_choose()
        self.APP.create_request.software_category_choose()
        self.APP.create_request.ms_gandiva_type_choose()
        self.APP.create_request.test_type_one_job_type_choose()
        # Создание описания
        self.APP.create_request.test_description()
        # Добавление согласующих
        for result in range(2):
            result += 1
            self.APP.create_request.add_coordinator('boss', result)
        # Сохранение заявки
        self.APP.edit_request.save_request()
        # Получение номера заявки
        request = self.APP.edit_request.get_request_number()
        # Выход с текущего пользователя
        self.APP.login.logout()
        # Авторизация Boss1
        self.APP.login.g1_login_log_pas(self.APP.group_data.users['boss1']['log'], self.APP.group_data.
                                        users['boss1']['pass'])
        # Прямой переход к заявке
        self.APP.any_page.go_to_request_with_request_number(request)
        # Отклонение заявки
        self.APP.edit_request.cancel_request()
        # Получение статуса первого согласующего
        firstcoordinator = self.APP.edit_request.get_coordinator_status(self.APP.group_data.users_id['boss1']['id'])
        # Выход с текущего пользователя
        self.APP.login.logout()
        # Авторизация Boss2
        self.APP.login.g1_login_log_pas(self.APP.group_data.users['boss2']['log'], self.APP.group_data.
                                        users['boss2']['pass'])
        # Прямой переход к заявке
        self.APP.any_page.go_to_request_with_request_number(request)
        # Согласование заявки
        self.APP.edit_request.approve_request_to_yourself()
        # Получение статуса второго согласующего
        secondcoordinator = self.APP.edit_request.get_coordinator_status(self.APP.group_data.users_id['boss2']['id'])

        # Проверяем статусы согласующих и заявки
        assert self.APP.edit_request.get_request_status() == 'В работе'
        assert 'Отклонено' in firstcoordinator
        assert 'Согласовано' in secondcoordinator

    @allure.title('Тест на взятие заявки на себя с последующей сдачей и оценкой работы инициатором')
    def test_user_rates_request_user(self):
        # Открытие главной страницы
        self.APP.any_page.open_main_page()
        # Авторизация User1
        self.APP.login.g1_login_log_pas()
        # Переход к заявкам
        self.APP.any_page.go_to_requests()
        # Клик по кнопке создания заявки
        self.APP.request_list.create_new_default_request()
        # Выбор норматива "Тестовый_Тип_1"
        self.APP.create_request.gandiva_test_department_choose()
        self.APP.create_request.software_category_choose()
        self.APP.create_request.ms_gandiva_type_choose()
        self.APP.create_request.test_type_one_job_type_choose()
        # Создание описания
        self.APP.create_request.test_description()
        # Сохранение заявки
        self.APP.edit_request.save_request()
        # Проверка наличия кнопки "Назначить на себя" у User1
        firstassign = self.APP.edit_request.presence_of_a_button(self.APP.group_data.buttons_web['assignToSelf'])
        # Получение номера заявки
        request = self.APP.edit_request.get_request_number()
        # Выход с текущего пользователя
        self.APP.login.logout()
        # Авторизация User3
        self.APP.login.g1_login_log_pas(self.APP.group_data.users['user3']['log'],
                                        self.APP.group_data.users['user3']['pass'])
        # Прямой переход к заявке
        self.APP.any_page.go_to_request_with_request_number(request)
        # Проверка наличия кнопки "Назначить на себя" у User3
        secondassign = self.APP.edit_request.presence_of_a_button(self.APP.group_data.buttons_web['assignToSelf'])
        # Назначение заявки на себя
        self.APP.edit_request.assign_request_to_yourself()
        # Сохранение заявки
        self.APP.edit_request.save_request()
        # Проверка наличия кнопки "На проверку" у User3
        secondexamination = self.APP.edit_request.presence_of_a_button(self.APP.group_data.buttons_web['toExamination'])
        # Перевод заявки на проверку
        self.APP.edit_request.transfer_to_examination()
        # Сохранение заявки
        self.APP.edit_request.save_request()
        # Проверка наличия кнопки "В работу" у User3
        secondtowork = self.APP.edit_request.presence_of_a_button(self.APP.group_data.buttons_web['toWork'])
        # Выход с текущего пользователя
        self.APP.login.logout()
        # Авторизация User1
        self.APP.login.g1_login_log_pas()
        # Прямой переход к заявке
        self.APP.any_page.go_to_request_with_request_number(request)
        # Проверка наличия кнопки "На доработку" у User1
        firsttowork = self.APP.edit_request.presence_of_a_button(self.APP.group_data.buttons_web['toWork'])
        # Оценка работы на 4 и добавление комментария
        self.APP.edit_request.give_grade_to_work(4)
        # Сохранение заявки
        self.APP.edit_request.save_request()

        # Проверяем статус заявки и наличие кнопок
        assert self.APP.edit_request.get_request_status() == 'Закрыта'
        assert firstassign
        assert firsttowork
        assert secondassign
        assert secondexamination
        assert secondtowork
