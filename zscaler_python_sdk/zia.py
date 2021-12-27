import configparser
from typing import Optional

from zscaler_python_sdk.lib import admin
from zscaler_python_sdk.lib import auth
from zscaler_python_sdk.lib import url_categories


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

    def fetch_url_categories(self, is_custom_only: Optional[str] = None):
        api_token: str = auth.login(
            self.base_url, self.admin_user, self.admin_password, self.api_key
        )
        categories = url_categories.fetch_url_categories(
            api_token, self.base_url, is_custom_only
        )
        auth.logout(api_token, self.base_url)
        return categories

    def lookup_url_category(self, target_urls: list[str]):
        api_token: str = auth.login(
            self.base_url, self.admin_user, self.admin_password, self.api_key
        )
        lookuped_categories = url_categories.lookup_url_classification(
            api_token, self.base_url, target_urls
        )
        return lookuped_categories

    def create_custom_url_category(
        self,
        configured_names: str,
        urls: list[str],
        db_categorized_urls: list[str],
        description: str,
    ):
        api_token: str = auth.login(
            self.base_url, self.admin_user, self.admin_password, self.api_key
        )
        new_category = url_categories.create_custom_url_category(
            api_token,
            self.base_url,
            configured_names,
            urls,
            db_categorized_urls,
            description,
        )
        return new_category

    def update_url_in_category(self, category_name: str, urls: list[str]):
        api_token: str = auth.login(
            self.base_url, self.admin_user, self.admin_password, self.api_key
        )
        category_id: str = url_categories.fetch_category_id_by_category_name(
            api_token, self.base_url, category_name
        )
        if category_id is None:
            raise RuntimeError
        result = url_categories.update_custom_url_category(
            api_token, self.base_url, category_id, urls
        )
        return result
