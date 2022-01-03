from zscaler_python_sdk.lib import api


def fetch_all_dst_groups(api_token: str, base_url: str) -> list[str]:
    return api.get(api_token, f"{base_url}/ipDestinationGroups")


def fetch_one_dst_groups(api_token: str, base_url: str, group_name: str) -> list[str]:
    ip_dst_groups = api.get(api_token, f"{base_url}/ipDestinationGroups")
    print(ip_dst_groups)
    for group in ip_dst_groups:
        if group["name"] == group_name:
            return group
    return None


def create_dst_groups(api_token: str, base_url: str) -> list[str]:
    pass


def update_dst_groups(api_token: str, base_url: str) -> list[str]:
    pass


def delete_dst_groups(api_token: str, base_url: str) -> list[str]:
    pass
