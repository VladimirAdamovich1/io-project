from eat_it.app import ping

UNIMPLEMENTED = 501

def test_ping_returns_501_response():
    result = ping()
    assert result.status_code == UNIMPLEMENTED

def test_ping_returns_hello_message():
    result = ping()
    assert result.json == {"message": "Hello"}

def test_ping_returns_content_type_header():
    result = ping()
    assert result.headers["Content-Type"] == "application/json"
