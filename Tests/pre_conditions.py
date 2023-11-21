from Tests.test_base import TestBase


class PreConditions(TestBase):

    def setup_class(self):
        pass

    def teardown_class(self):
        self.APP.driver_instance.stop_driver()

    def setup_method(self):
        self.APP.driver_instance.start_driver()
        self.APP.any_page.open_main_page()

    def teardown_method(self):
        self.APP.driver_instance.stop_driver()
