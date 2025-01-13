import pytest
import yaml
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
import random
import string

with open("./test_data.yaml") as conf_f:
    data_yaml = yaml.safe_load(conf_f)

browser_type = data_yaml["browser"]


@pytest.fixture(scope="session")
def browser_driver():
    if browser_type == 'firefox':
        service = Service(executable_path=GeckoDriverManager().install())
        options = webdriver.FirefoxOptions()
        driver = webdriver.Firefox(service=service, options=options)
    else:
        service = Service(executable_path=ChromeDriverManager().install())
        options = webdriver.ChromeOptions()
        driver = webdriver.Chrome(service=service, options=options)
    yield driver
    driver.quit()


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





