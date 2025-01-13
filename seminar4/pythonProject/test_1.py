from test_page_ui import OperationsHelperUI
from test_page_api import OperationHelperAPI
import logging
import yaml
import time

with open ("test_data.yaml") as conf_f:
    data_yaml = yaml.safe_load(conf_f)

class TestAPI:
    def test_api_login_successful(self):
        logging.info("test_api_login_successful is starting...")
        test_api = OperationHelperAPI(data_yaml["api_url_login"])
        result = test_api.login(data_yaml["user_name"], data_yaml["passwd"])
        assert type(result[0]["token"]) == str and result[1] == 200, "test_api_login_successful FAILED"

    def test_api_wrong_login(self):
        logging.info("test_api_wrong_login is starting...")
        test_api = OperationHelperAPI(data_yaml["api_url_login"])
        result = test_api.login("random_user", "test123456")
        assert result[0]["error"] == "Invalid credentials." and result[1] == 401, "test_api_wrong_login FAILED"

    def test_api_create_new_post(self, get_auth_token_login, data_for_new_post):
        logging.info("test_api_create_new_post is starting...")
        test_api = OperationHelperAPI(data_yaml["api_url_posts"])
        result_create = test_api.create_new_post(auth_token=get_auth_token_login, post_title=data_for_new_post[0],
                                                 post_description=data_for_new_post[1], post_content=data_for_new_post[2])
        get_posts = test_api.get_user_posts(auth_token=get_auth_token_login)
        test_results = [result_create[0]["title"] == data_for_new_post[0],
                        result_create[1] == 200,
                        data_for_new_post[1] in [post["description"] for post in get_posts[0]["data"]]
                        ]
        assert all(test_results), "test_api_create_new_post FAILED"

    def test_api_title_in_posts_list(self, get_auth_token_login, get_the_oldest_post_title):
        logging.info("test_api_title_in_posts_list is starting...")
        test_api = OperationHelperAPI(data_yaml["api_url_posts"])
        result = test_api.get_not_user_posts(auth_token=get_auth_token_login, order="ASC")
        assert get_the_oldest_post_title in [post['title'] for post in result[0]['data']] and result[1] == 200,\
            "test_api_title_in_posts_list FAILED"

    def test_api_get_posts_no_token_header(self):
        logging.info("test_api_get_posts_no_token_header is starting...")
        test_api = OperationHelperAPI(data_yaml["api_url_posts"])
        result = test_api.get_user_posts()
        assert result[0]["message"] == 'Auth header required X-Auth-Token' and result[1] == 401,\
            "test_api_get_posts_no_token_header FAILED"



class TestUI:
    def test_ui_wrong_login_data(self, browser_driver):
        logging.info("test_ui_wrong_login_data is starting...")
        test_page = OperationsHelperUI(browser_driver)
        test_page.go_to_site()
        test_page.enter_login("test")
        test_page.enter_password("test123")
        test_page.click_login_btn()
        assert test_page.get_error_login_text() == "401", "test_ui_wrong_login_data is FAILED"


    def test_ui_successful_login(self, browser_driver):
        logging.info("test_ui_successful_login is starting...")
        test_page = OperationsHelperUI(browser_driver)
        test_page.enter_login(data_yaml["user_name"])
        test_page.enter_password(data_yaml["passwd"])
        test_page.click_login_btn()
        assert test_page.get_hello_user_text() == "Hello, {}".format(data_yaml["user_name"]),\
            "test_ui_successful_login FAILED"


    def test_ui_create_post(self, browser_driver, data_for_new_post):
        logging.info("test_ui_create_post is starting...")
        test_page = OperationsHelperUI(browser_driver)

        test_page.click_create_post_btn()
        test_page.enter_post_title(data_for_new_post[0])
        test_page.enter_post_description(data_for_new_post[1])
        test_page.enter_post_content(data_for_new_post[2])
        test_page.click_save_post_btn()
        time.sleep(5)

        assert test_page.get_post_own_page_title_text() == data_for_new_post[0], "test_ui_create_post FAILED"


    def test_ui_contact_us(self, browser_driver):
        logging.info("test_ui_contact_us is starting...")
        results = []

        test_page = OperationsHelperUI(browser_driver)
        test_page.click_contact_us_link()
        time.sleep(3)
        results.append(test_page.get_contact_us_title_text() == "Contact us!")

        test_page.enter_contact_us_name("user_auto_test123")
        test_page.enter_contact_us_email("user_auto@test.com")
        test_page.enter_contact_us_content("Put here something.....")
        test_page.click_contact_us_send_btn()
        time.sleep(5)
        results.append(test_page.get_alert() == "Form successfully submitted")

        assert all(results), "test_ui_contact_us FAILED"
