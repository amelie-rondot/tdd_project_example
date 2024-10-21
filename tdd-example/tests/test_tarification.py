from tdd_example.tarification import get_price

def test_get_price():
    # GIVEN a person who is 0 year old
    # WHEN apply 'get_price' function
    # EXPECT that the price to pay is 0 €
    
    # given 
    age = 0
    
    # expected
    expected_price = 0
    
    # result
    resulted_price = get_price(age)
    
    # assertion
    assert resulted_price == expected_price
    