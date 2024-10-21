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
    # GIVEN a person who is older than 17 years old
    # WHEN apply 'get_price' function
    # EXPECT an exception is raised because this age is not 
    # between 0 and 17 years old

    # given
    ages = [18, 20]

    for age in ages:
        # expect an exception is raised
        with pytest.raises(Exception):
            resulted_price = get_price(age)


def test_get_price3():
    # GIVEN a person whose given age is -1 year old
    # WHEN apply 'get_price' function
    # EXPECT an exception is raised because this age is an invalid age

    # given
    age = -1
    
    # expected
    error_message = (
        "L'âge de la personne que vous avez renseigné, "
        f"{age} ans, est négatif ! Ce n'est pas une valeur valide."
    )

    # expect an exception is raised
    with pytest.raises(Exception) as exc_info:
        resulted_price = get_price(age)
        
    # except a specific err
    resulted_error_message = exc_info.value.args[0]
    
    # assertion
    assert resulted_error_message == error_message

