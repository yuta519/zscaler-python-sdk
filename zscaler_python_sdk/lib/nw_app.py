from zscaler_python_sdk.lib import api


def fetch_all_nw_apps(api_token: str, base_url: str) -> list[str]:
    return api.get(api_token, f"{base_url}/networkApplications")


def fetch_all_nw_app_groups(api_token: str, base_url: str) -> list[str]:
    return api.get(api_token, f"{base_url}/networkApplicationGroups")


# def fetch_all_nw_app_groups(api_token: str, base_url: str) -> list[str]:
#     return api.get(api_token, f"{base_url}")


# def fetch_all_nw_app_groups(api_token: str, base_url: str) -> list[str]:
#     return api.get(api_token, f"{base_url}")


# def fetch_all_nw_app_groups(api_token: str, base_url: str) -> list[str]:
#     return api.get(api_token, f"{base_url}")


# def fetch_all_nw_app_groups(api_token: str, base_url: str) -> list[str]:
#     return api.get(api_token, f"{base_url}")
