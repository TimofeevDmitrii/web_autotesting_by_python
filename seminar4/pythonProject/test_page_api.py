from BaseAppAPI import BaseAPI
import logging

class OperationHelperAPI(BaseAPI):

    def login(self, user_login=None, user_password=None):
        login_data = {"username": user_login, "password": user_password}
        logging.debug(f"Send Request POST {self.url}")
        response = self.send_post_request(data=login_data)
        if response is None:
            logging.error(f"Send Request POST {self.url}")
            return None
        results = None
        try:
            results = response.json(), response.status_code
        except():
            logging.exception("Parse response exception")
        return results

    def get_not_user_posts(self, auth_token=None, owner="notMe", sort=None, order=None, page=None):
        headers = {"X-Auth-Token": auth_token}
        params = {"owner": owner, "sort": sort, "order": order, "page":page}
        logging.debug(f"Send Request GET {self.url}")
        response = self.send_get_request(headers=headers, params=params)
        if response is None:
            logging.error(f"Send Request GET {self.url}")
            return None
        results = None
        try:
            results = response.json(), response.status_code
        except():
            logging.exception("Parse response exception")
        return results

    def get_user_posts(self, auth_token=None, sort=None, order=None, page=None):
        headers = {"X-Auth-Token": auth_token}
        params = {"sort": sort, "order": order, "page":page}
        logging.debug(f"Send Request GET {self.url}")
        response = self.send_get_request(headers=headers, params=params)
        if response is None:
            logging.error(f"Send Request GET {self.url}")
            return None
        results = None
        try:
            results = response.json(), response.status_code
        except():
            logging.exception("Parse response exception")
        return results

    def create_new_post(self, auth_token=None, post_title=None, post_description=None, post_content=None,
                        post_image=None, post_is_draft=None, post_delay_publish_to=None):
        data_post = {"title": post_title, 'description': post_description, "content": post_content,
                     "image": post_image, "isDraft": post_is_draft, "delayPublishTo": post_delay_publish_to}
        headers = {"X-Auth-Token": auth_token}
        logging.debug(f"Send Request POST {self.url}")
        response = self.send_post_request(headers=headers, data=data_post)
        if response is None:
            logging.error(f"Send Request POST {self.url}")
            return None
        results = None
        try:
            results = response.json(), response.status_code
        except():
            logging.exception("Parse response exception")
        return results


