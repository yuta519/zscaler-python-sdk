import configparser
import json
import time

import requests
from requests.models import Response

from zscaler_python_sdk.lib import admin
from zscaler_python_sdk.lib import auth


class Zia(object):
    def __init__(self, config_path: str) -> None:
        config = configparser.ConfigParser()
        config.read(config_path)
        zia = config["zia"]
        self.cloud_name = zia["HOSTNAME"]
        self.base_url = f"https://admin.{self.cloud_name}/api/v1"
        self.api_key = zia["APIKEY"]
        self.admin_user = zia["USERNAME"]
        self.admin_password = zia["PASSWORD"]

    def fetch_admin_users(self, search_query: str = None) -> list[str]:
        api_token: str = auth.login(
            self.base_url, self.admin_user, self.admin_password, self.api_key
        )
        admin_users = admin.fetch_adminusers(api_token, self.base_url, search_query)
        auth.logout(api_token, self.base_url)
        return admin_users

    def fetch_admin_roles(self) -> list[str]:
        api_token: str = auth.login(
            self.base_url, self.admin_user, self.admin_password, self.api_key
        )
        admin_roles = admin.fetch_adminroles(api_token, self.base_url)
        auth.logout(api_token, self.base_url)
        return admin_roles

    def create_admin_users(
        self, login_name, user_name, email, password, role
    ) -> list[str]:
        api_token: str = auth.login(
            self.base_url, self.admin_user, self.admin_password, self.api_key
        )
        result = admin.create_adminuser(
            api_token, self.base_url, login_name, user_name, email, password, role
        )
        auth.logout(api_token, self.base_url)
        return result
