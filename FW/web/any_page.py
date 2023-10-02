from FW.web.web_base import WebBase
import time


class AnyPage(WebBase):
    def go_to_request(self, request):
        self.get_driver().get(f'https://web-test-compose.gandiva.ru/Request/Edit/{request}')
        time.sleep(1)