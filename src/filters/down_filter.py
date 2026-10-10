def filter_unreachable_targets(results: list):
    return [r for r in results if not r.get('is_alive')]
