import pytest
from math_operations import math_operations

def test_valid_operations():
    assert math_operations(10, 5, '+') == 15
    assert math_operations(10, 5, '-') == 5
    assert math_operations(10, 5, '*') == 50
    assert math_operations(10, 5, '/') == 2.0

def test_division_rounding():
    assert math_operations(10, 3, '/') == 3.33
    assert math_operations(7, 3, '/') == 2.33
    assert math_operations(1, 3, '/') == 0.33

def test_division_by_zero():
    with pytest.raises(ZeroDivisionError) as exc_info:
        math_operations(10, 0, '/')
    assert str(exc_info.value) == "Division par zéro impossible"

def test_invalid_operator():
    with pytest.raises(ValueError) as exc_info:
        math_operations(10, 5, '%')
    assert "Opérateur" in str(exc_info.value) 