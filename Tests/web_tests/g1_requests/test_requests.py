from Tests.pre_conditions import PreConditions
import time


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
        self.APP.edit_request.save_request()
        firstcoordinator = self.APP.edit_request.get_coordinator_status(self.APP.group_data.users_id['boss1']['id'])
        self.APP.login.logout()
        self.APP.login.g1_login_log_pas(self.APP.group_data.users['boss2']['log'], self.APP.group_data.
                                        users['boss2']['pass'])
        self.APP.any_page.go_to_request_with_request_number(request)
        self.APP.edit_request.cancel_request()
        self.APP.edit_request.save_request()
        secondcoordinator = self.APP.edit_request.get_coordinator_status(self.APP.group_data.users_id['boss2']['id'])

        assert self.APP.edit_request.get_request_status() == 'Отклонена'
        assert 'Согласовано' in firstcoordinator
        assert 'Отклонено' in secondcoordinator

    def test_request_cancel_assign(self):
        self.APP.any_page.open_main_page()
        self.APP.login.g1_login_log_pas()
        self.APP.any_page.go_to_requests()
        self.APP.request_list.create_new_default_request()
        self.APP.create_request.gandiva_test_department_choose()
        self.APP.create_request.software_category_choose()
        self.APP.create_request.test_type_choose()
        self.APP.create_request.test_job_type_choose()
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
        self.APP.edit_request.save_request()
        firstcoordinator = self.APP.edit_request.get_coordinator_status(self.APP.group_data.users_id['boss1']['id'])
        self.APP.login.logout()
        self.APP.login.g1_login_log_pas(self.APP.group_data.users['boss2']['log'], self.APP.group_data.
                                        users['boss2']['pass'])
        self.APP.any_page.go_to_request_with_request_number(request)
        self.APP.edit_request.approve_request_to_yourself()
        self.APP.edit_request.save_request()
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
        self.APP.create_request.test_type_choose()
        self.APP.create_request.test_job_type_choose()
        self.APP.create_request.test_description()
        self.APP.edit_request.save_request()
        request = self.APP.edit_request.get_request_number()
        self.APP.login.logout()
        self.APP.login.g1_login_log_pas(self.APP.group_data.users['user3']['log'],
                                        self.APP.group_data.users['user3']['pass'])
        self.APP.any_page.go_to_request_with_request_number(request)
        self.APP.edit_request.assign_request_to_yourself()
        self.APP.edit_request.save_request()
        self.APP.edit_request.transfer_to_examination()
        self.APP.edit_request.save_request()
        self.APP.login.logout()
        self.APP.login.g1_login_log_pas()
        self.APP.any_page.go_to_request_with_request_number(request)
        self.APP.edit_request.give_grade_to_work(4)
        self.APP.edit_request.save_request()
