from BaseApp import BasePage
from selenium.webdriver.common.by import By
import logging

class TestSearchLocators:

    LOCATOR_LOGIN_FIELD = (By.XPATH, """//*[@id="login"]/div[1]/label/input""")
    LOCATOR_PASSWORD_FIELD = (By.XPATH, """//*[@id="login"]/div[2]/label/input""")
    LOCATOR_LOGIN_BTN = (By.CSS_SELECTOR, """button""")
    LOCATOR_ERR_MESS = (By.XPATH, """//*[@id="app"]/main/div/div/div[2]/h2""")

class OperationsHelper(BasePage):
    def enter_login(self, user_login):
        logging.info(f"Send {user_login} to element {TestSearchLocators.LOCATOR_LOGIN_FIELD[1]}")
        login_field = self.find_element(TestSearchLocators.LOCATOR_LOGIN_FIELD)
        login_field.clear()
        login_field.send_keys(user_login)


    def enter_password(self, user_password):
        logging.info(f"Send {user_password} to element {TestSearchLocators.LOCATOR_PASSWORD_FIELD[1]}")
        passwd_field = self.find_element(TestSearchLocators.LOCATOR_PASSWORD_FIELD)
        passwd_field.clear()
        passwd_field.send_keys(user_password)


    def click_login_btn(self):
        logging.info("Click login button")
        login_btn = self.find_element(TestSearchLocators.LOCATOR_LOGIN_BTN)
        login_btn.click()


    def get_error_text(self):
        error_field = self.find_element(TestSearchLocators.LOCATOR_ERR_MESS)
        text = error_field.text
        logging.info(f"Get {error_field.text} in error field {TestSearchLocators.LOCATOR_ERR_MESS[1]}")
        return text