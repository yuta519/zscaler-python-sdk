# Please erase comment out, when you try examples below.

# from zscaler_python_sdk.users import fetch_departments
# from zscaler_python_sdk.users import fetch_groups

# from zscaler_python_sdk.users import fetch_users

"""
# You can fetch users
users = fetch_users(
    size=10,
    tenant="softbank-demo-05",
)
print(users)
"""

"""
departments = fetch_departments(
    search="DevSecOps推進部1課",
    tenant="softbank-demo-05",
)
print(departments)
"""

"""
groups = fetch_groups(
    search="Zscaler",
    tenant="softbank-demo-05",
)
print(groups)
"""

from zscaler_python_sdk.zia import Zia

zia = Zia("/Users/yuta519/work/zscaler-python-sdk/config/config.ini")
print(zia.api_key)
print(zia.login())
