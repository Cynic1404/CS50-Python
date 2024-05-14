from um import count

def test_positive():
    assert count("um?")==1
    assert count("Um, thanks for the album.")==1
    assert count("Um, thanks, um...")==2
