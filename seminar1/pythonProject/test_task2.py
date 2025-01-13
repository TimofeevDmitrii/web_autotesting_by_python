import requests
import yaml
import json
from pprint import pprint

with open("config.yaml") as conf_f:
    data_yaml = yaml.safe_load(conf_f)

def test_title_in_posts_list(get_auth_token_login, post_title):
    headers = {"X-Auth-Token": get_auth_token_login}
    params = {"owner": "notMe"}
    resp = requests.get(data_yaml["url_posts"], headers=headers, params=params)
    pprint(json.loads(resp.text))
    resp_json = resp.json()
    assert post_title in [post['title'] for post in resp_json['data']]


def test_create_new_post(get_auth_token_login, create_new_post):
    headers = {"X-Auth-Token": get_auth_token_login}
    resp = requests.get(data_yaml["url_posts"], headers=headers)
    pprint(json.loads(resp.text))
    resp_json = resp.json()
    print("post title now created: " + create_new_post[0])
    assert create_new_post[1] in [post["description"] for post in resp_json["data"]]