from bank import value
import pytest

def test_happy():
    assert value("hello")==0
    assert value("hi")==20
    assert value("oops")==100

def test_negative():
    assert value("What’s up")!=20
    assert value("What’s up")!=0

def test_fromat():
    with pytest.raises(AttributeError):
            value(8)


def test_case_ins():
    assert value("Hello")==0
    assert value("Hi")==20
    assert value("Oops")==100


