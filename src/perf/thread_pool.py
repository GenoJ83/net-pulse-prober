from concurrent.futures import ThreadPoolExecutor
def parallel_probes(targets, fn, workers=8):
    with ThreadPoolExecutor(max_workers=workers) as ex:
        return list(ex.map(fn, targets))
