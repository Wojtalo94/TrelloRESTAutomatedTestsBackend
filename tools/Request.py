import requests


class Request():
    def __init__(self):
        self._urls = {""}
                      
    
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
        
