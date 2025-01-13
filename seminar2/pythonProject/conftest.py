import pytest
import yaml
import random
import string


with open("test_data_crossbrowse.yaml") as conf_f:
    data_yaml = yaml.safe_load(conf_f)


@pytest.fixture()
def login_field_selector():
    return "xpath", """//*[@id="login"]/div[1]/label/input"""


@pytest.fixture()
def password_field_selector():
    return "xpath", """//*[@id="login"]/div[2]/label/input"""


@pytest.fixture()
def login_btn_selector():
    return "css", """button"""


@pytest.fixture()
def error_elem_selector():
    return "xpath", """//*[@id="app"]/main/div/div/div[2]/h2"""


@pytest.fixture()
def expected_result_wrong_auth():
    return "401"






@pytest.fixture()
def header_hello_user_link():
    return "xpath", """//*[@id="app"]/main/nav/ul/li[3]/a"""


@pytest.fixture()
def expected_result_successful_auth():
    return "Hello, {}".format(data_yaml["user_name"])





@pytest.fixture()
def create_post_btn():
    # return "css", """#create-btn"""
    return "xpath", """//*[@id="create-btn"]"""

@pytest.fixture()
def post_title_field_selector():
    return "xpath", """//*[@id="create-item"]/div/div/div[1]/div/label/input"""


@pytest.fixture()
def post_description_field_selector():
    return "xpath", """//*[@id="create-item"]/div/div/div[2]/div/label/span/textarea"""


@pytest.fixture()
def post_content_field_selector():
    return "xpath", """//*[@id="create-item"]/div/div/div[3]/div/label/span/textarea"""

@pytest.fixture()
def save_post_btn():
    return "xpath", """//*[@id="create-item"]/div/div/div[7]/div/button"""



@pytest.fixture()
def post_own_page_title_selector():
    return "xpath", """//*[@id="app"]/main/div/div[1]/h1"""

@pytest.fixture()
def data_for_new_post():
    post_title = ''.join(random.choices(string.ascii_letters + string.digits, k=10))
    post_description = ''.join(random.choices(string.ascii_letters + string.digits, k=30))
    post_content = ''.join(random.choices(string.ascii_letters + string.digits, k=100))
    return post_title, post_description, post_content





