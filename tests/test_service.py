import pytest

from app.service import add, divide


def test_add():
    a, b = 2, 3
    result = add (a, b)
    assert result == 5

def test_add_negative():
    assert add(-2, -3) == -5

def test_add_float():
    assert add(0.5, 0.25) == 0.75

def test_divide():
    assert divide(10, 2) == 5

def test_divide_float():
    assert divide(1, 4) == 0.25

def test_divide_by_zero():
    with pytest.raises(ValueError):
        divide(10, 0)
