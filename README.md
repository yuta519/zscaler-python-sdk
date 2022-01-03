# Zscaler Python SDK
This is a Python SDK for Zscaler Internet Access. This client library is designed to support the Zscaler Internet Access (ZIA) API. Now This library does not support Zscaler Private Access (ZPA), but this will be implemented in the future.
This SDK has been developed mainly using Python 3.9.0 .

NOTE: This repository is not official. Zscaler does not support this repository.

## Preparation
---
You need a ZIA credentials like below.
- ZIA Admin Username (like `admin@example.com`)
- ZIA Admin Password
- ZIA Hostname (like `zscaler.net`)
- ZIA APIKEY (You need to request an api key to Zscaler support team.)

## Set profile
---
If you have verified your credentials, set up your credentials to use this repository. Please replace `/Users/utah18` to your arbitrary directory path.

```
$ mkdir /Users/utah18/.zscaler && cat > /Users/utah18/.zscaler/config.ini <<EOF
[zia]
USERNAME=example@example.com
PASSWORD=P@ssw0rd
HOSTNAME=zscaler.net
APIKEY=xxxxxxxxxxxxxxxxxxxxxxx
EOF
```

## Clone and Install Repository
---
In this case, we use `poetry`. If you don't have this, please install poetry from [HERE](https://python-poetry.org/docs/)
```
$ poetry add zscaler-python-sdk
```

## Quick Start
---
After installing, you can try below to check if you could use this library.
```
$ python
$ from zscaler_python_sdk.zia import Zia
$ zia = Zia("/Users/utah18/.zscaler/config.ini")
$print(zia.fetch_admin_users())
```

## Support Zscaler features
---
Below table has all features which this library could provides.
- ZIA
  | Category | Features | Notes |
  | --- | --- | --- |
  | Admin | Show admin roles | No supports to create new role |
  | Admin | Show admin users |  |
  | Admin | Create new admin users |  |
  | URL categories | Show URL categories |  |
  | URL categories | Lookup URL category from input URL |  |
  | URL categories | Create new custom URL category |  |
  | URL filtering rules | Show URL filtering rules |  |
  | URL filtering rules | Create new URL filtering rule |  |
  | URL filtering rules | Update existing rule |  |
  | Users | Show users |  |
  | Users | Show departments  |  |
  | Users | Show groups |  |


...
Reporting Issues
If you have bugs or other issues specifically pertaining to this library, file them here.

## References
- https://help.zscaler.com/zia/api
- https://help.zscaler.com/zia/zscaler-api-developer-guide
- https://help.zscaler.com/zia/sd-wan-api-integration
