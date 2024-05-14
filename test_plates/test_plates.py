from plates import is_valid


def test_happy():
    assert is_valid("CS50")

def test_length():
    assert not is_valid("C")
    assert is_valid("AA")
    assert is_valid("ABCDEF")
    assert  not is_valid("ABCDEFE")

def test_starts_with():
    assert is_valid("ABcd")
    assert not is_valid("A1")


def test_happy_only_letters():
    assert is_valid("CSAAA")

def test_negative_first_zero():
    assert not is_valid("CS05")

def test_negative_ends_with_letter():
    assert not is_valid("CS50P")

def test_negative_special_character():
    assert not is_valid("PI3.14")


def test_negative_starts_with_number():
    assert not is_valid("1BCDEF")

def test_negative_max_lenghth():
    assert is_valid("ABCDEF")
