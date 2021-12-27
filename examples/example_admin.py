# Please erase comment out, when you try examples below.


# from zscaler_python_sdk.admin import create_adminuser
# from zscaler_python_sdk.admin import fetch_adminroles

# from zscaler_python_sdk.admin import fetch_adminusers


"""
# You can fetch adminusers
adminusers = fetch_adminusers()
print(adminusers)

# If you manage multi ZIA account, could specify a tenant.
adminusers = fetch_adminusers(tenant="xxxxxxxxxxxx")
print(adminusers)
"""


"""
# You can fetch adminroles
adminroles = fetch_adminroles()
print(adminroles)

# If you manage multi ZIA account, could specify a tenant.
adminroles = fetch_adminroles(tenant="xxxxxxxxxxxx")
print(adminroles)
"""


"""
# You can create an adminuser.
create_adminuser_message = create_adminuser(
    loginName="test1@zscaler.net",
    userName="Yuta Kawamura",
    email="test1@zscaler.net",
    password="P@ssw0rd",
    rolename="Super Admin",
    tenant="xxxxxxxxxxxx",
)
print(create_adminuser_message)
"""

from zscaler_python_sdk.zia import Zia

zia = Zia("/Users/yuta519/work/zscaler-python-sdk/config/config.ini")
# print(zia.fetch_admin_users())
# print(zia.fetch_admin_roles())
# print(
#     zia.create_admin_users(
#         "test1@zscaler.net",
#         "Yuta Kawamura",
#         "test1@zscaler.net",
#         "P@ssw0rd",
#         "Super Admin",
#     )
# )
