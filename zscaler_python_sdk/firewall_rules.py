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
