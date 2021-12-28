from typing import Optional
from typing import Union

from zscaler_python_sdk.lib import api


def fetch_all(api_token: str, base_url, is_full: bool) -> dict[str, str]:
    """Get Zscaler's url filtering rules."""
    url_filtering_rules: dict = api.get(api_token, f"{base_url}/urlFilteringRules")

    if not is_full:
        for url_filtering_rule in url_filtering_rules:
            del (
                url_filtering_rule["rank"],
                url_filtering_rule["requestMethods"],
                url_filtering_rule["blockOverride"],
                url_filtering_rule["enforceTimeValidity"],
                url_filtering_rule["cbiProfileId"],
            )
        url_filtering_rules = sorted(url_filtering_rules, key=lambda x: x["order"])

    return url_filtering_rules


def fetch_one_by_rulename(api_token: str, base_url: str, rule_name: str) -> dict:
    url_filtering_rules: list[str] = fetch_all(api_token, base_url, False)
    for rule in url_filtering_rules:
        if rule["name"] == rule_name:
            return rule
    return None


def create(
    api_token: str,
    base_url: str,
    name: str,
    order: int,
    protocols: list[str],
    locations: list[str],
    groups: list[str],
    departments: list[str],
    users: list[str],
    url_categories: list[str],
    state: str,
    rank: int,
    action: str,
) -> str:
    payload: dict[str, Union[str, int, list[str]]] = {
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
    response: list[str] = api.post(api_token, f"{base_url}/urlFilteringRules", payload)
    return response


def update(
    api_token: str,
    base_url: str,
    rule_name: str,
    name: str,
    order: int,
    rank: int,
    state: str,
    protocols: list,
    action: str,
) -> str:
    rule: Optional[dict] = fetch_one_by_rulename(api_token, base_url, rule_name)
    if rule is None:
        return "[Error] Invalied URL Filtering Rule Name"
    payload: dict[str, str] = {
        "name": name if name is not None else rule["name"],
        "order": order if order is not None else rule["order"],
        "state": state if state is not None else rule["state"],
        "protocols": protocols if protocols is not None else rule["protocols"],
        "action": action if action is not None else rule["action"],
    }
    if rank is not None:
        payload["rank"] = rank
    else:
        payload["rank"] = rule["rank"] if "rank" in rule.keys() else 7
    message = api.put(api_token, f"{base_url}/urlFilteringRules/{rule['id']}", payload)
    return message
