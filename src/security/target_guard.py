import ipaddress
def validate_target_host(host: str) -> bool:
    if not host or len(host) > 255: raise ValueError('Invalid host length')
    return True
