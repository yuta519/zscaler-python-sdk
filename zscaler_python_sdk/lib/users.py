from typing import Any
from zscaler_python_sdk.lib import api

from requests.models import Response


def fetch_users(
    api_token: str,
    base_url: str,
    name: str,
    department: str,
    group: str,
    page: int,
    size: int,
) -> dict[str, Any]:
    """Get users who are using Zscaler."""
    name_query: str = f"name={name}" if name is not None else None
    department_query: str = f"dept={department}" if department is not None else None
    group_query: str = f"group={group}" if group is not None else None
    page_query: str = f"page={page}" if page is not None else None
    size_query: str = f"pageSize={size}" if size is not None else None

    endpoint_path: str = "/users?"
    for query in [name_query, department_query, group_query, page_query, size_query]:
        if query is not None:
            endpoint_path += f"&{query}"
    users = api.get(api_token, base_url + endpoint_path)
    return users


def fetch_departments(api_token: str, base_url: str, search: str) -> dict[str, Any]:
    departments = api.get(
        api_token,
        f"{base_url}/departments"
        if search is None
        else f"{base_url}/departments?search={search}",
    )
    return departments


def fetch_groups(api_token: str, base_url: str, search: str) -> dict[str, Any]:
    groups = api.get(
        api_token,
        f"{base_url}/groups"
        if search is None
        else f"{base_url}/groups?search={search}",
    )
    return groups


# TODO: yuta519
def create_user() -> dict[str, Any]:
    pass


# TODO: yuta519
def update_user() -> dict[str, Any]:
    pass


# TODO: yuta519
def delete_user() -> dict[str, Any]:
    pass
