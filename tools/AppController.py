import logging
from .Request import Request


class AppController:
    def __init__(self):
        self._logger = logging.getLogger("GameController")
        self._request = Request()


    def log_in(self):
        pass
    # https://testuj.pl/blog/testowanie-aplikacji-rest-przy-uzyciu-postmana/

    # https://trello.com/u/wojtalo222/boards
    # email: wojtalo222@gmail.com