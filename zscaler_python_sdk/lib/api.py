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
    return response.json()


def put(api_token: str, endpoint_path: str, payload: dict[any, any]) -> dict[any, any]:
    api_endpoint: str = f"{endpoint_path}"
    HEADER["cookie"] = api_token
    response: Response = requests.put(
        api_endpoint,
        json.dumps(payload),
        headers=HEADER,
    )
    return response.json()
