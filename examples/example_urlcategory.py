# from zscaler_python_sdk.url_categories import create_custom_url_category
# from zscaler_python_sdk.url_categories import fetch_url_categories


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
