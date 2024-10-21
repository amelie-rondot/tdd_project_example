import pytest

from tdd_example.tarification import get_price


def test_get_price():
    # GIVEN a person who is beatween 0 and 17 years old
    # WHEN apply 'get_price' function
    # EXPECT that the price to pay is 0 €

    # given
    ages = [0, 10, 17]

    # expected
    expected_price = 0

    # result
    for age in ages:
        resulted_price = get_price(age)

        # assertion
        assert resulted_price == expected_price


def test_get_price2():
    # GIVEN a person who is not between 0 and 17 years old
    # WHEN apply 'get_price' function
    # EXPECT an exception is raised

    # given
    ages = [-1, 18, 20]

    # expected
    detail_error_messages = [
        "est négatif ! Ce n'est pas une valeur valide.",
        "n'est pas compris entre 0 et 17 ans inclus.",
        "n'est pas compris entre 0 et 17 ans inclus.",
    ]

    # result
    for age, detail_error_message in zip(ages, detail_error_messages):
        # expect an exception is raised
        with pytest.raises(Exception) as exc_info:
            resulted_price = get_price(age)

        resulted_error_message = exc_info.value.args[0]

        # assertion
        assert detail_error_message in resulted_error_message
