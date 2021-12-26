import configparser
from typing import Dict
from typing import List


class Base(object):
    def __init__(self) -> None:
        config = configparser.ConfigParser()
        config.read("config/config.ini")

        self.tenants: List[str] = config.sections()
        self.cloud_name: Dict[str, str] = {}
        self.base_url: Dict[str] = {}
        self.api_key: Dict[str] = {}
        self.admin_user: Dict[str] = {}
        self.admin_password: Dict[str] = {}

        for section in config.sections():
            self.cloud_name[section] = config[section]["HOSTNAME"]
            self.base_url[section] = f"https://admin.{self.cloud_name[section]}/api/v1"
            self.api_key[section] = config[section]["APIKEY"]
            self.admin_user[section] = config[section]["USERNAME"]
            self.admin_password[section] = config[section]["PASSWORD"]

        # self.cloud_name: str = config["credential"]["HOSTNAME"]
        # self.base_url: str = f"https://admin.{self.cloud_name}/api/v1"
        # self.api_key: str = config["credential"]["APIKEY"]
        # self.admin_user: str = config["credential"]["USERNAME"]
        # self.admin_password: str = config["credential"]["PASSWORD"]
