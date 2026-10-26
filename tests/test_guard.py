from src.security.target_guard import validate_target_host
def test_guard():
    assert validate_target_host('example.com')
