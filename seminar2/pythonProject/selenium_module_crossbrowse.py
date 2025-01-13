import yaml
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager

with open("./test_data_crossbrowse.yaml") as conf_f:
    data_yaml = yaml.safe_load(conf_f)

browser = data_yaml["browser"]

class Site:
    def __init__(self, web_address):
        if browser == 'firefox':
            service = Service(executable_path=GeckoDriverManager().install())
            options = webdriver.FirefoxOptions()
            self.driver = webdriver.Firefox(service=service, options=options)
        elif browser == 'chrome':
            service = Service(executable_path=ChromeDriverManager().install())
            options = webdriver.ChromeOptions()
            self.driver = webdriver.Chrome(service=service, options=options)
        self.driver.implicitly_wait(data_yaml["wait"])
        self.driver.maximize_window()
        self.driver.get(web_address)
        time.sleep(data_yaml["sleep_time"])


    def find_element(self, mode, path):
        if mode == "css":
            element = self.driver.find_element(By.CSS_SELECTOR, path)
        elif mode == "xpath":
            element = self.driver.find_element(By.XPATH, path)
        else:
            element = None
        return element


    def get_element_property(self, mode, path, property):
        element = self.find_element(mode, path)
        return element.value_of_css_property(property)


    def close(self):
        self.driver.close()