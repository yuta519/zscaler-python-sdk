from typing import Any, Dict, Optional
from zscaler_python_sdk.zia import api_get


def fetch_firewall_rules(tenant: Optional[str] = None) -> Dict[str, Any]:
    firewall_rules: Dict[str, Any] = api_get("/firewallFilteringRules", tenant)
    # firewall_rules = sorted(firewall_rules[tenant], key=lambda x: x["order"]) for tenant in firewall_rules.keys()

    return firewall_rules
