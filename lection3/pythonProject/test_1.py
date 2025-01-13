from test_page import OperationsHelper
import logging

def test_wrong_login_data(browser_driver):
    logging.info("test_wrong_login_data starting...")
    test_page = OperationsHelper(browser_driver)
    test_page.go_to_site()
    test_page.enter_login("test")
    test_page.enter_password("test123")
    test_page.click_login_btn()
    assert test_page.get_error_text() == "401"


# def test_successful_login(login_field_selector, password_field_selector, login_btn_selector,
#                           header_hello_user_link, expected_result_successful_auth):
#
#     input_login = site.find_element(login_field_selector[0], login_field_selector[1])
#     input_login.clear()
#     input_login.send_keys(data_yaml["user_name"])
#
#     input_passwd = site.find_element(password_field_selector[0], password_field_selector[1])
#     input_passwd.clear()
#     input_passwd.send_keys(data_yaml["passwd"])
#
#     btn = site.find_element(login_btn_selector[0], login_btn_selector[1])
#     btn.click()
#
#     hello_link = site.find_element(header_hello_user_link[0], header_hello_user_link[1])
#     text_link = hello_link.text
#     site.close()
#
#     assert text_link == expected_result_successful_auth, "test_successful_login FAILED"
#
#
# def test_create_post(login_field_selector, password_field_selector, login_btn_selector,
#                      header_hello_user_link, expected_result_successful_auth, create_post_btn,
#                      post_title_field_selector, post_description_field_selector,
#                      post_content_field_selector, save_post_btn, post_own_page_title_selector,
#                      data_for_new_post
#                      ):
#     results = []
#
#     input_login = site.find_element(login_field_selector[0], login_field_selector[1])
#     input_login.clear()
#     input_login.send_keys(data_yaml["user_name"])
#
#     input_passwd = site.find_element(password_field_selector[0], password_field_selector[1])
#     input_passwd.clear()
#     input_passwd.send_keys(data_yaml["passwd"])
#
#     btn = site.find_element(login_btn_selector[0], login_btn_selector[1])
#     btn.click()
#
#     hello_link = site.find_element(header_hello_user_link[0], header_hello_user_link[1])
#     text_link = hello_link.text
#
#     results.append(text_link == expected_result_successful_auth)
#
#
#
#     add_new_post_btn = site.find_element(create_post_btn[0], create_post_btn[1])
#     add_new_post_btn.click()
#     time.sleep(data_yaml["sleep_time"])
#
#     title_field = site.find_element(post_title_field_selector[0], post_title_field_selector[1])
#     title_field.clear()
#     title_field.send_keys(data_for_new_post[0])
#     time.sleep(data_yaml["sleep_time"])
#
#     descr_field = site.find_element(post_description_field_selector[0], post_description_field_selector[1])
#     descr_field.clear()
#     descr_field.send_keys(data_for_new_post[1])
#     time.sleep(data_yaml["sleep_time"])
#
#     content_field = site.find_element(post_content_field_selector[0], post_content_field_selector[1])
#     content_field.clear()
#     content_field.send_keys(data_for_new_post[2])
#     time.sleep(data_yaml["sleep_time"])
#
#     save_btn = site.find_element(save_post_btn[0], save_post_btn[1])
#     save_btn.click()
#     time.sleep(data_yaml["sleep_time"]+9)
#
#     title_own_page = site.find_element(post_own_page_title_selector[0], post_own_page_title_selector[1])
#     text_title = title_own_page.text
#     time.sleep(data_yaml["sleep_time"])
#     site.close()
#
#     results.append(text_title == data_for_new_post[0])
#     print("new post title: " + data_for_new_post[0])
#
#     assert all(results), "test_create_post FAILED"

