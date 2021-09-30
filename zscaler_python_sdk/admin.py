from typing import Any
from typing import Dict 
from typing import List
from typing import Union

from requests.models import Response

from zscaler_python_sdk.zia import api_get
from zscaler_python_sdk.zia import api_post


def fetch_adminusers(search_query: str = None) -> List[Dict[Any, Any]]:
    """Get Zscaler's url catergories."""
    endpoint_path: str = "/adminUsers"
    if search_query is not None:
        endpoint_path = f"{endpoint_path}?search={search_query}"
    response: Response = api_get(endpoint_path)
    return response.json()


def fetch_adminroles():
    response: Response = api_get("/adminRoles/lite")
    return response.json()


def create_adminuser(
    loginName: str,
    userName: str,
    email: str,
    password: str,
    rolename: str,
) -> str:
    role_api_endpoint_path: str = "/adminRoles/lite"
    user_api_endpoint_path: str = "/adminUsers"

    role_response: Response = api_get(role_api_endpoint_path)
    roles: List[Dict[str, Union[int, str]]] = role_response.json()
    role_id: int = None
    for role in roles:
        if rolename in role.values():
            role_id: int = role["id"]
        else:
            print(f"There is no matched roles to specify you, {rolename}")

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

    admin_user_response: Response = api_post(
        user_api_endpoint_path, admin_user_information
    )

    message: str = "Success" if admin_user_response.status_code == 200 else f"Failed"
    # message += f": {user_response.status_code} {user_response.text}" if message == "Failed" else None
    return message
