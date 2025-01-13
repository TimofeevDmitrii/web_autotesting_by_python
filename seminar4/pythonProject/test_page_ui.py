from BaseAppUI import BasePage
from selenium.webdriver.common.by import By
import logging
import yaml

class TestSearchLocators:
    with open("./locators.yaml") as l_f:
        locators = yaml.safe_load(l_f)

    ids = dict()
    for locator in locators["xpath"].keys():
        ids[locator] = (By.XPATH, locators["xpath"][locator])
    for locator in locators["css"].keys():
        ids[locator] = (By.CSS_SELECTOR, locators["css"][locator])


class OperationsHelperUI(BasePage):

    def enter_text_into_field(self, locator, text, description=None):
        if description:
            element_name = description
        else:
            element_name = locator
        logging.debug(f"Send '{text}' to element {element_name}")
        field = self.find_element(locator)
        if not field:
            logging.error(f"Element not found: {element_name})")
            return False
        try:
            field.clear()
            field.send_keys(text)
        except():
            logging.exception(f"Send '{text}' to '{element_name}' exception")
            return False
        return True


    def click_element(self, locator, description=None):
        if description:
            element_name = description
        else:
            element_name = locator
        element = self.find_element(locator)
        if not element:
            logging.error(f"Element not found: {element_name})")
            return False
        try:
            element.click()
        except():
            logging.exception(f"Click '{element_name}' exception")
            return False
        logging.debug(f"Clicked '{element_name}'")
        return True


    def get_text_from_element(self, locator, description=None):
        if description:
            element_name = description
        else:
            element_name = locator
        element = self.find_element(locator)
        if not element:
            logging.error(f"Element not found: {element_name})")
            return None
        try:
            text = element.text
        except():
            logging.exception(f"Get text from '{element_name}' exception")
            return None
        logging.debug(f"Got '{text}' from '{element_name}'")
        return text

    #Enter text methods

    def enter_login(self, user_login):
        self.enter_text_into_field(TestSearchLocators.ids["LOCATOR_LOGIN_FIELD"], user_login, "user_login_field")


    def enter_password(self, user_password):
        self.enter_text_into_field(TestSearchLocators.ids["LOCATOR_PASSWORD_FIELD"], user_password,
                                   "user_password_field")


    def enter_post_title(self, title):
        self.enter_text_into_field(TestSearchLocators.ids["LOCATOR_POST_TITLE_FIELD"], title, "post_title_field")


    def enter_post_description(self, description):
        self.enter_text_into_field(TestSearchLocators.ids["LOCATOR_POST_DESCRIPTION_FIELD"], description,
                                   "post_description_field")


    def enter_post_content(self, content):
        self.enter_text_into_field(TestSearchLocators.ids["LOCATOR_POST_CONTENT_FIELD"], content,
                                   "post_content_field")


    def enter_contact_us_name(self, name):
        self.enter_text_into_field(TestSearchLocators.ids["LOCATOR_CONTACT_US_NAME_FIELD"], name,
                                   "contact_us_name_field")


    def enter_contact_us_email(self, email):
        self.enter_text_into_field(TestSearchLocators.ids["LOCATOR_CONTACT_US_EMAIL_FIELD"], email,
                                   "contact_us_email_field")


    def enter_contact_us_content(self, content):
        self.enter_text_into_field(TestSearchLocators.ids["LOCATOR_CONTACT_US_CONTENT_FIELD"], content,
                                   "contact_us_content_field")


    # CLick element methods

    def click_login_btn(self):
        self.click_element(TestSearchLocators.ids["LOCATOR_LOGIN_BTN"], "login_button")


    def click_create_post_btn(self):
        self.click_element(TestSearchLocators.ids["LOCATOR_CREATE_POST_BTN"], "create_post_button(+)")


    def click_save_post_btn(self):
        self.click_element(TestSearchLocators.ids["LOCATOR_SAVE_POST_BTN"], "save_post_button")


    def click_contact_us_link(self):
        self.click_element(TestSearchLocators.ids["LOCATOR_HEADER_CONTACT_US_LINK"], "contact_us_header_link")


    def click_contact_us_send_btn(self):
        self.click_element(TestSearchLocators.ids["LOCATOR_CONTACT_US_SEND_BTN"], "contact_us_send_btn")

    # Get text methods

    def get_error_login_text(self):
        return self.get_text_from_element(TestSearchLocators.ids["LOCATOR_ERR_LOGIN_MESS"],
                                          "error_field_under_login")

    def get_hello_user_text(self):
        return self.get_text_from_element(TestSearchLocators.ids["LOCATOR_HEADER_HELLO_USER_BTN"],
                                          "hello_user_header_btn")


    def get_post_own_page_title_text(self):
        return self.get_text_from_element(TestSearchLocators.ids["LOCATOR_POST_OWN_PAGE_TITLE"],
                                          "post's_own_page_title")

    def get_contact_us_title_text(self):
        return self.get_text_from_element(TestSearchLocators.ids["LOCATOR_CONTACT_US_TITLE"], "contact_us_page_title")

    def get_alert(self):
        logging.info("Get alert text")
        text = self.get_alert_text()
        logging.info(text)
        return text
