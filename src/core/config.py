from pydantic import BaseModel
class ProberConfig(BaseModel):
    timeout_seconds: float = 2.0
    dns_server: str = '8.8.8.8'
    retries: int = 3
