import pytest
from operations import addition, soustraction, multiplication, division

def test_addition():
    assert addition(5, 3) == 8
    assert addition(-1, 1) == 0
    assert addition(0, 0) == 0

def test_soustraction():
    assert soustraction(5, 3) == 2
    assert soustraction(1, 1) == 0
    assert soustraction(0, 5) == -5

def test_multiplication():
    assert multiplication(5, 3) == 15
    assert multiplication(-2, 3) == -6
    assert multiplication(0, 5) == 0

def test_division():
    assert division(6, 2) == 3
    assert division(5, 2) == 2.5
    assert division(-6, 2) == -3

def test_division_by_zero():
    with pytest.raises(ZeroDivisionError):
        division(5, 0) 