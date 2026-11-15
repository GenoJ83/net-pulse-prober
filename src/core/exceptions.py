class NetPulseError(Exception): pass
class DnsLookupError(NetPulseError): pass
class TcpConnectionError(NetPulseError): pass
