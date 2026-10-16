import argparse
def get_parser():
    p = argparse.ArgumentParser(prog='net-pulse')
    p.add_argument('target', nargs='?', default='1.1.1.1')
    p.add_argument('--port', type=int, default=80)
    return p
