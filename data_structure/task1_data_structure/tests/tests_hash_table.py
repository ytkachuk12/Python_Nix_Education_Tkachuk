"""Tests for task data structures:
linked list, stack, queue, hash table, tree, graph"""

from random import randint, sample
import pytest

from task1_data_structures import HashTable


@pytest.mark.parametrize("array",
                         [dict(zip(list(range(100)), [randint(-50, 50) for _ in range(100)])),
                          dict(zip(list(range(100)), [randint(-500, 500) for _ in range(100)])),
                          {5: "5", 1: "1", 0: "0", 4: "4", True: "True", False: "False"}]
                         )
def test_insert_lookup(array):
    """Test hash table insert methods
    that insert value in the tree by
    checking lookup methods returns proper value

    Test collision keys(1 and True, 0 anf False)

    :argument  array - randomly gen list"""
    # create HashTable
    insert_hash_table = HashTable(1125, "a")
    # add each new item on first position
    for key in array:
        insert_hash_table.insert(key, array[key])

    # check lookup return proper value
    for key in array:
        assert insert_hash_table.lookup(key) == array[key]


@pytest.mark.parametrize("array",
                         [dict(zip(list(range(100)), [randint(-50, 100) for _ in range(100)])),
                          dict(zip(list(range(100)), [randint(-500, 500) for _ in range(100)])),
                          {5: "5", 1: "1", 0: "0", 4: "4", True: "True", False: "False"}]
                         )
def test_delete(array):
    """Test hash table delete methods
        that delete value in the hash table by
        checking lookup returns None

        :argument  array - randomly gen list"""
    # create HashTable
    delete_hash_table = HashTable(1125, "a")
    # add each new item on first position
    for key in array:
        delete_hash_table.insert(key, array[key])

    # check lookup return proper value
    for key in array:
        delete_hash_table.delete(key)
        assert delete_hash_table.lookup(key) is None


@pytest.mark.parametrize("array",
                         [{5: "5", 1: "1", 0: "0", 4: "4", True: "True", False: "False"}]
                         )
def test_raise_error(array):
    """Test hash table delete method
    Raises:
            KeyError: In case no such key in the hash table
    """
    # create BinaryTree
    delete_hash_table = HashTable(1125, "1125")
    # add each new item on first position
    for key in array:
        delete_hash_table.insert(key, array[key])

    with pytest.raises(KeyError):
        delete_hash_table.delete(112)

