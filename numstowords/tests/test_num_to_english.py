from numstowords.utils import convert_num_to_english
import pytest

# out of range
def test_below_range():
    with pytest.raises(ValueError):
        convert_num_to_english(-4) 

def test_above_range():
    with pytest.raises(ValueError):
        convert_num_to_english(1000000001)

# < 20

def test_single_digit():
    assert convert_num_to_english(2) == "two"
    assert convert_num_to_english(7) == "seven"

def test_teens():
    assert convert_num_to_english(13) == "thirteen"
    assert convert_num_to_english(19) == "nineteen"

# < 100
def test_just_tens():
    assert convert_num_to_english(30) == "thirty"

def test_double_digits():
    assert convert_num_to_english(32) == "thirty two"
    assert convert_num_to_english(56) == "fifty six"
    assert convert_num_to_english(97) == "ninety seven"

# < 1000
def test_just_hundreds():
    assert convert_num_to_english(400) == "four hundred"

def test_hundreds_and_ones():
    assert convert_num_to_english(602) == "six hundred two"
    assert convert_num_to_english(905) == "nine hundred five"

def test_hundreds_and_tens():
    assert convert_num_to_english(320) == "three hundred twenty"
    assert convert_num_to_english(590) == "five hundred ninety"

def test_triple_digits():
    assert convert_num_to_english(672) == "six hundred seventy two"
    assert convert_num_to_english(325) == "three hundred twenty five"
    assert convert_num_to_english(593) == "five hundred ninety three"
    assert convert_num_to_english(965) == "nine hundred sixty five"

# < million
def test_just_thousands():
    assert convert_num_to_english(4000) == "four thousand"

def test_mixed_places_thousands():
    assert convert_num_to_english(1602) == "one thousand six hundred two"
    assert convert_num_to_english(5905) == "five thousand nine hundred five"
    assert convert_num_to_english(1062) == "one thousand sixty two"
    assert convert_num_to_english(5095) == "five thousand ninety five"

def test_four_digits():
    assert convert_num_to_english(1672) == "one thousand six hundred seventy two"
    assert convert_num_to_english(3325) == "three thousand three hundred twenty five"
    assert convert_num_to_english(6593) == "six thousand five hundred ninety three"
    assert convert_num_to_english(9965) == "nine thousand nine hundred sixty five"

# < billion
def test_just_millions():
    assert convert_num_to_english(4000000) == "four million"

def test_mixed_places_millions():
    assert convert_num_to_english(1031602) == "one million thirty one thousand six hundred two"
    assert convert_num_to_english(5345905) == "five million three hundred forty five thousand nine hundred five"
    assert convert_num_to_english(10345905) == "ten million three hundred forty five thousand nine hundred five"