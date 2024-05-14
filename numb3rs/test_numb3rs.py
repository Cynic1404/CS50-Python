from numb3rs import validate

def test_test():
    assert validate("1.1.1.1")
    assert validate("255.255.255.255")
    assert not validate("1.1.1.")
    assert not validate("1.1.1.256")
    assert not validate("zzz")

