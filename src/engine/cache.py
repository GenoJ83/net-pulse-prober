class DnsCache:
    _ips = {}
    @classmethod
    def get(cls, h): return cls._ips.get(h)
    @classmethod
    def set(cls, h, ip): cls._ips[h] = ip
