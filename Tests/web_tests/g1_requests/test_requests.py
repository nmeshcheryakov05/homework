from Tests.pre_conditions import PreConditions


class TestRequests(PreConditions):

    def test_request_assign_cancel(self):
        self.APP.any_page.open_main_page()
        self.APP.login.g1_login_log_pas()
        self.APP.any_page.go_to_requests()
        self.APP.request_list.create_new_default_request()
        self.APP.create_request.gandiva_test_department_choose()
        self.APP.create_request.software_category_choose()
        self.APP.create_request.ms_gandiva_type_choose()
        self.APP.create_request.test_type_one_job_type_choose()
        self.APP.create_request.test_description()
        for result in range(2):
            result += 1
            self.APP.create_request.add_coordinator('boss', result)
        self.APP.edit_request.save_request()
        request = self.APP.edit_request.get_request_number()
        self.APP.login.logout()
        self.APP.login.g1_login_log_pas(self.APP.group_data.users['boss1']['log'], self.APP.group_data.
                                        users['boss1']['pass'])
        self.APP.any_page.go_to_request_with_request_number(request)
        self.APP.edit_request.approve_request_to_yourself()
        firstapproover = self.APP.edit_request.get_coordinator_status(self.APP.group_data.users_id['boss1']['id'])
        self.APP.login.logout()
        self.APP.login.g1_login_log_pas(self.APP.group_data.users['boss2']['log'], self.APP.group_data.
                                        users['boss2']['pass'])
        self.APP.any_page.go_to_request_with_request_number(request)
        self.APP.edit_request.cancel_request()
        secondapproover = self.APP.edit_request.get_coordinator_status(self.APP.group_data.users_id['boss2']['id'])

        assert self.APP.edit_request.get_request_status() == 'Отклонена'
        assert 'Согласовано' in firstapproover
        assert 'Отклонено' in secondapproover

    def test_request_cancel_assign(self):
        self.APP.any_page.open_main_page()
        self.APP.login.g1_login_log_pas()
        self.APP.any_page.go_to_requests()
        self.APP.request_list.create_new_default_request()
        self.APP.create_request.gandiva_test_department_choose()
        self.APP.create_request.software_category_choose()
        self.APP.create_request.ms_gandiva_type_choose()
        self.APP.create_request.test_type_one_job_type_choose()
        self.APP.create_request.test_description()
        for result in range(2):
            result += 1
            self.APP.create_request.add_coordinator('boss', result)
        self.APP.edit_request.save_request()
        request = self.APP.edit_request.get_request_number()
        self.APP.login.logout()
        self.APP.login.g1_login_log_pas(self.APP.group_data.users['boss1']['log'], self.APP.group_data.
                                        users['boss1']['pass'])
        self.APP.any_page.go_to_request_with_request_number(request)
        self.APP.edit_request.cancel_request()
        firstcoordinator = self.APP.edit_request.get_coordinator_status(self.APP.group_data.users_id['boss1']['id'])
        self.APP.login.logout()
        self.APP.login.g1_login_log_pas(self.APP.group_data.users['boss2']['log'], self.APP.group_data.
                                        users['boss2']['pass'])
        self.APP.any_page.go_to_request_with_request_number(request)
        self.APP.edit_request.approve_request_to_yourself()
        secondcoordinator = self.APP.edit_request.get_coordinator_status(self.APP.group_data.users_id['boss2']['id'])

        assert self.APP.edit_request.get_request_status() == 'В работе'
        assert 'Отклонено' in firstcoordinator
        assert 'Согласовано' in secondcoordinator

    def test_user_rates_user(self):
        self.APP.any_page.open_main_page()
        self.APP.login.g1_login_log_pas()
        self.APP.any_page.go_to_requests()
        self.APP.request_list.create_new_default_request()
        self.APP.create_request.gandiva_test_department_choose()
        self.APP.create_request.software_category_choose()
        self.APP.create_request.ms_gandiva_type_choose()
        self.APP.create_request.test_type_one_job_type_choose()
        self.APP.create_request.test_description()
        self.APP.edit_request.save_request()
        firstassign = self.APP.edit_request.presence_of_a_button(self.APP.group_data.buttons_web['assignToSelf'])
        request = self.APP.edit_request.get_request_number()
        self.APP.login.logout()
        self.APP.login.g1_login_log_pas(self.APP.group_data.users['user3']['log'],
                                        self.APP.group_data.users['user3']['pass'])
        self.APP.any_page.go_to_request_with_request_number(request)
        secondassign = self.APP.edit_request.presence_of_a_button(self.APP.group_data.buttons_web['assignToSelf'])
        self.APP.edit_request.assign_request_to_yourself()
        self.APP.edit_request.save_request()
        secondexamination = self.APP.edit_request.presence_of_a_button(self.APP.group_data.buttons_web['toExamination'])
        self.APP.edit_request.transfer_to_examination()
        self.APP.edit_request.save_request()
        secondtowork = self.APP.edit_request.presence_of_a_button(self.APP.group_data.buttons_web['toWork'])
        self.APP.login.logout()
        self.APP.login.g1_login_log_pas()
        self.APP.any_page.go_to_request_with_request_number(request)
        firsttowork = self.APP.edit_request.presence_of_a_button(self.APP.group_data.buttons_web['toWork'])
        self.APP.edit_request.give_grade_to_work(4)
        self.APP.edit_request.save_request()

        assert self.APP.edit_request.get_request_status() == 'Закрыта'
        assert firstassign
        assert firsttowork
        assert secondassign
        assert secondexamination
        assert secondtowork
