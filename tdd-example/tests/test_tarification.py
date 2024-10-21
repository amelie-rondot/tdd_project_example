import pytest

from tdd_example.tarification import get_price


def test_get_price():
    # GIVEN a person who is 0 year old or 17 years old
    # WHEN apply 'get_price' function
    # EXPECT that the price to pay is 0 €

    # given
    ages = [0, 17]

    # expected
    expected_price = 0

    # result
    for age in ages:
        resulted_price = get_price(age)

        # assertion
        assert resulted_price == expected_price


def test_get_price2():
    # GIVEN a person who is 18 years old
    # WHEN apply 'get_price' function
    # EXPECT an exception is raised because this age is not 
    # between 0 and 17 years old

    # given
    age = 18

    # expect an exception is raised
    with pytest.raises(Exception):
        resulted_price = get_price(age)
