from zscaler_python_sdk.lib.zpa import auth


class Zpa(object):
    def __init__(self, customer_id: str, client_id: str, client_secret: str) -> None:
        self.customer_id: str = customer_id
        self.client_id: str = client_id
        self.client_secret: str = client_secret
        self.access_token: str = auth.login(self.client_id, self.client_secret)

    def login(self):
        print(self.access_token)
        print(auth.logout(self.access_token))
