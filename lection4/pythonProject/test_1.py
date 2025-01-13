from test_page import OperationsHelper
import logging
import yaml
import time

with open ("test_data.yaml") as conf_f:
    data_yaml = yaml.safe_load(conf_f)


def test_wrong_login_data(browser_driver):
    logging.info("test_wrong_login_data is starting...")
    test_page = OperationsHelper(browser_driver)
    test_page.go_to_site()
    test_page.enter_login("test")
    test_page.enter_password("test123")
    test_page.click_login_btn()
    assert test_page.get_error_login_text() == "401"


def test_successful_login(browser_driver):
    logging.info("test_successful_login is starting...")
    test_page = OperationsHelper(browser_driver)
    test_page.enter_login(data_yaml["user_name"])
    test_page.enter_password(data_yaml["passwd"])
    test_page.click_login_btn()
    assert test_page.get_hello_user_text() == "Hello, {}".format(data_yaml["user_name"]), "test_successful_login FAILED"


def test_create_post(browser_driver, data_for_new_post):
    logging.info("test_create_post is starting...")
    test_page = OperationsHelper(browser_driver)

    test_page.click_create_post_btn()
    test_page.enter_post_title(data_for_new_post[0])
    test_page.enter_post_description(data_for_new_post[1])
    test_page.enter_post_content(data_for_new_post[2])
    test_page.click_save_post_btn()
    time.sleep(5)

    print("new post title: " + data_for_new_post[0])

    assert test_page.get_post_own_page_title_text() == data_for_new_post[0], "test_create_post FAILED"


def test_contact_us(browser_driver):
    logging.info("test_contact_us is starting...")
    results = []

    test_page = OperationsHelper(browser_driver)
    test_page.click_contact_us_link()
    time.sleep(3)
    results.append(test_page.get_contact_us_title_text() == "Contact us!")

    test_page.enter_contact_us_name("user_auto_test123")
    test_page.enter_contact_us_email("user_auto@test.com")
    test_page.enter_contact_us_content("Put here something.....")
    test_page.click_contact_us_send_btn()
    time.sleep(5)
    results.append(test_page.get_alert() == "Form successfully submitted")

    assert all(results), "test_contact_us FAILED"
