from pydantic import BaseModel
class ProbeResult(BaseModel):
    target: str
    probe_type: str
    is_alive: bool
    latency_ms: float
    error: str = None
