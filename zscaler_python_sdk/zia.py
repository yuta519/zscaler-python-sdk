import json
import time
from typing import Any
from typing import Dict
from typing import List
from typing import Optional
from typing import Union

import requests
from requests.models import Response

from zscaler_python_sdk.base import Base


base = Base()


def fetch_tenants() -> List[str]:
    return base.tenants


def obfuscateApiKey(tenant: str) -> List[Union[int, str]]:
    """Parse API Key to use zscaler api.
    This functions are supplied by Zscaler.
    More information of this function is below.
    Reference : Zscaler help pages.
        https://help.zscaler.com/zia/api-getting-started
    """
    seed = base.api_key[tenant]
    now = int(time.time() * 1000)
    n = str(now)[-6:]
    r = str(int(n) >> 1).zfill(6)
    key = ""
    for i in range(0, len(str(n)), 1):
        key += seed[int(str(n)[i])]
    for j in range(0, len(str(r)), 1):
        key += seed[int(str(r)[j]) + 2]
    obfuscate_api_key = [now, key]
    return obfuscate_api_key


def login(tenant: str) -> str:
    """Login to Zscaler and create an api session."""
    obfuscate_api_key: List[int, str] = obfuscateApiKey(tenant)

    api_endpoint: str = f"{base.base_url[tenant]}/authenticatedSession"
    headers: dict[str, str] = {
        "content-type": "application/json",
        "cache-control": "no-cache",
    }
    payload: dict[str, str] = {
        "username": base.admin_user[tenant],
        "password": base.admin_password[tenant],
        "timestamp": obfuscate_api_key[0],
        "apiKey": obfuscate_api_key[1],
    }

    response: Response = requests.post(
        api_endpoint, json.dumps(payload), headers=headers
    )
    cookie: dict[str, str] = response.cookies.get_dict()
    api_token: str = "JSESSIONID=" + cookie["JSESSIONID"]

    return api_token


def activate_configuration() -> None:
    """ """
    # TODO (yuta.kawamura)
    pass


def logout(api_token: str, tenant: str) -> None:
    """Logout from API sesion."""
    api_endpoint: str = f"{base.base_url[tenant]}/authenticatedSession"
    headers: dict[str, str] = {
        "content-type": "application/json",
        "cache-control": "no-cache",
        "cookie": api_token,
    }
    requests.delete(api_endpoint, headers=headers)


def api_get(endpoint_path: str, tenant: Optional[str] = None) -> Dict[Any, Any]:
    """ """

    def get_request(
        tenant: str, response_list: List[Dict[str, Any]]
    ) -> List[Dict[str, Any]]:
        api_endpoint: str = f"{base.base_url[tenant]}{endpoint_path}"
        api_token: str = login(tenant)
        headers: dict[str, str] = {
            "content-type": "application/json",
            "cache-control": "no-cache",
            "cookie": api_token,
        }
        response: Response = requests.get(api_endpoint, headers=headers)
        logout(api_token, tenant)

        if response.status_code == 200:
            response_list[tenant] = response.json()

        return response_list

    response_list: List[Dict[str, Any]] = {}
    if tenant in fetch_tenants():
        get_request(tenant, response_list)
    if tenant is None:
        for tenant in fetch_tenants():
            get_request(tenant, response_list)

    return response_list


def api_post(
    endpoint_path: str,
    payload: Dict[Any, Any],
    tenant: Optional[str] = None,
) -> Response:
    """"""

    def post_request(
        tenant: str, response_list: List[Dict[str, Any]]
    ) -> List[Dict[str, Any]]:
        api_endpoint: str = f"{base.base_url[tenant]}{endpoint_path}"
        api_token: str = login(tenant)
        headers: dict[str, str] = {
            "content-type": "application/json",
            "cache-control": "no-cache",
            "cookie": api_token,
        }
        response: Response = requests.post(
            api_endpoint,
            json.dumps(payload),
            headers=headers,
        )
        logout(api_token, tenant)

        if response.status_code == 200:
            response_list[tenant] = response.json()
        return response_list

    response_list: List[Dict[str, Any]] = {}
    if tenant in fetch_tenants():
        post_request(tenant, response_list)
    if tenant is None:
        for tenant in fetch_tenants():
            post_request(tenant, response_list)

    return response_list


def api_put(
    endpoint_path: str,
    payload: Dict[Any, Any],
) -> Response:
    api_endpoint: str = f"{base.base_url}{endpoint_path}"
    api_token: str = login()
    headers: dict[str, str] = {
        "content-type": "application/json",
        "cache-control": "no-cache",
        "cookie": api_token,
    }
    response: Response = requests.put(
        api_endpoint,
        json.dumps(payload),
        headers=headers,
    )
    logout(api_token)

    if response.status_code == 200:
        return response
    else:
        print(response.status_code)
        print(response.text)
