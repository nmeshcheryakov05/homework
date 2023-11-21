from FW.api.api_base import ApiBase


class WorkNormative(ApiBase):
    def work_normative_search(self, params=None):
        return self.requests_GET(self.get_base_url() + '/workNormative/Search', params=params)
