from src.cli.args import get_parser
def test_cli():
    p = get_parser()
    args = p.parse_args(['google.com', '--port', '443'])
    assert args.target == 'google.com'
    assert args.port == 443
