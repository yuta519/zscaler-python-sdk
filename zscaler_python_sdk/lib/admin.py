from typing import Any
from typing import Optional

from requests.models import Response

from zscaler_python_sdk.lib import api


def fetch_adminusers(
    api_token: str, base_url: str, search_query: Optional[str] = None
) -> dict[Any, Any]:
    """Get Zscaler's url catergories."""
    endpoint_path: str = (
        f"{base_url}/adminUsers"
        if search_query is None
        else f"{base_url}/adminUsers?search={search_query}"
    )
    response: Response = api.get(api_token, endpoint_path)
    return response


def fetch_adminroles(api_token: str, base_url: str) -> list[dict[Any, Any]]:
    return api.get(api_token, f"{base_url}/adminRoles/lite")


def create_adminuser(
    api_token: str,
    base_url: str,
    loginName: str,
    userName: str,
    email: str,
    password: str,
    rolename: str,
) -> str:
    roles: list[str] = fetch_adminroles(api_token, base_url)
    role_id: int = None
    for role in roles:
        if rolename in role["name"]:
            role_id = role["id"]
    if role_id is None:
        return {"Error": f"[Error]There is no matched roles you specified, {rolename}"}

    new_admin_user: dict[str, Any] = {
        "loginName": loginName,
        "userName": userName,
        "email": email,
        "password": password,
        "role": {"id": role_id},
        "adminScopescopeGroupMemberEntities": [],
        "adminScopeType": "ORGANIZATION",
        "adminScopeScopeEntities": [],
        "isPasswordLoginAllowed": True,
        "name": userName,
    }
    response: Response = api.post(api_token, f"{base_url}/adminUsers", new_admin_user)
    return response.text
