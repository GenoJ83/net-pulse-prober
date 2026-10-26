from src.stats.uptime import calculate_uptime_sla
def test_uptime():
    assert calculate_uptime_sla(999, 1000) == 99.9
