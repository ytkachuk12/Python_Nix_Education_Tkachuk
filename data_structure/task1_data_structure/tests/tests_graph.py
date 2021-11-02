"""Tests for task data structures:
linked list, stack, queue, hash table, tree, graph"""

from random import randint, sample
import pytest

from task1_data_structures import Graph


@pytest.mark.parametrize("array",
                         [list(range(50))]
                         )
def test_insert_lookup(array):
    """Test graph insert methods
        that insert new node with edges in the graph
        checking lookup methods returns proper name

        :argument  array - randomly gen list"""
    # create graph
    insert_graph = Graph("a")
    # add each new item on first position
    for item in array:
        insert_graph.insert(item, array[:item])

    # check lookup return proper name
    for name in array:
        returns_value = insert_graph.lookup(name)
        assert returns_value.node_name == name


@pytest.mark.parametrize("array",
                         [list(range(50))]
                         )
def test_delete(array):
    """Test graph delete method
        that delete node with edges by link from the graph
        checking lookup methods returns None

        :argument  array - randomly gen list"""
    # create graph
    delete_graph = Graph("a")
    # add each new item on first position
    for item in array:
        delete_graph.insert(item, array[:item])

    # check lookup return proper name
    for name in array:
        delete_graph.delete(delete_graph.lookup(name))
        assert delete_graph.lookup(name) is None


@pytest.mark.parametrize("array",
                         [list(range(50))]
                         )
def test_raise_error(array):
    """Test graph delete method
    Raises:
            ValueError: In case no such node in the graph
        """
    # create graph
    delete_graph = Graph("a")
    # add each new item on first position
    for item in array:
        delete_graph.insert(item, array[:item])

    with pytest.raises(ValueError):
        delete_graph.delete(12)