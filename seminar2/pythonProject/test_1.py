import yaml
from selenium_module_crossbrowse import Site
import time

with open("test_data_crossbrowse.yaml") as conf_f:
    data_yaml = yaml.safe_load(conf_f)


site = Site(data_yaml["base_web_address"])

# css_selector = "span.mdc-text-field__ripple"
# print(site.get_element_property("css", css_selector, "height"))
#
# xpath_selector = '//*[@id="login"]/div[3]/button/div'
# print(site.get_element_property("xpath", xpath_selector, "color"))


def test_wrong_login_data(login_field_selector, password_field_selector, login_btn_selector,
                          error_elem_selector, expected_result_wrong_auth):

    input_login = site.find_element(login_field_selector[0], login_field_selector[1])
    input_login.clear()
    input_login.send_keys("test")

    input_passwd = site.find_element(password_field_selector[0], password_field_selector[1])
    input_passwd.clear()
    input_passwd.send_keys("test123")

    btn = site.find_element(login_btn_selector[0], login_btn_selector[1])
    btn.click()

    err_elem = site.find_element(error_elem_selector[0], error_elem_selector[1])

    try:
        assert err_elem.text == expected_result_wrong_auth, "test_wrong_login_data FAILED"
    finally:
        site.close()


def test_successful_login(login_field_selector, password_field_selector, login_btn_selector,
                          header_hello_user_link, expected_result_successful_auth):

    input_login = site.find_element(login_field_selector[0], login_field_selector[1])
    input_login.clear()
    input_login.send_keys(data_yaml["user_name"])

    input_passwd = site.find_element(password_field_selector[0], password_field_selector[1])
    input_passwd.clear()
    input_passwd.send_keys(data_yaml["passwd"])

    btn = site.find_element(login_btn_selector[0], login_btn_selector[1])
    btn.click()

    hello_link = site.find_element(header_hello_user_link[0], header_hello_user_link[1])
    text_link = hello_link.text
    site.close()

    assert text_link == expected_result_successful_auth, "test_successful_login FAILED"


def test_create_post(login_field_selector, password_field_selector, login_btn_selector,
                     header_hello_user_link, expected_result_successful_auth, create_post_btn,
                     post_title_field_selector, post_description_field_selector,
                     post_content_field_selector, save_post_btn, post_own_page_title_selector,
                     data_for_new_post
                     ):
    results = []

    input_login = site.find_element(login_field_selector[0], login_field_selector[1])
    input_login.clear()
    input_login.send_keys(data_yaml["user_name"])

    input_passwd = site.find_element(password_field_selector[0], password_field_selector[1])
    input_passwd.clear()
    input_passwd.send_keys(data_yaml["passwd"])

    btn = site.find_element(login_btn_selector[0], login_btn_selector[1])
    btn.click()

    hello_link = site.find_element(header_hello_user_link[0], header_hello_user_link[1])
    text_link = hello_link.text

    results.append(text_link == expected_result_successful_auth)



    add_new_post_btn = site.find_element(create_post_btn[0], create_post_btn[1])
    add_new_post_btn.click()
    time.sleep(data_yaml["sleep_time"])

    title_field = site.find_element(post_title_field_selector[0], post_title_field_selector[1])
    title_field.clear()
    title_field.send_keys(data_for_new_post[0])
    time.sleep(data_yaml["sleep_time"])

    descr_field = site.find_element(post_description_field_selector[0], post_description_field_selector[1])
    descr_field.clear()
    descr_field.send_keys(data_for_new_post[1])
    time.sleep(data_yaml["sleep_time"])

    content_field = site.find_element(post_content_field_selector[0], post_content_field_selector[1])
    content_field.clear()
    content_field.send_keys(data_for_new_post[2])
    time.sleep(data_yaml["sleep_time"])

    save_btn = site.find_element(save_post_btn[0], save_post_btn[1])
    save_btn.click()
    time.sleep(data_yaml["sleep_time"]+9)

    title_own_page = site.find_element(post_own_page_title_selector[0], post_own_page_title_selector[1])
    text_title = title_own_page.text
    time.sleep(data_yaml["sleep_time"])
    site.close()

    results.append(text_title == data_for_new_post[0])
    print("new post title: " + data_for_new_post[0])

    assert all(results), "test_create_post FAILED"

