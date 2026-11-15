from src.engine.jitter import compute_jitter
def test_jitter():
    assert compute_jitter([10.0, 12.0, 11.0, 15.0]) > 0.0
