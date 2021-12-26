from typing import Any, Dict, Optional
from zscaler_python_sdk.zia import api_get


def fetch_firewall_rules(
    rule_id: Optional[str] = None,
    tenant: Optional[str] = None,
) -> Dict[str, Any]:
    firewall_rules: Dict[str, Any] = api_get(
        "/firewallFilteringRules"
        if rule_id is None
        else f"/firewallFilteringRules/{rule_id}",
        tenant,
    )
    return firewall_rules


def create_new_firewall_rule() -> str:
    pass


def update_firewall_rule() -> str:
    pass


def fetch_ip_destination_groups(
    ip_group_id: Optional[int] = None,
    tenant: Optional[str] = None,
) -> Dict[str, Any]:
    ip_destination_groups: Dict[str, Any] = api_get(
        "/ipDestinationGroups"
        if ip_group_id is None
        else f"/ipDestinationGroups/{ip_group_id}",
        tenant,
    )
    return ip_destination_groups


def create_ip_destination_groups() -> str:
    pass


def update_ip_destination_group() -> str:
    pass


def fetch_ip_source_groups(
    ip_group_id: Optional[int] = None,
    tenant: Optional[str] = None,
) -> Dict[str, Any]:
    ip_source_groups: Dict[str, Any] = api_get(
        "/ipSourceGroups" if ip_group_id is None else f"/ipSourceGroups/{ip_group_id}",
        tenant,
    )
    return ip_source_groups


def create_ip_source_groups() -> str:
    pass


def update_ip_source_group() -> str:
    pass


def fetch_network_application_groups(
    group_id: Optional[int] = None,
    tenant: Optional[str] = None,
) -> Dict[str, Any]:
    nw_app_groups: Dict[str, Any] = api_get(
        "/networkApplicationGroups"
        if group_id is None
        else f"/networkApplicationGroups/{group_id}",
        tenant,
    )
    return nw_app_groups


def fetch_network_applications(
    app_id: Optional[int] = None,
    tenant: Optional[str] = None,
) -> Dict[str, Any]:
    nw_apps: Dict[str, Any] = api_get(
        "/networkApplications" if app_id is None else f"/networkApplications/{app_id}",
        tenant,
    )
    return nw_apps


def fetch_network_service_groups(
    group_id: Optional[int] = None,
    tenant: Optional[str] = None,
) -> Dict[str, Any]:
    nw_app_groups: Dict[str, Any] = api_get(
        "/networkServiceGroups"
        if group_id is None
        else f"/networkServiceGroups/{group_id}",
        tenant,
    )
    return nw_app_groups


def fetch_network_services(
    service_id: Optional[int] = None,
    tenant: Optional[str] = None,
) -> Dict[str, Any]:
    nw_apps: Dict[str, Any] = api_get(
        "/networkServices" if service_id is None else f"/networkServices/{service_id}",
        tenant,
    )
    return nw_apps
