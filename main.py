from zscaler_python_sdk.url_filtering_rules import fetch_all_url_filering_rules
from zscaler_python_sdk.admin import create_adminuser, fetch_adminusers
from zscaler_python_sdk.url_categories import create_custom_url_category
from zscaler_python_sdk.url_categories import fetch_url_categories
from zscaler_python_sdk.url_categories import lookup_url_classification

# from zscaler_python_sdk.url_categories import


# print(fetch_adminusers())

# print(create_adminuser(
#     loginName="test1@softbank-demo-05.com",
#     userName="Yuta Kawamura",
#     email="test1@softbank-demo-05.com",
#     password="P@ssw0rd",
#     rolename="Super Admin",
# ))


# print(fetch_url_categories())


# mess = create_custom_url_category(
#     configured_name="TEST CATEGORY",
#     urls=[".test.co.jp"],
#     db_categorized_urls=[],
#     description="This url category is created with API for test",
# )
# print(mess)

# create_adminuser(
#     loginName="test1@zscaler.net",
#     userName="Yuta Kawamura",
#     email="test1@zscaler.net",
#     password="P@ssw0rd",
#     rolename="Admin",
# )

# print(fetch_all_url_filering_rules())

# create_url_filering_rules(
#     name="Test Filtering Rule",
#     order=1,
#     protocols=["HTTPS_RULE"],
#     locations=[],
#     groups=[],
#     departments=[],
#     users=[],
#     url_categories=["GAMBLING"],
#     state="DISABLED",
#     rank=0,
#     action="ALLOW",
# )
# fetch_url_categories()
# classfication = lookup_url_classification(["aaa.com"])
# print(classfication)
# create_custom_url_category(
#     configured_name="TEST CATEGORY",
#     urls=[".test.co.jp"],
#     db_categorized_urls=[],
#     description="This url category is created with API for test",
# )

# print(lookup_url_classification(["hoge.com"]))

# print(fetch_all_url_filering_rules())
