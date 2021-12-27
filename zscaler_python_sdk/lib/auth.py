import json
import time

import requests
from requests import Response


def _obfuscateApiKey(api_key: str) -> dict[str, str]:
    """Parse API Key to use zscaler api.
    This functions are supplied by Zscaler.
    More information of this function is below.
    Reference : Zscaler help pages.
        https://help.zscaler.com/zia/api-getting-started
    """
    seed, now = api_key, int(time.time() * 1000)
    n = str(now)[-6:]
    r = str(int(n) >> 1).zfill(6)
    key = ""
    for i in range(0, len(str(n)), 1):
        key += seed[int(str(n)[i])]
    for j in range(0, len(str(r)), 1):
        key += seed[int(str(r)[j]) + 2]
    return {"time": now, "obfuscated_key": key}


def login(base_url: str, admin_user: str, admin_password: str, api_key: str) -> str:
    """Login to Zscaler and create an api session."""
    obfuscate_api_key: dict[str, str] = _obfuscateApiKey(api_key)
    headers: dict[str, str] = {
        "content-type": "application/json",
        "cache-control": "no-cache",
    }
    payload: dict[str, str] = {
        "username": admin_user,
        "password": admin_password,
        "timestamp": obfuscate_api_key["time"],
        "apiKey": obfuscate_api_key["obfuscated_key"],
    }
    response: Response = requests.post(
        f"{base_url}/authenticatedSession", json.dumps(payload), headers=headers
    )
    cookie: dict[str, str] = response.cookies.get_dict()
    return "JSESSIONID=" + cookie["JSESSIONID"]


# def activate_configuration() -> None:
#     """ """
#     # TODO (yuta.kawamura)
#     pass


def logout(api_token: str, base_url: str) -> None:
    """Logout from API sesion."""
    headers: dict[str, str] = {
        "content-type": "application/json",
        "cache-control": "no-cache",
        "cookie": api_token,
    }
    requests.delete(f"{base_url}/authenticatedSession", headers=headers)
