import yaml
from selenium_module import Site

with open("test_data.yaml") as conf_f:
    data_yaml = yaml.safe_load(conf_f)

site = Site(data_yaml["base_web_address"])

css_selector = "span.mdc-text-field__ripple"
print(site.get_element_property("css", css_selector, "height"))

xpath_selector = '//*[@id="login"]/div[3]/button/div'
print(site.get_element_property("xpath", xpath_selector, "color"))