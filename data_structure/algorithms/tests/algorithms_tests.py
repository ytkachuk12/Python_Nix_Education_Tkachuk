"""Tests for task algorithms"""

from math import factorial
from random import randint
import pytest

import algorithms


def generate_pseudo_random_list(minimum, maximum, length):
    """generate pseudo random numbers in min - max range
    and make a list with input length
    Return list and list.sort"""
    # seed(50)
    my_list = [randint(minimum, maximum) for _ in range(length)]
    return my_list, my_list.sort()


@pytest.mark.parametrize("array, num, expected", [
    (tuple(range(100)), 3, 3), (tuple(range(-10, 50)), -10, 0),
    (tuple(range(10)), 20, -1), ((1,), 1, 0)
    ])
def test_binary_search(array, num, expected):
    """Test binary search func in algorithms.py"""
    assert algorithms.binary_search(array, num) == expected


@pytest.mark.parametrize("array, expected", [
    (generate_pseudo_random_list(0, 500, 100)),
    (generate_pseudo_random_list(-25, 50, 125)),
    ([1], [1]),
    ])
def test_quick_sort_iterative(array, expected):
    """Test quick sort func in algorithms.py"""
    assert algorithms.quick_sort_iterative(array) == expected


@pytest.mark.parametrize("num, expected", [
    (15, factorial(15)), (7, factorial(7)), (25, factorial(25))
    ])
def test_recursion_factorial(num, expected):
    """Test recursion_factorial func in algorithms.py"""
    assert algorithms.recursion_factorial(num) == expected


def test_raise_error():
    """Test recursion_factorial func
    Raises:
            TypeError: in case if number is not type int
    """
    with pytest.raises(TypeError):
        algorithms.recursion_factorial(7.6)
