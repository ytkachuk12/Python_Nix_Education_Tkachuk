"""Tests for task data structures:
linked list, stack, queue, hash table, tree, graph"""

from random import randint, sample
import pytest

from task1_data_structures import BinarySearchTree


@pytest.mark.parametrize("array",
                         [[randint(-50, 50) for _ in range(100)],
                          [randint(-50, 50) for _ in range(100)],
                         [randint(-500, 500) for _ in range(100)]]
                         )
def test_insert_lookup(array):
    """Test binary tree insert methods
    that insert value in the tree by
    checking lookup returns proper value

    :argument  array - randomly gen list"""
    # create BinaryTree
    insert_binary_tree = BinarySearchTree(1125)
    # add each new item on first position
    for item in array:
        insert_binary_tree.insert(item)

    # check lookup return proper value
    for value in array:
        returns_value = insert_binary_tree.lookup(value)
        assert returns_value.value == hash(value) % 10**8


@pytest.mark.parametrize("array",
                         [list(range(100)),
                          sample(list(range(500)), 100),
                         sample(list(range(500)), 100)]
                         )
def test_delete(array):
    """Test binary tree delete methods
        that delete value in the tree by
        checking lookup returns None

        :argument  array - randomly gen list"""
    # create BinaryTree
    delete_binary_tree = BinarySearchTree(1125)
    # add each new item on first position
    for item in array:
        delete_binary_tree.insert(item)

    # check lookup return proper value
    for value in array:
        delete_binary_tree.delete(value)
        assert delete_binary_tree.lookup(value) is None


@pytest.mark.parametrize("array",
                         [list(range(10))]
                         )
def test_raise_error(array):
    """Test binary tree delete methods
    Raises:
            ValueError: In case no such value in the tree
    """
    # create BinaryTree
    delete_binary_tree = BinarySearchTree(1125)
    # add each new item on first position
    for item in array:
        delete_binary_tree.insert(item)

    with pytest.raises(ValueError):
        delete_binary_tree.delete(12)
