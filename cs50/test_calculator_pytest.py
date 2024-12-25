from calculator_2_for_test import square

def test_positive():
    assert square(2) == 4
    assert square(3) == 9
    
def test_negative():
    assert square(-2) == 4
    assert square(-3) == 9
    
def test_zeo():
    assert square(0) == 0
    