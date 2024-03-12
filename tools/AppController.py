import logging
from .Request import Request
from pages.base_page import BasePage
from tools.AppLogAnalyzer import AppLogAnalyzer


class AppController():
    def __init__(self, driver):
        self._logger = logging.getLogger("AppController")
        self.driver = driver
        self._request = Request()
        self._base_page = BasePage(driver)
        self._AppLogAnalyzer = AppLogAnalyzer(driver)


    def log_in(self):
        self._base_page.click_log_in_button().fill_email("wojtalo222@gmail.com").click_submit_login()
        self._base_page.fill_password("sumara290").click_submit_login().wait_for_main_page()
        



    # https://testuj.pl/blog/testowanie-aplikacji-rest-przy-uzyciu-postmana/

    # https://trello.com/u/wojtalo222/boards
    # email: wojtalo222@gmail.com