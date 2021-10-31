"""some tests for main.py"""
from datetime import datetime
import pytest
from freezegun import freeze_time

import main


@pytest.mark.parametrize("test_input,expected", [
                         (4, "even"), (7, "odd"), (-128, "even"), (-24, "even")
                         ])
def test_even_odd(test_input, expected):
    """Test even_odd func in main.py.
    Args:
        test_input (int): number to check.
        expected (str): result of check. `even` if given number is even
                        and `odd` if the number is odd.
    """
    assert main.even_odd(test_input) == expected


@pytest.mark.parametrize("num1,num2,num3,expected", [
                         (1, 2, 3, 6), (2, -2, -2.75, -2.75), (0.00, 4.544, 1.0000, 5.5440)
                         ])
def test_sum_all(num1, num2, num3, expected):
    """Test sum_all func in main.py
    Args:
        num1, num2, num3 (int or float): numbers for sum.
        expected (int or float): result of sum
    """
    assert main.sum_all(num1, num2, num3) == expected


@freeze_time("Jan 14th, 2018, 23:20")
def test_time_of_day():
    """Test time_of_day func in main.py.
    Using FreezeGun library that allows Python tests to travel through time
    by mocking the datetime module.
    """
    print(datetime.now())
    assert main.time_of_day() == "night"


@pytest.fixture
def product():
    """Returns a Product instance 'oranges' for 3.7$(10 kilo)"""
    return main.Product("orange", 3.7, 10)


@pytest.mark.parametrize("subtract_product, add_product, expected", [
                         (5, 25, 30), (2, 6, 14),
                         ])
def test_change_quantity(product, subtract_product, add_product, expected):
    """Test change add_quantity and subtract_quantity methods in Product class in main.py.
    Args:
        subtract_product, add_product (int): number of products
                                            available to subtract or add.
        expected (int): number of products left
        """
    product.subtract_quantity(subtract_product)
    product.add_quantity(add_product)
    assert product.quantity == expected


def test_change_price(product):
    """Test change_price method in Product class in main.py
    Args:
        _ (float): the price to change to.
    """
    product.change_price(3.9)
    assert product.price == 3.9


@pytest.fixture
def empty_shop():
    """Returns a Shop instance with no products"""
    return main.Shop()


@pytest.fixture
def shop():
    """Returns a Shop instance with some products"""
    product = main.Product("cherry", 5, 25)
    product1 = main.Product("candy", 2.25, 12)
    return main.Shop([product, product1])


def test_add_product(empty_shop, shop, product):
    """Test add_product method in Shop class in main.py
    Args:
        shop, empty_shop (Shop): instance Shop
        product (Product): product to add to the shop.
    """
    empty_shop.add_product(product)
    shop.add_product(product)
    assert empty_shop.products[0] is product
    assert shop.products[-1] is product


@pytest.mark.parametrize("product_title, expected", [
                         ("cherry", 0), ("candy", 1), ("peach", None)
                         ])
def test_get_product_index(shop, product_title, expected):
    """Test _get_product_index method in Shop class in main.py
    Args:
        shop (Shop): instance Shop
        product_title (str): title of the product to look for.
    Returns:
        excepted: the index of the product if it present in the shop else None
    """
    assert shop._get_product_index(product_title) == expected


@pytest.mark.parametrize("product_title, qty_to_sell, expected", [
                         ("cherry", 10, 50), ("candy", 8, 18.00), ("cherry", 15, 75)
                         ])
def test_sell_product(shop, product_title, qty_to_sell, expected):
    """Test sell_product method in Shop class in main.py
    Args:
            product_title (str): the title of the product to sell.
            qty_to_sell (int, optional): the quantity of the product to sell.
                Defaults to 1."""
    assert shop.sell_product(product_title, qty_to_sell) == expected


def test_raise_error(shop):
    """Test sell_product method in Shop class in main.py
    Raises:
            ValueError: in case if amount of available products
                of that type is less then given."""
    with pytest.raises(ValueError):
        shop.sell_product("candy", 14)
