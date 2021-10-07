# Please erase comment out, when you try examples below.

# from zscaler_python_sdk.url_filtering_rules import create_url_filering_rules
# from zscaler_python_sdk.url_filtering_rules import fetch_all_url_filering_rules

"""
# You can fetch URL Filtering Rules
url_filering_rules = fetch_all_url_filering_rules(
    tenant="xxxxxxxxxxxxxxxxxxx",
)
print(url_filering_rules)
"""

"""
# You can fetch full information of URL Filtering Rules
url_filering_rules = fetch_all_url_filering_rules(
    isFull=True,
    tenant="xxxxxxxxxxxxxxxxxxx",
)
print(url_filering_rules)
"""


"""
# Create a new URL Filtering Rule
message = create_url_filering_rules(
    name="Test Filtering Rule",
    order=1,
    protocols=["HTTPS_RULE"],
    locations=[],
    groups=[],
    departments=[],
    users=[],
    url_categories=["GAMBLING"],
    state="DISABLED",
    rank=0,
    action="ALLOW",
    tenant="xxxxxxxxxxxxxxxxxx",
)
print(message)
"""
