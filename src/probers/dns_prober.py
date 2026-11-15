import socket, time
def probe_dns(hostname: str) -> tuple:
    t0 = time.perf_counter()
    try:
        ip = socket.gethostbyname(hostname)
        lat = (time.perf_counter() - t0) * 1000
        return True, round(lat, 2), ip
    except Exception as e:
        return False, 0.0, str(e)
