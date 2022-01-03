from zscaler_python_sdk.lib import api


def fetch_all(api_token: str, base_url: str) -> list[str]:
    rules = api.get(api_token, f"{base_url}/firewallFilteringRules")
    return rules


def fetch_one_by_ruleid(api_token: str, base_url: str, rule_id: str) -> list[str]:
    response = api.get(api_token, f"{base_url}/firewallFilteringRules{rule_id}")
    return response


def fetch_one_by_rule_name(api_token: str, base_url: str, rule_name: str) -> list[str]:
    rules = fetch_all(api_token, base_url)
    for rule in rules:
        if rule["name"] == rule_name:
            return rule
    return None


def createe(
    api_token: str,
    base_url: str,
    rule_name: str,
    order: int,
    accessControl: str,
    enableFullLogging: str,
    rank: int,
    users: list[str],
    action: str,
    state: str,
    description: str,
    destIpCategories: str,
    destCountries: str,
    nwServices: list[dict[str]],
) -> list[str]:
    print(
        {
            "name": rule_name,
            "order": order,
            "accessControl": accessControl,
            "enableFullLogging": enableFullLogging,
            "rank": rank,
            "users": users,
            "action": action,
            "state": state,
            "description": description,
            "destIpCategories": destIpCategories,
            "destCountries": destCountries,
            "nwServices": nwServices,
            "predefined": False,
            "defaultRule": False,
        },
    )
    result = api.post(
        api_token,
        f"{base_url}/firewallFilteringRules",
        {
            "name": rule_name,
            "order": order,
            "accessControl": accessControl,
            "enableFullLogging": enableFullLogging,
            "rank": rank,
            "users": users,
            "action": action,
            "state": state,
            "description": description,
            "destIpCategories": destIpCategories,
            "destCountries": destCountries,
            "nwServices": nwServices,
            "predefined": False,
            "defaultRule": False,
        },
    )
    return result


# def update_firewall_rule() -> str:
#     pass


# def fetch_ip_destination_groups(
#     ip_group_id: Optional[int] = None,
#     tenant: Optional[str] = None,
# ) -> Dict[str, Any]:
#     ip_destination_groups: Dict[str, Any] = api_get(
#         "/ipDestinationGroups"
#         if ip_group_id is None
#         else f"/ipDestinationGroups/{ip_group_id}",
#         tenant,
#     )
#     return ip_destination_groups


# def create_ip_destination_groups() -> str:
#     pass


# def update_ip_destination_group() -> str:
#     pass


# def fetch_ip_source_groups(
#     ip_group_id: Optional[int] = None,
#     tenant: Optional[str] = None,
# ) -> Dict[str, Any]:
#     ip_source_groups: Dict[str, Any] = api_get(
#         "/ipSourceGroups" if ip_group_id is None else f"/ipSourceGroups/{ip_group_id}",
#         tenant,
#     )
#     return ip_source_groups


# def create_ip_source_groups() -> str:
#     pass


# def update_ip_source_group() -> str:
#     pass


# def fetch_network_application_groups(
#     group_id: Optional[int] = None,
#     tenant: Optional[str] = None,
# ) -> Dict[str, Any]:
#     nw_app_groups: Dict[str, Any] = api_get(
#         "/networkApplicationGroups"
#         if group_id is None
#         else f"/networkApplicationGroups/{group_id}",
#         tenant,
#     )
#     return nw_app_groups


# def fetch_network_applications(
#     app_id: Optional[int] = None,
#     tenant: Optional[str] = None,
# ) -> Dict[str, Any]:
#     nw_apps: Dict[str, Any] = api_get(
#         "/networkApplications" if app_id is None else f"/networkApplications/{app_id}",
#         tenant,
#     )
#     return nw_apps


# def fetch_network_service_groups(
#     group_id: Optional[int] = None,
#     tenant: Optional[str] = None,
# ) -> Dict[str, Any]:
#     nw_app_groups: Dict[str, Any] = api_get(
#         "/networkServiceGroups"
#         if group_id is None
#         else f"/networkServiceGroups/{group_id}",
#         tenant,
#     )
#     return nw_app_groups


# def fetch_network_services(
#     service_id: Optional[int] = None,
#     tenant: Optional[str] = None,
# ) -> Dict[str, Any]:
#     nw_apps: Dict[str, Any] = api_get(
#         "/networkServices" if service_id is None else f"/networkServices/{service_id}",
#         tenant,
#     )
#     return nw_apps
