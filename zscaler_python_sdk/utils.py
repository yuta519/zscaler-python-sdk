from typing import Optional

from zscaler_python_sdk import url_categories


def translate_category_from_name_to_id(
    category_name: str,
    tenant: str,
) -> Optional[str]:
    all_url_categories = url_categories.fetch_url_categories(
        isCustomOnly=True,
        tenant=tenant,
    )
    category_id: Optional[str] = None
    for cateogry in all_url_categories[tenant]:
        if cateogry["configuredName"] == category_name:
            category_id = cateogry["id"]
    return category_id
