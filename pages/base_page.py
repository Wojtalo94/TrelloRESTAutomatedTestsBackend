from tools.config import MAX_WAIT
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait


class BasePage():
    _log_in = (By.CSS_SELECTOR, "a[data-uuid*='login']")
    _email = (By.CSS_SELECTOR, "input[id='username']")
    _submit_login = (By.CSS_SELECTOR, "button[id='login-submit']")
    _password = (By.CSS_SELECTOR, "input[id='password']")
    _without_two_step_verification = (By.CSS_SELECTOR, "button[id='mfa-promote-continue']")
    _main_page = (By.CSS_SELECTOR, "h3[class='boards-page-section-header-name']")

    def __init__(self, driver):
        self.driver = driver
        self.ec = ec
        self.wait = WebDriverWait(driver, MAX_WAIT)

    def click_log_in_button(self):
        self.wait.until(self.ec.element_to_be_clickable(self._log_in)).click()
        return self
    
    def fill_email(self, email):
        self.wait.until(self.ec.visibility_of_element_located(self._email))
        self.driver.find_element(*self._email).send_keys(email)
        return self
    
    def click_submit_login(self):
        self.wait.until(self.ec.element_to_be_clickable(self._submit_login)).click()
        return self
    
    def fill_password(self, password):
        self.wait.until(self.ec.visibility_of_element_located(self._password))
        self.driver.find_element(*self._password).send_keys(password)
        return self
    
    def click_without_two_step_verification(self):
        self.wait.until(self.ec.element_to_be_clickable(self._without_two_step_verification)).click()
        return self
    
    def wait_for_main_page(self):
        self.wait.until(self.ec.visibility_of_element_located(self._main_page))
        return self

    
