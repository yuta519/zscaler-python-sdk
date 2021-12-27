import json

import requests
from requests.models import Response

HEADER: dict[str, str] = {
    "content-type": "application/json",
    "cache-control": "no-cache",
}


def get(api_token: str, api_endpoint: str) -> dict[any, any]:
    """ """
    HEADER["cookie"] = api_token
    response: Response = requests.get(api_endpoint, headers=HEADER)
    return response.json() if response.status_code == 200 else RuntimeError


def post(api_token: str, api_endpoint: str, payload: dict[str, str]) -> any:
    HEADER["cookie"] = api_token
    response: Response = requests.post(
        api_endpoint, json.dumps(payload), headers=HEADER
    )
    return response


# def api_put(
#     endpoint_path: str,
#     payload: dict[any, Any],
#     tenant: str,
# ) -> Response:
#     api_endpoint: str = f"{base.base_url[tenant]}{endpoint_path}"
#     api_token: str = login(tenant)
#     headers: dict[str, str] = {
#         "content-type": "application/json",
#         "cache-control": "no-cache",
#         "cookie": api_token,
#     }
#     response: Response = requests.put(
#         api_endpoint,
#         json.dumps(payload),
#         headers=headers,
#     )
#     logout(api_token, tenant)
#     return response
