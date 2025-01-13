from BaseApp import BasePage
from selenium.webdriver.common.by import By
import logging

class TestSearchLocators:

    LOCATOR_LOGIN_FIELD = (By.XPATH, """//*[@id="login"]/div[1]/label/input""")
    LOCATOR_PASSWORD_FIELD = (By.XPATH, """//*[@id="login"]/div[2]/label/input""")
    LOCATOR_LOGIN_BTN = (By.CSS_SELECTOR, """button""")
    LOCATOR_ERR_LOGIN_MESS = (By.XPATH, """//*[@id="app"]/main/div/div/div[2]/h2""")
    LOCATOR_HEADER_HELLO_USER_BTN = (By.XPATH, """//*[@id="app"]/main/nav/ul/li[3]/a""")

    LOCATOR_CREATE_POST_BTN = (By.XPATH, """//*[@id="create-btn"]""")
    LOCATOR_SAVE_POST_BTN = (By.XPATH, """//*[@id="create-item"]/div/div/div[7]/div/button""")
    LOCATOR_POST_TITLE_FIELD = (By.XPATH, """//*[@id="create-item"]/div/div/div[1]/div/label/input""")
    LOCATOR_POST_DESCRIPTION_FIELD = (By.XPATH, """//*[@id="create-item"]/div/div/div[2]/div/label/span/textarea""")
    LOCATOR_POST_CONTENT_FIELD = (By.XPATH, """//*[@id="create-item"]/div/div/div[3]/div/label/span/textarea""")
    LOCATOR_POST_OWN_PAGE_TITLE = (By.XPATH, """//*[@id="app"]/main/div/div[1]/h1""")

    LOCATOR_HEADER_CONTACT_US_LINK = (By.XPATH, """//*[@id="app"]/main/nav/ul/li[2]/a""")
    LOCATOR_CONTACT_US_TITLE = (By.XPATH, """//*[@id="app"]/main/div/div/h1""")
    LOCATOR_CONTACT_US_NAME_FIELD = (By.XPATH, """//*[@id="contact"]/div[1]/label/input""")
    LOCATOR_CONTACT_US_EMAIL_FIELD = (By.XPATH, """//*[@id="contact"]/div[2]/label/input""")
    LOCATOR_CONTACT_US_CONTENT_FIELD = (By.XPATH, """//*[@id="contact"]/div[3]/label/span/textarea""")
    LOCATOR_CONTACT_US_SEND_BTN = (By.XPATH, """//*[@id="contact"]/div[4]/button""")


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


    def get_error_login_text(self):
        error_field = self.find_element(TestSearchLocators.LOCATOR_ERR_LOGIN_MESS)
        text = error_field.text
        logging.info(f"Get {text} in error field {TestSearchLocators.LOCATOR_ERR_LOGIN_MESS[1]}")
        return text


    def get_hello_user_text(self):
        hello_btn = self.find_element(TestSearchLocators.LOCATOR_HEADER_HELLO_USER_BTN)
        text = hello_btn.text
        logging.info(f"Get {text} in hello user btn {TestSearchLocators.LOCATOR_HEADER_HELLO_USER_BTN[1]}")
        return text


    def click_create_post_btn(self):
        logging.info("Click create post button")
        create_post_btn = self.find_element(TestSearchLocators.LOCATOR_CREATE_POST_BTN)
        create_post_btn.click()


    def click_save_post_btn(self):
        logging.info("Click save post button")
        save_post_btn = self.find_element(TestSearchLocators.LOCATOR_SAVE_POST_BTN)
        save_post_btn.click()


    def enter_post_title(self, title):
        logging.info(f"Send {title} to element {TestSearchLocators.LOCATOR_POST_TITLE_FIELD[1]}")
        title_field = self.find_element(TestSearchLocators.LOCATOR_POST_TITLE_FIELD)
        title_field.clear()
        title_field.send_keys(title)

    def enter_post_description(self, description):
        logging.info(f"Send {description} to element {TestSearchLocators.LOCATOR_POST_DESCRIPTION_FIELD[1]}")
        description_field = self.find_element(TestSearchLocators.LOCATOR_POST_DESCRIPTION_FIELD)
        description_field.clear()
        description_field.send_keys(description)


    def enter_post_content(self, content):
        logging.info(f"Send {content} to element {TestSearchLocators.LOCATOR_POST_CONTENT_FIELD[1]}")
        content_field = self.find_element(TestSearchLocators.LOCATOR_POST_CONTENT_FIELD)
        content_field.clear()
        content_field.send_keys(content)


    def get_post_own_page_title_text(self):
        title_own_page = self.find_element(TestSearchLocators.LOCATOR_POST_OWN_PAGE_TITLE)
        text = title_own_page.text
        logging.info(f"Get {text} in post's own page title {TestSearchLocators.LOCATOR_POST_OWN_PAGE_TITLE[1]}")
        return text


    def click_contact_us_link(self):
        logging.info("Click contact us link")
        contact_us_link = self.find_element(TestSearchLocators.LOCATOR_HEADER_CONTACT_US_LINK)
        contact_us_link.click()


    def get_contact_us_title_text(self):
        title_contact_us = self.find_element(TestSearchLocators.LOCATOR_CONTACT_US_TITLE)
        text = title_contact_us.text
        logging.info(f"Get {title_contact_us.text} in contact us page title {TestSearchLocators.LOCATOR_CONTACT_US_TITLE[1]}")
        return text


    def enter_contact_us_name(self, name):
        logging.info(f"Send {name} to element {TestSearchLocators.LOCATOR_CONTACT_US_NAME_FIELD[1]}")
        name_field = self.find_element(TestSearchLocators.LOCATOR_CONTACT_US_NAME_FIELD)
        name_field.clear()
        name_field.send_keys(name)


    def enter_contact_us_email(self, email):
        logging.info(f"Send {email} to element {TestSearchLocators.LOCATOR_CONTACT_US_EMAIL_FIELD[1]}")
        email_field = self.find_element(TestSearchLocators.LOCATOR_CONTACT_US_EMAIL_FIELD)
        email_field.clear()
        email_field.send_keys(email)


    def enter_contact_us_content(self, content):
        logging.info(f"Send {content} to element {TestSearchLocators.LOCATOR_CONTACT_US_CONTENT_FIELD[1]}")
        content_field = self.find_element(TestSearchLocators.LOCATOR_CONTACT_US_CONTENT_FIELD)
        content_field.clear()
        content_field.send_keys(content)


    def click_contact_us_send_btn(self):
        logging.info("Click contact us send btn")
        contact_us_btn = self.find_element(TestSearchLocators.LOCATOR_CONTACT_US_SEND_BTN)
        contact_us_btn.click()


    def get_alert_text(self):
        alert = self.driver.switch_to.alert
        text = alert.text
        logging.info(f"Get {text} in contact us page alert")
        return text