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
