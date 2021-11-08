from typing import Dict
from typing import List
from typing import Optional
from typing import Union

from zscaler_python_sdk.zia import api_get
from zscaler_python_sdk.zia import api_post

from requests.models import Response


def fetch_all_url_filering_rules(
    isFull: bool = False,
    tenant: str = None,
) -> Dict[str, str]:
    """Get Zscaler's url filtering rules."""
    response: Response = api_get("/urlFilteringRules", tenant)
    url_filtering_rules: list = response

    if not isFull:
        for tenant_name in url_filtering_rules.keys():
            for url_filtering_rule in url_filtering_rules[tenant_name]:
                del (
                    url_filtering_rule["rank"],
                    url_filtering_rule["requestMethods"],
                    url_filtering_rule["blockOverride"],
                    url_filtering_rule["enforceTimeValidity"],
                    url_filtering_rule["cbiProfileId"],
                )
            url_filtering_rules[tenant_name] = sorted(
                url_filtering_rules[tenant_name], key=lambda x: x["order"]
            )

    return url_filtering_rules


def fetch_specific_url_filering_rules():
    pass


def fetch_specific_url_filering_rule_id(rule_name: str, tenant: str) -> int:
    url_filtering_rules: list[str] = api_get("/urlFilteringRules", tenant)
    target_rule_id: Optional[int] = None
    for rule in url_filtering_rules:
        target_rule_id = rule["id"] if rule["name"] == rule_name else None
    return target_rule_id


def update_url_filtering_rule(rule_name: str, tenant: str) -> str:
    rule_id: Optional[int] = fetch_specific_url_filering_rule_id(
        rule_name=rule_name,
        tenant=tenant,
    )
    if rule_id is None:
        return "[Error] Invalied URL Filtering Rule Name"
    # api_put("/urlFilteringRules", tenant)


def create_url_filering_rules(
    name: str,
    order: int,
    protocols: List[str],
    locations: List[str],
    groups: List[str],
    departments: List[str],
    users: List[str],
    url_categories: List[str],
    state: str,
    rank: int,
    action: str,
    tenant: str,
) -> str:
    payload: Dict[str, Union[str, int, List[str]]] = {
        "name": name,
        "order": order,
        "protocols": protocols,
        "locations": locations,
        "groups": groups,
        "departments": departments,
        "users": users,
        "urlCategories": url_categories,
        "state": state,
        "rank": rank,
        "action": action,
    }
    response: Response = api_post("/urlFilteringRules", payload, tenant)

    return response
