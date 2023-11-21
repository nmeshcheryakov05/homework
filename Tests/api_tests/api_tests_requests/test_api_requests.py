from Tests.test_base import TestBase
import pytest


class TestApiRequests(TestBase):

    def test_request_assign_cancel(self):
        login = self.APP.group_data.users['user1']['log']
        password = self.APP.group_data.users['user1']['pass']
        description = f"API Test request {self.APP.time.get_date_time_for_sql_increased_x_days()}"
        self.APP.api_token.get_token(login, password)
        body = {
            "Department": {"id": 38},
            "Category": {"id": 489},
            "RequestType": {"id": 2552},
            "JobType": {"id": 13728},
            "Description": description,
            "Approvers": [
                {"id": 179904},
                {"id": 179903}
            ]
        }
        response = self.APP.api_requests.post_requests(body)
        requestid = response['Id']
        lastmodifieddate = response['LastModifiedDate']
        login = self.APP.group_data.users['boss1']['log']
        password = self.APP.group_data.users['boss1']['pass']
        self.APP.api_token.get_token(login, password)
        body = {
            "lastModifiedDate": lastmodifieddate,
            "bidAction": 2
        }
        response = self.APP.api_requests.put_requests_id(body, requestid)
        lastmodifieddate = response['LastModifiedDate']
        login = self.APP.group_data.users['boss2']['log']
        password = self.APP.group_data.users['boss2']['pass']
        self.APP.api_token.get_token(login, password)
        body = {
            "lastModifiedDate": lastmodifieddate,
            "bidAction": 3
        }
        response = self.APP.api_requests.put_requests_id(body, requestid)
        #firstapproverstatus = response['userStatus']
        #secondapproverstatus = response['userStatus']

        #assert firstapproverstatus ==
        #assert secondapproverstatus ==
        assert response['Status'] == 5
        print()

    def test_request_cancel_assign(self):
        login = self.APP.group_data.users['user1']['log']
        password = self.APP.group_data.users['user1']['pass']
        description = f"API Test request {self.APP.time.get_date_time_for_sql_increased_x_days()}"
        self.APP.api_token.get_token(login, password)
        body = {
            "Department": {"id": 38},
            "Category": {"id": 489},
            "RequestType": {"id": 2552},
            "JobType": {"id": 13728},
            "Description": description,
            "Approvers": [
                {"id": 179904},
                {"id": 179903}
            ]
        }
        response = self.APP.api_requests.post_requests(body)
        requestid = response['Id']
        lastmodifieddate = response['LastModifiedDate']
        login = self.APP.group_data.users['boss1']['log']
        password = self.APP.group_data.users['boss1']['pass']
        self.APP.api_token.get_token(login, password)
        body = {
            "lastModifiedDate": lastmodifieddate,
            "bidAction": 3
        }
        response = self.APP.api_requests.put_requests_id(body, requestid)
        lastmodifieddate = response['LastModifiedDate']
        login = self.APP.group_data.users['boss2']['log']
        password = self.APP.group_data.users['boss2']['pass']
        self.APP.api_token.get_token(login, password)
        body = {
            "lastModifiedDate": lastmodifieddate,
            "bidAction": 2
        }
        response = self.APP.api_requests.put_requests_id(body, requestid)
        # firstapproverstatus = response['userStatus']
        # secondapproverstatus = response['userStatus']

        # assert firstapproverstatus ==
        # assert secondapproverstatus ==
        assert response['Status'] == 6

    def test_user_rates_user(self):
        login = self.APP.group_data.users['user1']['log']
        password = self.APP.group_data.users['user1']['pass']
        description = f"API Test request {self.APP.time.get_date_time_for_sql_increased_x_days()}"
        self.APP.api_token.get_token(login, password)
        body = {
            "Department": {"id": 38},
            "Category": {"id": 489},
            "RequestType": {"id": 2552},
            "JobType": {"id": 13728},
            "Description": description,
            "Approvers": [
                {"id": 179904},
                {"id": 179903}
            ]
        }
        response = self.APP.api_requests.post_requests(body)
        requestid = response['Id']
        lastmodifieddate = response['LastModifiedDate']
        login = self.APP.group_data.users['user3']['log']
        password = self.APP.group_data.users['user3']['pass']
        self.APP.api_token.get_token(login, password)
        body = {
            "lastModifiedDate": lastmodifieddate,
            "bidAction": 9
        }
        response = self.APP.api_requests.put_requests_id(body, requestid)
        lastmodifieddate = response['LastModifiedDate']
        body = {
            "lastModifiedDate": lastmodifieddate,
            "bidAction": 5
        }
        response = self.APP.api_requests.put_requests_id(body, requestid)
        lastmodifieddate = response['LastModifiedDate']
        login = self.APP.group_data.users['user1']['log']
        password = self.APP.group_data.users['user1']['pass']
        self.APP.api_token.get_token(login, password)
        body = {
            "lastModifiedDate": lastmodifieddate,
            "bidAction": 7,
            "rating": 4
        }
        response = self.APP.api_requests.put_requests_id(body, requestid)

        assert response['Status'] == 9
        