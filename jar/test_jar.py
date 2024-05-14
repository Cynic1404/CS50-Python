import pytest

from jar import Jar
import random

jar_to_test = Jar(12, 0)

def test_deposit():
    size_before = jar_to_test.size
    random_value = random.randint(0, jar_to_test.capacity-jar_to_test.size)
    jar_to_test.deposit(random_value)
    assert size_before+random_value == jar_to_test.size

def test_overdeposit():
    with pytest.raises(ValueError):
        jar_to_test.deposit(100)


def test_withdraw():
    size_before = jar_to_test.size
    random_value = random.randint(0, jar_to_test.size)
    jar_to_test.withdraw(random_value)
    assert size_before-random_value == jar_to_test.size

def test_overwithdraw():
    with pytest.raises(ValueError):
        jar_to_test.withdraw(99999)
