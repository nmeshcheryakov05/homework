from Tests.test_base import TestBase
import pytest

class TestWorkNormative(TestBase):

    def test_search_normative_info(self):
        params = {
            "phrase": "Тестовый_Тип_1",
            "size": 20,
            "page": 1
        }
        response = self.APP.api_work_normative.work_normative_search(params)
        print()
