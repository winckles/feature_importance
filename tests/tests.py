from calculator.calculator import Calculator


def test_correct_addition():
    assert Calculator(2, 2).add == 4


def test_correct_subtraction():
    assert Calculator(3, 1).subtract == 2


def test_correct_division():
    assert Calculator(10, 2).divide == 5


def test_correct_multiplication():
    assert Calculator(10, 2).multiply == 20
