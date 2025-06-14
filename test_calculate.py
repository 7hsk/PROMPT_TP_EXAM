import pytest
from calculate import calculate

def test_valid_operations():
    assert calculate(10, 5, '+') == 15
    assert calculate(10, 5, '-') == 5
    assert calculate(10, 5, '*') == 50
    assert calculate(10, 5, '/') == 2.0

def test_division_rounding():
    assert calculate(10, 3, '/') == 3.33
    assert calculate(7, 3, '/') == 2.33
    assert calculate(1, 3, '/') == 0.33

def test_division_by_zero():
    with pytest.raises(ZeroDivisionError):
        calculate(10, 0, '/')

def test_invalid_operator():
    with pytest.raises(ValueError):
        calculate(10, 5, '%')
    with pytest.raises(ValueError):
        calculate(10, 5, '^') 