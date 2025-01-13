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
def data_for_new_post():
    post_title = ''.join(random.choices(string.ascii_letters + string.digits, k=10))
    post_description = ''.join(random.choices(string.ascii_letters + string.digits, k=30))
    post_content = ''.join(random.choices(string.ascii_letters + string.digits, k=100))
    return post_title, post_description, post_content





