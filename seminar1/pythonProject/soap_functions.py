from zeep import Client, Settings
import yaml

with open("config.yaml") as conf_f:
    data_yaml = yaml.safe_load(conf_f)

client = Client(wsdl=data_yaml["wsdl"], settings=Settings(strict=False))

def checkText_method(text, lang="ru", options=0, format="plain"):
    return client.service.checkText(text, lang, options, format)
