from typing import Any
from typing import Dict
from typing import List
from typing import Union

from requests.models import Response

from zscaler_python_sdk.zia import api_get
from zscaler_python_sdk.zia import api_post


def fetch_adminusers(
    search_query: str = None,
    tenant: str = None,
) -> List[Dict[Any, Any]]:
    """Get Zscaler's url catergories."""
    endpoint_path: str = "/adminUsers"
    if search_query is not None:
        endpoint_path = f"{endpoint_path}?search={search_query}"
    response: Response = api_get(endpoint_path, tenant)
    return response


def fetch_adminroles(
    tenant: str = None,
) -> List[Dict[Any, Any]]:
    response: Response = api_get("/adminRoles/lite", tenant)
    return response


def create_adminuser(
    loginName: str,
    userName: str,
    email: str,
    password: str,
    rolename: str,
    tenant: str,
) -> str:
    user_api_endpoint_path: str = "/adminUsers"
    roles: List[Dict[str, Union[int, str]]] = fetch_adminroles(tenant)
    role_id: int = None

    for role in roles:
        if rolename in role.values():
            role_id: int = role["id"]

    if role_id is None:
        message = f"There is no matched roles to specify you, {rolename}"
        return message

    admin_user_information = {
        "loginName": loginName,
        "userName": userName,
        "email": email,
        "password": password,
        "role": {"id": role_id},
        "adminScopescopeGroupMemberEntities": [],
        "adminScopeType": "ORGANIZATION",
        "adminScopeScopeEntities": [],
        "isPasswordLoginAllowed": True,
        "name": "Yuta Kawamura",
    }

    response: Response = api_post(
        user_api_endpoint_path, admin_user_information, tenant
    )
    message: str = "Success" if response.status_code == 200 else "Failed"
    message += (
        f": {response.status_code} {response.text}" if message == "Failed" else None
    )

    return message
