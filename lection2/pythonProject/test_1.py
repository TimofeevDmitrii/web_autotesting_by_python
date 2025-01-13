import yaml
from selenium_module_crossbrowse import Site

with open("test_data_crossbrowse.yaml") as conf_f:
    data_yaml = yaml.safe_load(conf_f)


site = Site(data_yaml["base_web_address"])

css_selector = "span.mdc-text-field__ripple"
print(site.get_element_property("css", css_selector, "height"))

xpath_selector = '//*[@id="login"]/div[3]/button/div'
print(site.get_element_property("xpath", xpath_selector, "color"))


def test_wrong_login_data():
    x_selector1 = """//*[@id="login"]/div[1]/label/input"""
    input_login = site.find_element("xpath", x_selector1)
    input_login.send_keys("test")

    x_selector2 = """//*[@id="login"]/div[2]/label/input"""
    input_passwd = site.find_element("xpath", x_selector2)
    input_passwd.send_keys("test123")

    x_btn_selector3 = """//*[@id="login"]/div[3]/button"""
    btn = site.find_element("xpath", x_btn_selector3)
    btn.click()

    x_401_selector = """//*[@id="app"]/main/div/div/div[2]/h2"""
    elem_401 = site.find_element("xpath", x_401_selector)
    assert elem_401.text == "401"