import requests
import json
import os
from datetime import datetime, timedelta
from config import settings

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
TOKEN_DIR = os.path.join(BASE_DIR, "data", "token")
TOKEN_FILE = os.path.join(TOKEN_DIR, "access_token.json")


def generate_access_token():
    url = "https://accounts.zoho.com/oauth/v2/token"

    params = {
        "refresh_token": settings.zoho_refresh_token,
        "client_id": settings.zoho_client_id,
        "client_secret": settings.zoho_client_secret,
        "grant_type": "refresh_token",
    }

    resp = requests.post(url, params=params)
    if not resp.ok:
        raise RuntimeError(f"Zoho OAuth error {resp.status_code}: {resp.text}")

    data = resp.json()
    return data["access_token"], data["expires_in"]


def create_token_file():
    os.makedirs(TOKEN_DIR, exist_ok=True)

    token, expires_in = generate_access_token()

    expires_at = datetime.utcnow() + timedelta(seconds=expires_in - 600)

    payload = {
        "token": token,
        "expires_at": expires_at.isoformat(),
    }

    with open(TOKEN_FILE, "w") as f:
        json.dump(payload, f, indent=3)

    return token


def get_access_token():
    try:
        with open(TOKEN_FILE, "r") as f:
            data = json.load(f)

        expires_at = datetime.fromisoformat(data["expires_at"])

        if datetime.utcnow() >= expires_at:
            return create_token_file()

        return data["token"]

    except (FileNotFoundError, json.JSONDecodeError, KeyError):
        return create_token_file()


if __name__ == "__main__":
    token = get_access_token()
    print("Access token OK:", token[:25], "...")





