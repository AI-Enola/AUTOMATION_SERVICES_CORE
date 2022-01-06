import re

def check_ip(ip=str) -> object:
    return re.search("((25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)(\.|$)){4}", ip) # If match not found return None else it return match object