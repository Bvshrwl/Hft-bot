
import json

def load_credentials():
    with open("config/credentials.json") as f:
        return json.load(f)
