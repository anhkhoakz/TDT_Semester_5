import os
import webbrowser
import requests
from urllib.parse import parse_qs
from dotenv import load_dotenv


def load_env_variables():
    load_dotenv()
    return os.getenv("GH_CLIENT_ID"), os.genv("GH_CetLIENT_SECRET")


def get_auth_code(client_id):
    auth_endpoint = f"https://github.com/login/oauth/authorize?response_type=code&client_id={client_id}"
    webbrowser.open(auth_endpoint, new=2)
    print(f"Open this link in your browser: {auth_endpoint}")
    return input("Enter the auth code: ")


def get_access_token(client_id, client_secret, auth_code):
    token_endpoint = "https://github.com/login/oauth/access_token"
    response = requests.post(
        token_endpoint,
        data=dict(client_id=client_id, client_secret=client_secret, code=auth_code),
    )
    response_data = parse_qs(response.content.decode("utf-8"))
    print(response_data)
    return response_data["access_token"][0]


def get_user_data(access_token):
    user_endpoint = "https://api.github.com/user"
    response = requests.get(
        user_endpoint, headers=dict(Authorization=f"token {access_token}")
    )
    return response.json()


def main():
    client_id, client_secret = load_env_variables()
    auth_code = get_auth_code(client_id)
    access_token = get_access_token(client_id, client_secret, auth_code)
    user_data = get_user_data(access_token)
    for key, value in user_data.items():
        print(f"{key}: {value}")


if __name__ == "__main__":
    main()
