import pytest
from app.core import Calculator

@pytest.fixture
def calculator():
    return Calculator()

def test_add(calculator):
    assert calculator.add(1, 2) == 3

def test_subtract(calculator):
    assert calculator.subtract(2, 1) == 1

def test_multiply(calculator):
    assert calculator.multiply(2, 1) == 2

def test_divide(calculator):
    assert calculator.divide(8, 2) == 4
