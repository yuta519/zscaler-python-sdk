import configparser
from typing import Optional

from zscaler_python_sdk.lib import admin
from zscaler_python_sdk.lib import auth
from zscaler_python_sdk.lib import firewall_rules
from zscaler_python_sdk.lib import ip_group
from zscaler_python_sdk.lib import nw_app
from zscaler_python_sdk.lib import nw_service
from zscaler_python_sdk.lib import url_categories
from zscaler_python_sdk.lib import url_filtering_rules
from zscaler_python_sdk.lib import users


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

    def fetch_users(
        self,
        name: Optional[str] = None,
        department: Optional[str] = None,
        group: Optional[str] = None,
        page: Optional[int] = None,
        size: Optional[int] = None,
    ) -> list[str]:
        api_token: str = auth.login(
            self.base_url, self.admin_user, self.admin_password, self.api_key
        )
        user_list = users.fetch_users(
            api_token, self.base_url, name, department, group, page, size
        )
        auth.logout(api_token, self.base_url)
        return user_list

    def fetch_departments(self, search: Optional[int] = None) -> list[str]:
        api_token: str = auth.login(
            self.base_url, self.admin_user, self.admin_password, self.api_key
        )
        departments = users.fetch_departments(api_token, self.base_url, search)
        auth.logout(api_token, self.base_url)
        return departments

    def fetch_groups(self, search: Optional[int] = None) -> list[str]:
        api_token: str = auth.login(
            self.base_url, self.admin_user, self.admin_password, self.api_key
        )
        groups = users.fetch_groups(api_token, self.base_url, search)
        auth.logout(api_token, self.base_url)
        return groups

    def fetch_url_categories(self, is_custom_only: Optional[str] = None) -> list[str]:
        api_token: str = auth.login(
            self.base_url, self.admin_user, self.admin_password, self.api_key
        )
        categories = url_categories.fetch_url_categories(
            api_token, self.base_url, is_custom_only
        )
        auth.logout(api_token, self.base_url)
        return categories

    def lookup_url_category(self, target_urls: list[str]) -> list[str]:
        api_token: str = auth.login(
            self.base_url, self.admin_user, self.admin_password, self.api_key
        )
        lookuped_categories = url_categories.lookup_url_classification(
            api_token, self.base_url, target_urls
        )
        auth.logout(api_token, self.base_url)
        return lookuped_categories

    def create_custom_url_category(
        self,
        configured_names: str,
        urls: list[str],
        db_categorized_urls: list[str],
        description: str,
    ) -> str:
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
        auth.logout(api_token, self.base_url)
        return new_category

    def update_url_in_category(self, category_name: str, urls: list[str]) -> dict:
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
        auth.logout(api_token, self.base_url)
        return result

    def fetch_all_url_filtering_rules(self, is_full: bool = False) -> list[str]:
        api_token: str = auth.login(
            self.base_url, self.admin_user, self.admin_password, self.api_key
        )
        rules: list[str] = url_filtering_rules.fetch_all(
            api_token, self.base_url, is_full
        )
        auth.logout(api_token, self.base_url)
        return rules

    def fetch_one_url_filtering_rules(self, rule_name: str) -> list[str]:
        api_token: str = auth.login(
            self.base_url, self.admin_user, self.admin_password, self.api_key
        )
        rule: dict[str, str] = url_filtering_rules.fetch_one_by_rulename(
            api_token, self.base_url, rule_name
        )
        auth.logout(api_token, self.base_url)
        return rule

    def create_url_filtering_rule(
        self,
        name: str,
        order: int,
        protocols: list[str],
        locations: list[str],
        groups: list[str],
        departments: list[str],
        users: list[str],
        url_categories: list[str],
        state: str,
        rank: int,
        action: str,
    ):
        api_token: str = auth.login(
            self.base_url, self.admin_user, self.admin_password, self.api_key
        )
        result = url_filtering_rules.create(
            api_token,
            self.base_url,
            name,
            order,
            protocols,
            locations,
            groups,
            departments,
            users,
            url_categories,
            state,
            rank,
            action,
        )
        auth.logout(api_token, self.base_url)
        return result

    def update_url_filtering_rule(
        self,
        rule_name: str,
        name: Optional[str] = None,
        order: Optional[int] = None,
        rank: Optional[int] = None,
        state: Optional[str] = None,
        protocols: Optional[list] = None,
        action: Optional[str] = None,
    ) -> str:
        api_token: str = auth.login(
            self.base_url, self.admin_user, self.admin_password, self.api_key
        )
        result = url_filtering_rules.update(
            api_token,
            self.base_url,
            rule_name,
            name,
            order,
            rank,
            state,
            protocols,
            action,
        )
        auth.logout(api_token, self.base_url)
        return result

    def fetching_all_fw_rules(self):
        api_token: str = auth.login(
            self.base_url, self.admin_user, self.admin_password, self.api_key
        )
        fw_rules: list[str] = firewall_rules.fetch_all(api_token, self.base_url)
        auth.logout(api_token, self.base_url)
        return fw_rules

    def fetching_one_fw_rule(self, rule_name: str):
        api_token: str = auth.login(
            self.base_url, self.admin_user, self.admin_password, self.api_key
        )
        fw_rules: list[str] = firewall_rules.fetch_one_by_rule_name(
            api_token, self.base_url, rule_name
        )
        auth.logout(api_token, self.base_url)
        return fw_rules

    def create_fw_rule(
        self,
        rule_name: str,
        order: int,
        accessControl: str,
        enableFullLogging: str,
        rank: int,
        users: list[str],
        action: str,
        state: str,
        description: str,
        destIpCategories: str,
        destCountries: str,
        nwServices: list[dict[str]],
    ):
        api_token: str = auth.login(
            self.base_url, self.admin_user, self.admin_password, self.api_key
        )
        result = firewall_rules.create(
            api_token,
            self.base_url,
            rule_name,
            order,
            accessControl,
            enableFullLogging,
            rank,
            users,
            action,
            state,
            description,
            destIpCategories,
            destCountries,
            nwServices,
        )
        auth.logout(api_token, self.base_url)
        return result

    def fetch_all_ip_dst_groups(self):
        api_token: str = auth.login(
            self.base_url, self.admin_user, self.admin_password, self.api_key
        )
        ip_dst_groups = ip_group.fetch_all_dst_groups(api_token, self.base_url)
        auth.logout(api_token, self.base_url)
        return ip_dst_groups

    def fetch_one_ip_dst_group(self, group_name: str):
        api_token: str = auth.login(
            self.base_url, self.admin_user, self.admin_password, self.api_key
        )
        ip_dst_group = ip_group.fetch_one_dst_groups(
            api_token, self.base_url, group_name
        )
        auth.logout(api_token, self.base_url)
        return ip_dst_group

    def fetch_all_ip_src_groups(self):
        api_token: str = auth.login(
            self.base_url, self.admin_user, self.admin_password, self.api_key
        )
        ip_dst_groups = ip_group.fetch_all_src_groups(api_token, self.base_url)
        auth.logout(api_token, self.base_url)
        return ip_dst_groups

    def fetch_one_ip_src_group(self, group_name: str):
        api_token: str = auth.login(
            self.base_url, self.admin_user, self.admin_password, self.api_key
        )
        ip_src_group = ip_group.fetch_one_src_groups(
            api_token, self.base_url, group_name
        )
        auth.logout(api_token, self.base_url)
        return ip_src_group

    def fetch_all_nw_apps(self):
        api_token: str = auth.login(
            self.base_url, self.admin_user, self.admin_password, self.api_key
        )
        nw_apps = nw_app.fetch_all_nw_apps(api_token, self.base_url)
        auth.logout(api_token, self.base_url)
        return nw_apps

    def fetch_all_nw_app_groups(self):
        api_token: str = auth.login(
            self.base_url, self.admin_user, self.admin_password, self.api_key
        )
        nw_app_groups = nw_app.fetch_all_nw_app_groups(api_token, self.base_url)
        auth.logout(api_token, self.base_url)
        return nw_app_groups

    def fetch_all_nw_services(self):
        api_token: str = auth.login(
            self.base_url, self.admin_user, self.admin_password, self.api_key
        )
        nw_services = nw_service.fetch_all_nw_services(api_token, self.base_url)
        auth.logout(api_token, self.base_url)
        return nw_services

    def fetch_all_nw_service_group(self):
        api_token: str = auth.login(
            self.base_url, self.admin_user, self.admin_password, self.api_key
        )
        nw_service_group = nw_service.fetch_all_nw_service_groups(
            api_token, self.base_url
        )
        auth.logout(api_token, self.base_url)
        return nw_service_group
