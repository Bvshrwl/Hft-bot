
import asyncio
from utils.config_loader import load_credentials
from token.totp_login import generate_tokens
from master.check_positions import get_master_positions
from slaves.copy_trade import copy_to_slave

import time

def main():
    creds = load_credentials()
    tokens = generate_tokens()

    previous = None

    while True:
        current = get_master_positions()
        if current != previous:
            print(f"[MASTER] Detected change: {current}")
            asyncio.run(send_to_slaves(tokens['slaves'], current))
            previous = current
        time.sleep(1)

async def send_to_slaves(slaves, position):
    tasks = [copy_to_slave(slave, position) for slave in slaves]
    await asyncio.gather(*tasks)

if __name__ == "__main__":
    main()
