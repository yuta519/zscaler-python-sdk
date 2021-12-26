import configparser
import json
import time
from typing import Optional

import requests
from requests.models import Response

from zscaler_python_sdk.lib import admin


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

    def obfuscateApiKey(self) -> None:
        """Parse API Key to use zscaler api.
        This functions are supplied by Zscaler.
        More information of this function is below.
        Reference : Zscaler help pages.
            https://help.zscaler.com/zia/api-getting-started
        """
        seed, now = self.api_key, int(time.time() * 1000)
        n = str(now)[-6:]
        r = str(int(n) >> 1).zfill(6)
        key = ""
        for i in range(0, len(str(n)), 1):
            key += seed[int(str(n)[i])]
        for j in range(0, len(str(r)), 1):
            key += seed[int(str(r)[j]) + 2]
        return {"time": now, "obfuscated_key": key}

    def login(self) -> str:
        """Login to Zscaler and create an api session."""
        api_endpoint: str = f"{self.base_url}/authenticatedSession"
        obfuscate_api_key: dict[str, str] = self.obfuscateApiKey()
        headers: dict[str, str] = {
            "content-type": "application/json",
            "cache-control": "no-cache",
        }
        payload: dict[str, str] = {
            "username": self.admin_user,
            "password": self.admin_password,
            "timestamp": obfuscate_api_key["time"],
            "apiKey": obfuscate_api_key["obfuscated_key"],
        }
        response: Response = requests.post(
            api_endpoint, json.dumps(payload), headers=headers
        )
        cookie: dict[str, str] = response.cookies.get_dict()
        api_token: str = "JSESSIONID=" + cookie["JSESSIONID"]
        return api_token

    # def activate_configuration() -> None:
    #     """ """
    #     # TODO (yuta.kawamura)
    #     pass

    def logout(self, api_token: str) -> None:
        """Logout from API sesion."""
        api_endpoint: str = f"{self.base_url}/authenticatedSession"
        headers: dict[str, str] = {
            "content-type": "application/json",
            "cache-control": "no-cache",
            "cookie": api_token,
        }
        requests.delete(api_endpoint, headers=headers)

    def fetch_admin_users(self, search_query: str = None):
        api_token: str = self.login()
        admin_users = admin.fetch_adminusers(
            api_token=api_token, base_url=self.base_url, search_query=search_query
        )
        print(admin_users)

    # def api_get(self, endpoint_path: str) -> dict[any, any]:
    #     """ """

    #     def get_request(response: list[str]) -> list[any]:
    #         api_endpoint: str = f"{self.base_url}{endpoint_path}"
    #         headers: dict[str, str] = {
    #             "content-type": "application/json",
    #             "cache-control": "no-cache",
    #             "cookie": self.api_key,
    #         }
    #         response: Response = requests.get(api_endpoint, headers=headers)
    #         self.logout(api_token, tenant)

    #         if response.status_code == 200:
    #             response[tenant] = response.json()

    #         return response_list

    #     response_list: list[dict[str, any]] = {}
    #     if tenant in self.fetch_tenants():
    #         get_request(tenant, response_list)
    #     if tenant is None:
    #         for tenant in self.fetch_tenants():
    #             get_request(tenant, response_list)

    #     return response_list

    # def api_post(


#     #     endpoint_path: str,
#     #     payload: dict[any, any],
#     #     tenant: Optional[str] = None,
#     # ) -> Response:
#     #     """"""

#     #     def post_request(
#     #         tenant: str, response_list: list[dict[str, any]]
#     #     ) -> list[dict[str, any]]:
#     #         api_endpoint: str = f"{base.base_url[tenant]}{endpoint_path}"
#     #         api_token: str = login(tenant)
#     #         headers: dict[str, str] = {
#     #             "content-type": "application/json",
#     #             "cache-control": "no-cache",
#     #             "cookie": api_token,
#     #         }
#     #         response: Response = requests.post(
#     #             api_endpoint,
#     #             json.dumps(payload),
#     #             headers=headers,
#     #         )
#     #         logout(api_token, tenant)

#     #         if response.status_code == 200:
#     #             response_list[tenant] = response.json()
#     #         else:
#     #             response_list[
#     #                 tenant
#     #             ] = f"[Error]{response.status_code}: {response.json()['message']}"
#     #         return response_list

#     #     response_list: list[dict[str, any]] = {}
#     #     if tenant in fetch_tenants():
#     #         post_request(tenant, response_list)
#     #     if tenant is None:
#     #         for tenant in fetch_tenants():
#     #             post_request(tenant, response_list)

#     #     return response_list

#     # def api_put(
#     #     endpoint_path: str,
#     #     payload: dict[any, any],
#     #     tenant: str,
#     # ) -> Response:
#     #     api_endpoint: str = f"{base.base_url[tenant]}{endpoint_path}"
#     #     api_token: str = login(tenant)
#     #     headers: dict[str, str] = {
#     #         "content-type": "application/json",
#     #         "cache-control": "no-cache",
#     #         "cookie": api_token,
#     #     }
#     #     response: Response = requests.put(
#     #         api_endpoint,
#     #         json.dumps(payload),
#     #         headers=headers,
#     #     )
#     #     logout(api_token, tenant)
#     #     return response
