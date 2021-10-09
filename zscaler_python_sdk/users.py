from typing import Any, Optional
from typing import Dict
from zscaler_python_sdk.zia import api_get

# from zscaler_python_sdk.zia import api_post

from requests.models import Response


def fetch_users(
    name: Optional[str] = None,
    dept: Optional[str] = None,
    group: Optional[str] = None,
    page: Optional[int] = None,
    size: Optional[int] = None,
    tenant: str = None,
) -> Dict[str, Any]:
    """Get users who are using Zscaler."""
    name_query: Optional[str] = f"name={name}" if name is not None else None
    dept_query: Optional[str] = f"dept={dept}" if dept is not None else None
    group_query: Optional[str] = f"group={group}" if group is not None else None
    page_query: Optional[str] = f"page={page}" if page is not None else None
    size_query: Optional[str] = f"pageSize={size}" if size is not None else None

    endpoint_path: str = "/users?"
    for query in [name_query, dept_query, group_query, page_query, size_query]:
        if query is not None:
            endpoint_path += f"&{query}"

    response: Response = api_get(endpoint_path, tenant)
    return response


def fetch_departments(
    search: Optional[str] = None,
    tenant: Optional[str] = None,
) -> Dict[str, Any]:
    response: Response = api_get(
        "/departments" if search is None else f"/departments?search={search}",
        tenant,
    )
    return response


def fetch_groups(
    search: Optional[str] = None,
    tenant: Optional[str] = None,
) -> Dict[str, Any]:
    response: Response = api_get(
        "/groups" if search is None else f"/groups?search={search}",
        tenant,
    )
    return response
