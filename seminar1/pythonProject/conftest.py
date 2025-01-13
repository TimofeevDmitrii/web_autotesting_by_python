import pytest
import yaml
import requests
import string
import random

with open("config.yaml") as conf_f:
    data_yaml = yaml.safe_load(conf_f)

@pytest.fixture()
def word_with_missing_letter():
    return "Мшина", "Машина"


@pytest.fixture()
def word_with_wrong_letter():
    return "Венегрет", "Винегрет"


@pytest.fixture()
def get_auth_token_login():
    data = {"username": data_yaml["user_name"], "password": data_yaml["passwd"]}
    resp_json = requests.post(data_yaml["url_login"], data).json()
    return resp_json["token"]


@pytest.fixture()
def post_title():
    return "Зима"


@pytest.fixture()
def create_new_post():
    post_title = ''.join(random.choices(string.ascii_letters + string.digits, k=10))
    post_description = ''.join(random.choices(string.ascii_letters + string.digits, k=30))
    post_content = ''.join(random.choices(string.ascii_letters + string.digits, k=100))

    data_login = {"username": data_yaml["user_name"], "password": data_yaml["passwd"]}
    token = requests.post(data_yaml["url_login"], data_login).json()["token"]

    data_post = {"title": post_title, 'description': post_description, "content": post_content}
    headers = {"X-Auth-Token": token}
    requests.post(data_yaml["url_posts"], headers=headers, data=data_post)

    return post_title, post_description, post_content


