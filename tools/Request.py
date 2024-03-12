import requests
from tools.user_data import UserData


class Request():
    def __init__(self):
        _user_data = UserData("tools/user_data.csv")
        _api_key = _user_data.get_user_data("TRELLO_API_KEY")
        _api_token = _user_data.get_user_data("TRELLO_API_TOKEN")
        self._urls = {"trello_user": f"https://api.trello.com/1/members/me/?key={_api_key}&token={_api_token}"}
    
    def url(self, name: str):
        if not name in self._urls:
            raise AttributeError(f"Missing {name} in urls list")
        return self._urls[name]

    def _prepare_return(self, response):
        try:
            data = response.json()
        except:
            data = {}
        return data, response.status_code

    def get(self, url: str):
        with requests.Session() as s:
            return self._prepare_return(s.get(url, proxies=None))

    def patch(self, url: str, json: dict):
        with requests.Session() as s:
            return self._prepare_return(s.patch(url, json=json, proxies=None))

    def put(self, url: str, json=None):
        with requests.Session() as s:
            return self._prepare_return(s.put(url, json=json, proxies=None))

    def post(self, url: str, json: dict):
        with requests.Session() as s:
            return self._prepare_return(s.post(url, json=json, proxies=None))

    def delete(self, url: str):
        with requests.Session() as s:
            return self._prepare_return(s.delete(url, proxies=None))
    
    def get_init_id(self):
        response = self.get(self.url("trello_user"))
        return response