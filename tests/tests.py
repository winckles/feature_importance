from calculator.calculator_package import Calculator
import pytest


def test_reset_memory():
    calc = Calculator(5)
    assert calc.reset_memory() == 'The number in memory is now 0'


def test_correct_addition():
    calc = Calculator()
    assert calc.add(4) == 4


def test_correct_subtraction():
    calc = Calculator()
    assert calc.subtract(2) == -2


def test_correct_multiplication():
    calc = Calculator(10)
    assert calc.multiply(2) == 20


def test_correct_division():
    calc = Calculator(10)
    assert calc.divide(2) == 5


def test_divide_by_zero_error():
    calc = Calculator()
    with pytest.raises(ZeroDivisionError):
        calc.divide(0)


def test_take_root():
    calc = Calculator(16)
    assert calc.take_root(4) == 4


def test_take_root_by_zero_error():
    calc = Calculator()
    with pytest.raises(ZeroDivisionError):
        calc.take_root(0)
