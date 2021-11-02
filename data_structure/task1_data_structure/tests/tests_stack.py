"""Tests for task data structures:
linked list, stack, queue, hash table, tree, graph"""

from random import randint
import pytest

from task1_data_structures import Stack
from convert_to_list import convert_to_list


@pytest.mark.parametrize("array",
                         [[randint(-50, 50) for _ in range(100)],
                          [randint(-50, 50) for _ in range(50)],
                         [randint(-500, 500) for _ in range(100)]]
                         )
def test_push(array):
    """Test stack push methods
    that add new element at first position.

    :argument  array - randomly gen list"""
    # create LikedList
    push_linked_list = Stack(25)
    # add each new item on first position
    for item in reversed(array):
        push_linked_list.push(item)
    array.append(25)
    assert convert_to_list(push_linked_list) == array


@pytest.mark.parametrize("array",
                         [[randint(-50, 50) for _ in range(100)],
                          [randint(-150, 150) for _ in range(100)],
                         [randint(-500, 500) for _ in range(100)]]
                         )
def test_delete(array):
    """Test stack pop methods
    that returns value from stack and delete node.

    :argument  array - randomly gen list"""
    # create LikedList
    pop_linked_list = Stack(25)
    # add each new item on last position
    for item in reversed(array):
        pop_linked_list.push(item)
    array.append(25)

    for _ in range(20):
        temp1 = pop_linked_list.pop()
        temp2 = array.pop(0)
        assert temp1 == temp2
    assert convert_to_list(pop_linked_list) == array


def test_peek(array = [0, 1, 3]):
    """Test peek stack method"""
    # create LikedList
    peek_linked_list = Stack(25)
    # add each new item on last position
    for item in reversed(array):
        peek_linked_list.push(item)
    array.append(25)

    assert peek_linked_list.peek() == array[0]