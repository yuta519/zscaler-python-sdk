import requests


def login(client_id: str, client_secret: str):
    url = "https://config.private.zscaler.com/signin"
    payload: dict[str, str] = {
        "client_id": client_id,
        "client_secret": client_secret,
    }
    headers: dict[str, str] = {
        "Content-Type": "application/x-www-form-urlencoded",
    }
    response = requests.request("POST", url, headers=headers, data=payload).json()
    return f"{response['token_type']} {response['access_token']}"


def logout(access_token: str) -> None:
    url = "https://config.private.zscaler.com/signout"
    payload = {}
    headers: dict[str, str] = {
        "Content-Type": "application/json",
        "Authorization": access_token,
    }
    requests.request("POST", url, headers=headers, data=payload)
