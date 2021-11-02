"""Tests for task data structures:
linked list, stack, queue, hash table, tree, graph"""

from random import randint
import pytest

from task1_data_structures import Queue
from convert_to_list import convert_to_list


@pytest.mark.parametrize("array",
                         [[randint(-50, 50) for _ in range(100)],
                          [randint(-50, 50) for _ in range(50)],
                         [randint(-500, 500) for _ in range(100)]]
                         )
def test_enqueue(array):
    """Test queue enqueue methods
    that add new element at last position.

    :argument  array - randomly gen list"""
    # create queue
    enqueue_linked_list = Queue(25)
    # add each new item on last position
    for item in array:
        enqueue_linked_list.enqueue(item)
    array.insert(0, 25)
    assert convert_to_list(enqueue_linked_list) == array



@pytest.mark.parametrize("array",
                         [[randint(-50, 50) for _ in range(100)],
                          [randint(-150, 150) for _ in range(100)],
                         [randint(-500, 500) for _ in range(100)]]
                         )
def test_dequeue(array):
    """Test queue dequeue methods
    that returns value and delete delete node.

    :argument  array - randomly gen list"""
    # create LikedList
    dequeue_linked_list = Queue(25)
    # add each new item on last position
    for item in array:
        dequeue_linked_list.enqueue(item)
    array.insert(0, 25)

    for _ in range(20):
        temp1 = dequeue_linked_list.dequeue()
        temp2 = array.pop(0)
        assert temp1 == temp2
    assert convert_to_list(dequeue_linked_list) == array


def test_peek(array = [0, 1, 3]):
    """Test peek queue method"""
    # create LikedList
    peek_linked_list = Queue(25)
    # add each new item on last position
    for item in array:
        peek_linked_list.enqueue(item)
    array.insert(0, 25)

    assert peek_linked_list.peek() == array[0]