
import pyotp
from kiteconnect import KiteConnect
from utils.config_loader import load_credentials

def get_access_token(user):
    kite = KiteConnect(api_key=user['api_key'])
    totp = pyotp.TOTP(user['totp_secret']).now()
    print(f"Login {user['user_id']} with OTP: {totp}")
    return f"TOKEN_{user['user_id']}"

def generate_tokens():
    creds = load_credentials()
    tokens = {"master": {}, "slaves": []}

    tokens['master']['user_id'] = creds['master']['user_id']
    tokens['master']['access_token'] = get_access_token(creds['master'])

    for slave in creds['slaves']:
        tokens['slaves'].append({
            "user_id": slave['user_id'],
            "access_token": get_access_token(slave)
        })

    return tokens
