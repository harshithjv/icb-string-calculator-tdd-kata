# import pytest
from string_calculator import StringCalculator

str_calc = StringCalculator()

def test_empty_string_return_0():
    assert str_calc.add("") == 0

def test_single_number_returns_number():
    assert str_calc.add("64") == 64

def test_multiple_numbers_returns_sum():
    assert str_calc.add("6,3") == 9
