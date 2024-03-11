from tools.config import MAX_WAIT
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait


class BasePage():
    _log_in = (By.CSS_SELECTOR, "a[data-uuid*='login']")
    _email = (By.CSS_SELECTOR, "")

    def __init__(self, driver):
        self.ec = ec
        self.wait = WebDriverWait(driver, MAX_WAIT)

    def click_log_in_button(self):
        log_in_button = self.wait.until(self.ec.element_to_be_clickable(self._log_in))
        log_in_button.click()
        return self
    
    def fill_email(self, email):
        self.find_element(self._email).send_keys(email)
        return self
    