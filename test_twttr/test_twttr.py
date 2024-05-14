
from twttr import shorten

def test_lala():
    assert shorten("lala") == "ll"


def test_hry():
    assert shorten("How are you?") == "Hw r y?"

def test_low():
    assert shorten("Hey, i an Actor") == "Hy,  n ctr"

def test_numbers():
    assert shorten("777") == "777"
