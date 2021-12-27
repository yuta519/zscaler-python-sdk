# Please erase comment out, when you try examples below.

# from zscaler_python_sdk.url_categories import create_custom_url_category
# from zscaler_python_sdk.url_categories import fetch_url_categories
# from zscaler_python_sdk.url_categories import lookup_url_classification


"""
# You can fetch URL Categories
url_categories = fetch_url_categories()
print(url_categories)
"""


"""
# If you manage multi ZIA account, could specify a tenant.
url_categories = fetch_url_categories(tenant="xxxxxxxxx")
print(url_categories)
"""


"""
# You can create URL Categories
message = create_custom_url_category(
    configured_name="TEST CATEGORY",
    urls=[".test.co.jp"],
    db_categorized_urls=[],
    description="This url category is created with API for test",
    tenant="xxxxxxxxxxxxxxxx",
)
print(message)
"""


"""
# You can lookup a category in Zscaler which url is given of
url_category = lookup_url_classification(
    target_urls=["zscaler.net"],
    tenant="xxxxxxxxxxxxxxxx",
)
print(url_category)
"""


from zscaler_python_sdk.zia import Zia

zia = Zia("/Users/yuta519/work/zscaler-python-sdk/config/config.ini")
# print(zia.fetch_url_categories())
# print(zia.lookup_url_category(["softbank.com", "https://www.innoscouter.com/"]))
# print(
#     zia.create_custom_url_category(
#         "Kawamura Test Category",
#         ["https://yuta519.github.io"],
#         [],
#         "API test",
#     )
# )
# print(
#     zia.update_url_in_category("BlackList_URLCategories", ["https://yuta519.github.io"])
# )
