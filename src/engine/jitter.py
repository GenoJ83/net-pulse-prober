import numpy as np
def compute_jitter(latencies: list) -> float:
    if len(latencies) < 2: return 0.0
    diffs = np.abs(np.diff(latencies))
    return float(round(np.mean(diffs), 2))
