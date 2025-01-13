import requests
import logging

class BaseAPI:

    def __init__(self, url):
        self.url = url


    def send_get_request(self, headers=None, params=None):
        response = None
        try:
            response = requests.get(self.url, headers=headers, params=params)
        except():
            logging.exception("Send GET request exception")
        return response

    def send_post_request(self, headers=None, data=None):
        response = None
        try:
            response = requests.post(self.url, headers=headers, data=data)
        except():
            logging.exception("Send POST request exception")
        return response






