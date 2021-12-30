# Zscaler Python SDK
This is a Python SDK for Zscaler Internet Access. This client library is designed to support the Zscaler Internet Access (ZIA) API. Now This library does not support Zscaler Private Access (ZPA), but this will be implemented in the future.

This SDK has been developed mainly using Python 3.8.5 on Ubuntu 20.04 LTS (Focal Fossa).

NOTE: This repository is not official. Zscaler does not support this repository.

## Preparation
You need a ZIA credentials like below.
- ZIA Admin Username (like `admin@example.com`)
- ZIA Admin Password
- ZIA Hostname (like `zscaler.net`)
- ZIA APIKEY (You need to request an api key to Zscaler support team.)

## Set profile
If you have verified your credentials, set up your credentials to use this repository.

$ mkdir ~/.zscaler && cat > ~/.zscaler/config.yaml <<EOF
[zia]
USERNAME=example@example.com
PASSWORD=P@ssw0rd
HOSTNAME=zscaler.net
APIKEY=xxxxxxxxxxxxxxxxxxxxxxx
EOF

### Clone and Install Repository

...
Reporting Issues
If you have bugs or other issues specifically pertaining to this library, file them here.

References
https://help.zscaler.com/zia/api
https://help.zscaler.com/zia/zscaler-api-developer-guide
https://help.zscaler.com/zia/sd-wan-api-integration
