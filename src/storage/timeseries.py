def append_latency_record(path: str, line: str):
    with open(path, 'a') as f: f.write(line + '\n')
