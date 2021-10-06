from re import match
from typing import Any
from typing import Dict
from typing import List
from typing import Optional
from urllib.parse import urlparse

from zscaler_python_sdk.zia import api_get
from zscaler_python_sdk.zia import api_post
from zscaler_python_sdk.zia import api_put


def extract_url_domain(target_url):
    """Extract domain from url given by user."""
    url_pattern = "https?://[\w/:%#\$&\?\(\)~\.=\+\-]+"
    if match(url_pattern, target_url):
        parsed_url = urlparse(target_url)
        domain = parsed_url.netloc
        return domain
    else:
        return target_url


def fetch_url_categories(
    isCustomOnly: bool = False, tenant: str = None
) -> Dict[Any, Any]:
    """Get Zscaler's url catergories."""
    response = api_get(
        "/urlCategories?customOnly=true" if isCustomOnly else "/urlCategories",
        tenant=tenant,
    )
    return response


def create_custom_url_category(
    configured_name: str,
    urls: List[str],
    db_categorized_urls: List[str],
    description: Optional[str],
    tenant: Optional[str] = None,
) -> str:
    payload = {
        "configuredName": configured_name,
        "urls": urls,
        "dbCategorizedUrls": db_categorized_urls,
        "customCategory": True,
        "editable": True,
        "description": description,
        "superCategory": "USER_DEFINED",
        "urlsRetainingParentCategoryCount": 0,
        "type": "URL_CATEGORY",
    }
    response = api_post("/urlCategories", payload, tenant)
    return response


def update_custom_url_category(
    category_id: str,
    urls: List[str],
    tenant: Optional[str] = None,
) -> str:
    """Update an existing Zscaler's url catergory."""
    payload = {urls}
    response = api_put(f"/urlCategories/{category_id}", payload, tenant)

    return response.json()


def lookup_url_classification(
    target_urls: List[str],
    tenant: Optional[str] = None,
) -> Dict[str, str]:
    """Lookup url category classifications to given url."""
    domains = [extract_url_domain(url) for url in target_urls]
    response = api_post("/urlLookup", domains, tenant)

    return response
