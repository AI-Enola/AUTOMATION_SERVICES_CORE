"""
Author : LA
Description : Send 'curl' terminal command request to get website status
Version : Publice V1
OS : Linux

Commande to use : curl -Is 127.0.0.1/home | head -n 1 - REPLACE WITH YOUR WEBSITE IP ADDRESS
"""

import os

def get_website_status() -> None:
    return os.popen("curl -Is 127.0.0.1/home | head -n 1").read() # Get Website status, if return None then website is down - REPLACE WITH YOUR WEBSITE IP ADDRESS