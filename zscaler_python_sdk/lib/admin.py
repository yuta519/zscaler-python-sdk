from typing import Any

from requests.models import Response

from zscaler_python_sdk.lib import api


def fetch_adminusers(
    api_token: str, base_url: str, search_query: str = None
) -> dict[Any, Any]:
    """Get Zscaler's url catergories."""
    endpoint_path: str = (
        f"{base_url}/adminUsers"
        if search_query is not None
        else f"{base_url}/adminUsers?search={search_query}"
    )
    response: Response = api.get(api_token, endpoint_path)
    return response


# def fetch_adminroles(
#     tenant: str = None,
# ) -> List[Dict[Any, Any]]:
#     response: Response = api_get("/adminRoles/lite", tenant)
#     return response


# def create_adminuser(
#     loginName: str,
#     userName: str,
#     email: str,
#     password: str,
#     rolename: str,
#     tenant: str,
# ) -> str:
#     user_api_endpoint_path: str = "/adminUsers"
#     roles: List[Dict[str, Union[int, str]]] = fetch_adminroles(tenant)
#     role_id: int = None

#     for role in roles[tenant]:
#         if rolename in role.values():
#             role_id: int = role["id"]

#     if role_id is None:
#         return {tenant: f"[Error]There is no matched roles you specified, {rolename}"}

#     admin_user_information: Dict[str, Any] = {
#         "loginName": loginName,
#         "userName": userName,
#         "email": email,
#         "password": password,
#         "role": {"id": role_id},
#         "adminScopescopeGroupMemberEntities": [],
#         "adminScopeType": "ORGANIZATION",
#         "adminScopeScopeEntities": [],
#         "isPasswordLoginAllowed": True,
#         "name": userName,
#     }

#     response: Response = api_post(
#         user_api_endpoint_path, admin_user_information, tenant
#     )

#     return response
