from app.main import hello_world

def test_hello_world():
    msg = hello_world()
    assert msg == "Hello World!"