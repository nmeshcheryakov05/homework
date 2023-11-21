
from FW.api.api_base import ApiBase


class Requests(ApiBase):

    def put_requests_id(self, body, id, params=None):
        return self.requests_PUT(self.get_base_url() + f'/Requests/{id}/Action', body, params)
    def get_requests(self, params=None):
        return self.requests_GET(self.get_base_url() + '/Requests', params=params)

    def post_requests(self, body, params=None):
        return self.requests_POST(self.get_base_url() + '/Requests', body, params=params)

    def get_requests_id(self, id, params=None):
        return self.requests_GET(self.get_base_url() + f'/Requests/{id}', params=params)

    def delete_requests_id_sub_requests_id(self, id, sub_request_id, params=None):
        return self.requests_DELETE(self.get_base_url() + f'/Requests/{id}/SubRequests/{sub_request_id}', params=params)

