def calculate_uptime_sla(success_count: int, total_count: int) -> float:
    if total_count == 0: return 100.0
    return round((success_count / total_count) * 100.0, 3)
