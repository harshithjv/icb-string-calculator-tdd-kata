import pytest
from string_calculator import StringCalculator


str_calc = StringCalculator()

def test_empty_string_return_0():
    assert str_calc.add("") == 0

def test_single_number_returns_number():
    assert str_calc.add("64") == 64

def test_multiple_numbers_comma_delimited_returns_sum():
    assert str_calc.add("6,3") == 9

def test_multiple_numbers_multi_delimited_returns_sum():
    assert str_calc.add("6,3\n5,2\n8,4,2") == 30

def test_numbers_with_custom_delimiter_returns_sum():
    assert str_calc.add("//;\n5;2;8") == 15

@pytest.mark.parametrize("nums,expected_message", [
    ("-1,-2", "Negatives not allowed: -1"),
    ("8,-4,2,-5", "Negatives not allowed: -4,-5"),
])
def test_numbers_with_negative_number_should_raise_exception(nums, expected_message):
    with pytest.raises(ValueError, match=expected_message):
        str_calc.add(nums)

def test_numbers_return_sum_ignore_number_greater_than_thousand():
    assert str_calc.add("45,1551,55") == 100

def test_numbers_with_long_length_delimiter_returns_sum():
    assert str_calc.add("//[-.=]\n3-.=1-.=8") == 12
