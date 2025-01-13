import yaml
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service

with open("./test_data.yaml") as conf_f:
    data_yaml = yaml.safe_load(conf_f)

service = Service(data_yaml["driver_path"])
options = webdriver.ChromeOptions()

class Site:
    def __init__(self, web_address):
        self.driver = webdriver.Chrome(service=service, options=options)
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