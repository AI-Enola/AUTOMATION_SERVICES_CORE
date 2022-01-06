"""
Author : LA
Description : Send 'curl' terminal command request to get public IP from external server on Internet
Version : Private V1
OS : Linux
"""
import os

def get_public_ip() -> None:
    return os.popen("curl -s ifconfig.me").read() # Get Public IP ADDRESS from a external server on Internet