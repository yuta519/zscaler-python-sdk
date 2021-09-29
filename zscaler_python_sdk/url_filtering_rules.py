import json
from typing import Dict
from typing import List
from typing import Union
from zscaler_python_sdk.zia import api_get, api_post, api_put

import requests
from requests import status_codes
from requests.models import Response


def fetch_all_url_filering_rules(isFull: bool = False) -> Dict[str, str]:
    """Get Zscaler's url filtering rules."""
    response: Response = api_get("/urlFilteringRules")
    url_filtering_rules: list = response.json()

    if not isFull:
        try:
            for url_filtering_rule in url_filtering_rules:
                del (
                    url_filtering_rule['rank'],
                    url_filtering_rule['requestMethods'],
                    url_filtering_rule['blockOverride'],
                    url_filtering_rule['enforceTimeValidity'],
                    url_filtering_rule['cbiProfileId'],
                )
        except:
            pass

    url_filtering_rules = sorted(url_filtering_rules, key=lambda x:x['order'])
    
    return url_filtering_rules


def fetch_specific_url_filering_rules():
    pass


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
    action: str
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
    response: Response = api_post("/urlFilteringRules", payload)

    message =(
        f"Success: '{response.json()['name']}' is created" if response.status_code == 200 
        else f"Failed: { response.status_code } { response.json()['message'] }"
    )
    return message
