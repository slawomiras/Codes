from hello_for_test import hello

def test_default():
    assert hello() == "hello, world"
    
def test_argument():
    for name in ["Hermione", "Ron", "Harry"]:
        assert hello(name) == f"hello, {name}"

