import socket, time
def probe_tcp_port(host: str, port: int, timeout: float = 2.0) -> tuple:
    t0 = time.perf_counter()
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(timeout)
    try:
        sock.connect((host, port))
        sock.close()
        lat = (time.perf_counter() - t0) * 1000
        return True, round(lat, 2)
    except Exception as e:
        return False, 0.0
