from re import match
from typing import Any
from typing import Optional
from urllib.parse import urlparse

from requests.models import Response

from zscaler_python_sdk.lib import api


def _extract_url_domain(target_url):
    """Extract domain from url given by user."""
    url_pattern = "https?://[\w/:%#\$&\?\(\)~\.=\+\-]+"
    if match(url_pattern, target_url):
        parsed_url = urlparse(target_url)
        domain = parsed_url.netloc
        return domain
    else:
        return target_url


def fetch_url_categories(
    api_token: str, base_url: str, is_custom_only: bool = False
) -> dict[Any, Any]:
    """Get Zscaler's url catergories."""
    response = api.get(
        api_token,
        f"{base_url}/urlCategories?customOnly=true"
        if is_custom_only
        else f"{base_url}/urlCategories",
    )
    return response


def lookup_url_classification(
    api_token: str, base_url: str, target_urls: list[str]
) -> dict[str, str]:
    """Lookup url category classifications to given url."""
    domains = [_extract_url_domain(url) for url in target_urls]
    response: Response = api.post(api_token, f"{base_url}/urlLookup", domains)
    return response


def create_custom_url_category(
    api_token: str,
    base_url: str,
    configured_name: str,
    urls: list[str],
    db_categorized_urls: list[str],
    description: Optional[str],
) -> str:
    payload = {
        "configuredName": configured_name,
        "urls": [_extract_url_domain(url) for url in urls],
        "dbCategorizedUrls": db_categorized_urls,
        "customCategory": True,
        "editable": True,
        "description": description,
        "superCategory": "USER_DEFINED",
        "urlsRetainingParentCategoryCount": 0,
        "type": "URL_CATEGORY",
    }
    response = api.post(api_token, f"{base_url}/urlCategories", payload)
    return response


def fetch_category_id_by_category_name(
    api_token: str, base_url: str, category_name: str
) -> str:
    categories: list[str] = fetch_url_categories(api_token, base_url)
    for category in categories:
        if category["customCategory"] is False:
            if category["id"] == category_name:
                return category["id"]
        else:
            if category["configuredName"] == category_name:
                return category["id"]
    return None


#  TODO: Does not work well. Improve
def update_custom_url_category(
    api_token: str,
    base_url: str,
    category_id: str,
    urls: list[str],
) -> str:
    """Update an existing Zscaler's url catergory."""
    response = api.put(api_token, f"{base_url}/urlCategories/{category_id}", urls)
    return response
