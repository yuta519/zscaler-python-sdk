# Please erase comment out, when you try examples below.

# from zscaler_python_sdk.firewall_rules import fetch_firewall_rules
# from zscaler_python_sdk.firewall_rules import fetch_ip_destination_groups
# from zscaler_python_sdk.firewall_rules import fetch_ip_source_groups
# from zscaler_python_sdk.firewall_rules import fetch_network_application_groups
# from zscaler_python_sdk.firewall_rules import fetch_network_applicatios

"""
# You can fetch firewall rules
firewall_rules = fetch_firewall_rules(
    tenant="xxxxxxxxxxxx",
)
print(firewall_rules)
"""

"""
# You can fetch a specific firewall rule
specific_firewall_rules = fetch_firewall_rules(
    rule_id=541982,
    tenant="xxxxxxxxxxxx",
)
print(specific_firewall_rules)
"""

"""
ip_destination_groups = fetch_ip_destination_groups(tenant="xxxxxxxxxxxx")
print(ip_destination_groups)
"""


"""
ip_destination_groups = fetch_ip_destination_groups(
    ip_group_id=927590,
    tenant="xxxxxxxxxxxx",
)
print(ip_destination_groups)
"""

"""
ip_source_groups = fetch_ip_source_groups(
    tenant="xxxxxxxxxxxx",
)
print(ip_source_groups)
"""


"""
nw_app_groups = fetch_network_application_groups(
    tenant="xxxxxxxxxxxx",
)
print(nw_app_groups)
"""

"""
nw_apps = fetch_network_applicatios(
    tenant="xxxxxxxxxxxx",
)
print(nw_apps)
"""

from zscaler_python_sdk.zia import Zia

zia = Zia("/Users/yuta519/work/zscaler-python-sdk/config/config.ini")
# print(zia.fetching_all_fw_rules())
# print(zia.fetching_one_fw_rule("Office 365 One Click Rule"))
print(
    zia.create_fw_rule(
        "test fw rule",
        1,
        "READ_WRITE",
        False,
        0,
        [],
        "BLOCK_RESET",
        "ENABLED",
        "api test rule",
        [],
        [],
        [],
    )
)
