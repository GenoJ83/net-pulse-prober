import json
def export_health_json(data: dict) -> str:
    return json.dumps(data, indent=2)
