from calculator.calculator import Calculator
import pytest


def test_reset_memory():
    calc = Calculator(5)
    assert calc.reset_memory() == 0


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





# def test_add_subtract():
#     calc = Calculator()
#     calc.add(5)
#     calc.subtract(4)
#     assert calc.state == 1
#
#
# def test_multiply_divide():
#     calc = Calculator(2.0)
#     calc.multiply(6)
#     calc.divide(3)
#     assert calc.state == 4
#
#
# def test_default_state():
#     calc = Calculator()
#     assert calc.state == 0
#
#
# def test_type_int():
#     calc = Calculator(1)
#     assert isinstance(calc.state, int)
#
#
# def test_type_float():
#     calc = Calculator(1.0)
#     assert isinstance(calc.state, float)
#
#
# def test_action_error():
#     calc = Calculator()
#     with pytest.raises(TypeError):
#         calc.add('5')
#
#
# def test_initialize_error():
#     with pytest.raises(TypeError):
#         Calculator('5')