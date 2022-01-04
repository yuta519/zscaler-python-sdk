from zscaler_python_sdk.lib import api


def fetch_all_nw_services(api_token: str, base_url: str) -> list[str]:
    return api.get(api_token, f"{base_url}/networkServices")


def fetch_all_nw_service_groups(api_token: str, base_url: str) -> list[str]:
    return api.get(api_token, f"{base_url}/networkServiceGroups")
