def format_status_table(results: list) -> str:
    return '\n'.join(f'{r.get("target")} | {"UP" if r.get("is_alive") else "DOWN"}' for r in results)
