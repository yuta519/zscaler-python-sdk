from typing import Dict
from typing import List

from zscaler_python_sdk import url_categories


def translate_category_from_name_to_id(
    category_names: List[str],
    tenant: str,
) -> Dict[str, str]:
    all_url_categories = url_categories.fetch_url_categories(
        isCustomOnly=True,
        tenant=tenant,
    )
    category_id_list: dict[str, str] = {}
    for cateogry in all_url_categories[tenant]:
        if cateogry["configuredName"] in category_names:
            category_id_list[cateogry["configuredName"]] = cateogry["id"]
    return category_id_list
