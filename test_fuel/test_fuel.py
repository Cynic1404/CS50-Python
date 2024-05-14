from fuel import convert, gauge
import pytest

def test_happy_path():
    assert convert("1/2")==50 and gauge(50)=="50%"

def test_empty_1():
    assert convert("1/100")==1 and gauge(1)=="E"

def test_full_99():
    assert convert("99/100")==99 and gauge(99)=="F"

def test_full_100():
    gauge(100)=="F"


def test_calue_error():
    with pytest.raises(ValueError):
        convert("2/cat")

def test_zero_division():
    with pytest.raises(ZeroDivisionError):
        convert("1/0")

