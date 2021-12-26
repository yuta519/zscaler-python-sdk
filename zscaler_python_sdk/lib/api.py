import requests
from requests.models import Response


def get(api_token: str, api_endpoint: str) -> dict[any, any]:
    """ """
    headers: dict[str, str] = {
        "content-type": "application/json",
        "cache-control": "no-cache",
        "cookie": api_token,
    }
    response: Response = requests.get(api_endpoint, headers=headers)
    return response.json() if response.status_code == 200 else RuntimeError


# def api_post(
#     api_token: str, url: str, headers: dict[str, str], payload: dict[str, str]
# ) -> any:
#     headers["cookie"] = api_token
#     result = requests.post(url=url, headers=headers, payload=payload)
#     return result


# def api_post(
#     endpoint_path: str,
#     payload: dict[any, Any],
#     tenant: Optional[str] = None,
# ) -> Response:
#     """"""

#     def post_request(
#         tenant: str, response_list: list[dict[str, any]]
#     ) -> list[dict[str, any]]:
#         api_endpoint: str = f"{base.base_url[tenant]}{endpoint_path}"
#         api_token: str = login(tenant)
#         headers: dict[str, str] = {
#             "content-type": "application/json",
#             "cache-control": "no-cache",
#             "cookie": api_token,
#         }
#         response: Response = requests.post(
#             api_endpoint,
#             json.dumps(payload),
#             headers=headers,
#         )
#         logout(api_token, tenant)

#         if response.status_code == 200:
#             response_list[tenant] = response.json()
#         else:
#             response_list[
#                 tenant
#             ] = f"[Error]{response.status_code}: {response.json()['message']}"
#         return response_list

#     response_list: list[dict[str, any]] = {}
#     if tenant in fetch_tenants():
#         post_request(tenant, response_list)
#     if tenant is None:
#         for tenant in fetch_tenants():
#             post_request(tenant, response_list)

#     return response_list


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
