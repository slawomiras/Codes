from calculator_2_for_test import square

def main():
    test_square()

def test_square():
    try:
        assert square(4) == 16
    except AssertionError:
        print("4 squared was not 16")
    try:
        assert square(3) == 9
    except AssertionError:
        print("3 squared was not 9")

if __name__ == "__main__":
    main()
