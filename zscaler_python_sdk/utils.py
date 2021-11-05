from typing import List

from zscaler_python_sdk import url_categories


def translate_category_from_name_to_id(
    category_names: List[str],
    tenant: str,
) -> List[str]:
    all_url_categories = url_categories.fetch_url_categories(tenant=tenant)
    category_id_list: List[str] = []
    for cateogry in all_url_categories[tenant]:
        if "configuredName" in cateogry.keys():
            if cateogry["configuredName"] in category_names:
                category_id_list.append(cateogry["id"])
        if cateogry["id"] in category_names:
            category_id_list.append(cateogry["id"])
    return category_id_list
