"""Task data structures
linked list, stack, queue, hash table, tree, graph"""

from typing import Any


class Node:
    """Node for linked list, queue and stack"""
    def __init__(self, value: Any) -> None:
        self.value = value
        # link to next node
        self.pointer = None

    def __repr__(self):
        return self.value

    def __get__(self, instance, owner):
        return self.value, self.pointer


class LinkedList:
    """linked list"""
    def __init__(self, value: Any) -> None:
        self.head = Node(value)
        self.tail = self.head
        self.length = 1

    def prepend(self, value: Any) -> None:
        """ add new element at first position"""
        # init new node
        new_node = Node(value)
        # link head to new node and assign pointer from new node to next one
        temp = self.head
        self.head = new_node
        new_node.pointer = temp
        self.length += 1

    def append(self, value: Any) -> None:
        """add new element at last position"""
        # init new node
        new_node = Node(value)

        # check if add first element - point head to next node
        if self.head == self.tail:
            self.head.pointer = new_node
        # assign pointer and tail link to next node
        self.tail.pointer = new_node
        self.tail = new_node
        self.length += 1

    def lookup(self, value: Any):
        """Find value in list
        In case value not in list no return
        """
        counter = 0
        # set start at the head
        current = self.head
        while current:
            # return index in case value in list
            if value == current.value:
                return counter
            # assign next node
            current = current.pointer
            counter += 1

    def insert(self, index: int, value: Any) -> None:
        """Insert value in linked list at specific index
        If index less than 0 or bigger than length of list - raise IndexError
        """
        # check index. it mast be more 0 and not more then length + 1
        # if not proper index raise IndexError
        if 0 > index > self.length:
            raise IndexError
        # init new node
        insert_value = Node(value)
        counter = 0
        # set start at the head
        current = self.head
        while current:

            # case insertion at first position. call prepend func and break loop
            if index == 0:
                self.prepend(value)
                break

            # case insertion at next to last position. call append func and break loop
            if index == self.length:
                self.append(value)
                break

            # insertion inside list and break loop
            if counter == index - 1:
                # link previous element to new element
                temp = current.pointer
                current.pointer = insert_value
                # link new element to next one
                insert_value.pointer = temp
                self.length += 1
                break
            # assign next node
            current = current.pointer
            counter += 1

    def delete(self, index: int) -> None:
        """Delete value from list by index
        If index less than 0 or bigger than length of list - raise IndexError
        if list is empty - raise IndexError
        """
        # check index. it mast be more 0 and not more then length + 1
        # if not proper index raise IndexError
        if index >= self.length or index < 0:
            raise IndexError("IndexError: list assignment index out of range")

        # IndexError: pop from empty list
        if self.length == 0:
            raise IndexError("IndexError: pop from empty list")

        counter = 0
        # assign 2 nodes: current = head and previous node
        previous = None
        current = self.head
        while current:

            # case first element delete. break loop after deleted
            if index == 0:
                # assign head to next node
                self.head = self.head.pointer
                self.length -= 1
                break

            # case inside element delete. break loop after deleted
            if index == counter:
                # assign previous element at element after deleted element
                previous.pointer = current.pointer

                # check if delete element is last in list
                # assign tail at previous element
                if current.pointer is None:
                    self.tail = previous
                self.length -= 1
                break
            # assign previous and current nodes to next nodes
            previous = current
            current = current.pointer
            counter += 1


class Stack:
    """Stack
    1 <- 2 <- 3. Tail it's the first node in list. It points to previous"""
    def __init__(self, value: Any) -> None:
        self.head = Node(value)
        self.length = 1

    def push(self, value: Any) -> None:
        """insert value in Stack at last position"""
        # init new node
        new_node = Node(value)
        # assign pointer of new node and tail to previous node
        temp = self.head
        self.head = new_node
        new_node.pointer = temp
        self.length += 1

    def pop(self) -> Any:
        """Return value of last node and delete that node from list
        Raise IndexError in case pop from empty list"""

        # IndexError: pop from empty list
        if self.length == 0:
            raise IndexError("IndexError: pop from empty list")

        # take value
        pop_value = self.head.value
        # assign tail on previous element
        self.head = self.head.pointer
        self.length -= 1
        return pop_value

    def peek(self) -> Any:
        """Return value of last element"""
        return self.head.value


class Queue:
    """Queue
    (tail)3 -> 2 -> 1(head). Tail it's the node at 0 index."""
    def __init__(self, value: Any) -> None:
        self.head = Node(value)
        self.tail = self.head
        self.length = 1

    def enqueue(self, value: Any) -> None:
        """Add element to queue at 0 position"""
        # init new node
        new_node = Node(value)

        # check if add first element - point head to next node
        if self.head == self.tail:
            self.head.pointer = new_node
        # link tail to new node and assign pointer from new node to next one
        self.tail.pointer = new_node
        self.tail = new_node
        self.length += 1

    def dequeue(self) -> Any:
        """Return value from last index and delete node
        Raise IndexError in case pop from empty list"""

        # IndexError: pop from empty list
        if self.length == 0:
            raise IndexError("IndexError: pop from empty list")

        dequeue_value = self.head.value
        # set head to previous node
        self.head = self.head.pointer
        self.length -= 1
        return dequeue_value

    def peek(self):
        """Return value of last index element"""
        return self.head.value


class TreeNode:
    """Node of binary tree"""
    def __init__(self, value: Any) -> None:
        self.value = hash(value) % 10**8
        self.left: TreeNode | None = None
        self.right: TreeNode | None = None

    def __repr__(self):
        return self.value


class BinarySearchTree:
    """Binary search tree"""
    def __init__(self, value: Any) -> None:
        self.root = TreeNode(value)
        # self.return_value = None

    def insert(self, value: Any) -> None:
        """Take value, set start node at root.
        Call recursive _insert func """
        # set node at root
        node = self.root
        # set inserting node
        new_node = TreeNode(value)
        if self._insert(new_node, node):
            print("Added", value)

    def _insert(self, new_node: TreeNode, node: TreeNode) -> TreeNode:
        """Insert value at proper place(smaller to left, bigger to right)"""
        # check if current node is empty ->  insert new node
        if node is None:
            node = new_node
            return node

        # if value less than root node -> move to left side
        if new_node.value < node.value:
            # call recursion function. move to next left root
            node.left = self._insert(new_node, node.left)

        # if value more or equal than root node -> move to right side
        else:
            # call recursion function. move to next right root
            node.right = self._insert(new_node, node.right)
        return node

    def lookup(self, value: Any):
        """Take value, set start node at root.
        Call recursive _lookup func
        Return link of looking node"""
        # set node at root
        node = self.root
        # hash value
        hash_value = hash(value) % 10 ** 8
        return self._lookup(hash_value, node)

    def _lookup(self, hash_value: int, node: TreeNode):
        """Looking hash value in tree
        If no value in the tree return None"""

        # case - value not found in tree. return None
        if node is None:
            return None

        # if value less than root node -> move to left side
        if hash_value < node.value:
            # call recursion function. move to next left root
            return_value = self._lookup(hash_value, node.left)

        # if value more than root node -> move to right side
        elif hash_value > node.value:
            # call recursion function. move to next right root
            return_value = self._lookup(hash_value, node.right)

        # if node found, return link at node to prev recursion
        else:
            return node
        # return found node or None
        return return_value

    @staticmethod
    def find_min_value_node(node: TreeNode) -> TreeNode:
        """Return minimum value"""
        while node.left is not None:
            node = node.left
        return node

    def delete(self, value: Any) -> None:
        """Delete value from binary tree
        In case empty tree raise IndexError
        In case no such value in tree raise ValueError"""
        # check case tree is empty
        if self.root is None:
            raise IndexError("IndexError: delete from empty binary_tree")
        # init root node
        node = self.root
        hash_value = hash(value) % 10 ** 8
        # call recursion function.
        self._delete(hash_value, node)

    def _delete(self, hash_value, node):
        """Looking value in tree and delete it,
        set smallest value from rite side instead deleted node
        In case no such value in tree raise ValueError"""
        # if value not found in tree
        if node is None:
            raise ValueError("ValueError: binary_tree.delete(x): x not in tree")

        # if value less than root node -> move to left side
        if hash_value < node.value:
            # call recursion function. move to next left root
            node.left = self._delete(hash_value, node.left)

        # if value more than root node -> move to right side
        elif hash_value > node.value:
            # call recursion function. move to next right root
            node.right = self._delete(hash_value, node.right)

        # if node was found
        else:
            # is left side is empty - just set right-side node instead current
            if node.left is None:
                node = node.right
                return node
            # is right side is empty - just set left-side node instead current
            if node.right is None:
                node = node.left
                return node

            # if deleting node has booth child
            # call function to find minimum value from right side
            temp = self.find_min_value_node(node.right)
            node.value = temp.value
            # delete minimum value(was found in find_min_value_node func)
            node.right = self._delete(temp.value, node.right)
        return node


class HashTableNode:
    """Hash table node"""
    def __init__(self, key: Any, value: Any) -> None:
        self.index = hash(key) % 10**8
        self.key = key
        self.value = value
        self.pointer: HashTableNode | None = None
        self.collision: HashTableNode | None = None

    def __repr__(self):
        return self.key, self.value


class HashTable:
    """Hash table"""
    def __init__(self, key: Any, value: Any) -> None:
        self.head = HashTableNode(key, value)

    def _prepend(self, new_node: HashTableNode) -> None:
        """Add (key, value) in hash table on firs position
        if no collision with current index"""
        # link head to new node and assign pointer from new node to next one
        temp = self.head
        self.head = new_node
        new_node.pointer = temp

    def insert(self, key: Any, value: Any) -> None:
        """Check for collision
        yes - call _insert_collision func and add node at existing index
        no - call _prepend func and add node at first position"""
        new_node = HashTableNode(key, value)
        node = self.head
        # checking all table for collision
        while node:
            if new_node.index == node.index:
                return self._insert_collision(new_node, node)
            node = node.pointer
        # else add node at firs position
        self._prepend(new_node)

    @staticmethod
    def _insert_collision(new_node: HashTableNode, node: HashTableNode) -> None:
        """Insert collision key, value in local linked list
        If inserting key already in the table - raise KeyError"""
        while True:
            # check if key already in the table - raise KeyError
            if new_node.key is node.key:  # new_node.key == node.key:
                raise KeyError("KeyError: hash_table.insert(key, value):key already in table")
            # add collision node at last position
            if node.collision is None:
                node.collision = new_node
                break
            # check next collision node
            node = node.collision

    def lookup(self, key: Any):
        """Looking for current key in hash table.
        Return value or None"""
        index = hash(key) % 10**8
        # init start node
        node = self.head
        # looking indexes
        while node:
            if index == node.index:
                # if node has no collision return value
                if not node.collision:
                    return node.value
                # else call _lookup_collision
                return self._lookup_collision(key, node)
            # assign next node
            node = node.pointer
        # if no current key - return None
        return None

    @staticmethod
    def _lookup_collision(key: Any, node: HashTableNode) -> None:
        """checking all collisions for current key"""
        while node:
            if key is node.key:
                return node.value
            # assign next node
            node = node.collision

    def delete(self, key: Any) -> True:
        """Call delete head with no collision
        call delete head with collision
        go through all table and find deleting key
        If no key raise KeyError
        """
        index = hash(key) % 10 ** 8
        # init previous and current node
        previous_node = None
        current_node = self.head

        # call delete head with no collision
        if self._delete_head_no_collision(index):
            return True
        # call delete head with collision
        if self._delete_head_collision(index, key, current_node):
            return True

        while current_node:
            # delete node with collision
            if index == current_node.index and current_node.collision:
                # call func
                current_node = self._delete_collision(key, current_node)
                # assign previous previous pointer to new node
                previous_node.pointer = current_node
                return True
            # delete node without collision
            if index == current_node.index:
                # call func
                previous_node.pointer = current_node.pointer
                return True
            # assign previous and current nodes to next nodes
            previous_node = current_node
            current_node = current_node.pointer
        # raise ValueError if no key in table
        raise KeyError("KeyError: hash_table.delete(x): x not in the hash table")

    def _delete_head_no_collision(self, index: int) -> bool:
        """Check if table is empty - raise IndexError
        Check if deleting key it's the head, and head has no collision
        Delete head with no collision - return True
        else - False
        """
        # if empty table raise IndexError
        if self.head is None:
            raise IndexError("IndexError: delete from empty hash_table")
        # if head node has no collision
        # point head to next node
        if index == self.head.index and not self.head.collision:
            self.head = self.head.pointer
            return True
        return False

    def _delete_head_collision(self, index: int, key: Any, current_node: HashTableNode) -> bool:
        """Check if deleting key it's the head, and head has collision
        Delete head with collision - return True
        else - False"""
        # if head has collision
        if index == self.head.index:
            # call _delete_collision and point head to new current node
            current_node = self._delete_collision(key, current_node)
            self.head = current_node
            return True
        return False

    @staticmethod
    def _delete_collision(key: Any, node: HashTableNode) -> HashTableNode:
        """Delete node with collision"""
        # if the first collision node must delete
        # it can has pointer to next not collision node
        if key is node.key:
            # save pointer to next node
            temp = node.pointer
            # assign node to next collision node
            node = node.collision
            # assign pointer to next node
            node.pointer = temp
            return node
        # check all other collision nodes
        # they are has pointer == None
        while node.collision:
            # assign next node
            next_node = node.collision
            # if its deleting key assign collision pointer to next node
            if key == next_node.key:
                node.collision = next_node.collision
                return node
            node = node.collision

    def list(self):
        """just for check"""
        node = self.head
        while node:
            print(node.index, node.value, node.pointer)
            if node.collision:
                collision = node.collision
                while collision:
                    print("coll", collision.key, collision.value)
                    collision = collision.collision
            node = node.pointer


class GraphNode:
    """graph node"""
    def __init__(self, node_name: str) -> None:
        self.node_name = node_name
        self.pointer: GraphNode | None = None
        self.pointer_to_edge: GraphEdge | None = None

    def __repr__(self):
        return self.node_name


class GraphEdge:
    """Graph edge"""
    def __init__(self, node_name=None, pointer_to_node=None):
        self.node_name: str | None = node_name
        self.pointer_to_node: GraphNode | None = pointer_to_node
        self.pointer_to_edge: GraphEdge | None = None

    def __repr__(self):
        return self.node_name


class Graph:
    """Simple Graph base on linked list"""
    def __init__(self, node_name):
        self.first_node = GraphNode(node_name)

    def insert(self, node_name: str, edges: tuple) -> None:
        """Add graph.

        You can add edges only to existing node
        Input edges name like name of existing node: 'a', 'b', 'new_node'"""

        # init new graph node, set it name
        new_node = GraphNode(node_name)
        # set link to previous node(its not edge)
        new_node.pointer = self.first_node
        # set enter in graph at last node
        self.first_node = new_node

        # iterate trough edges
        for edge in edges:
            # iterate trough our "linked list"
            next_node = new_node.pointer
            while next_node:
                # if we find node, edge point to
                if edge == next_node.node_name:
                    # init new edge(set name of node, and pointer to node)
                    new_edge = GraphEdge(edge, next_node)
                    # save new edge 'edge' pointer
                    temp = new_node.pointer_to_edge
                    # assign 'edge' pointer to new edge
                    new_node.pointer_to_edge = new_edge
                    # new edge pointer to next edge
                    new_edge.pointer_to_edge = temp
                    break
                # assign next node
                next_node = next_node.pointer

    def lookup(self, name: str) -> GraphNode:
        """Find node with current name
        Return link to node"""
        node = self.first_node
        while node:
            if name == node.node_name:
                return node
            node = node.pointer

    def delete(self, link: GraphNode) -> None:
        """Delete node and edges
        Raise index error if Graph is empty"""
        node = self.first_node
        if not node:
            raise IndexError("IndexError: delete from empty graph")
        self._delete_node(link, node)
        self._delete_edge(link, node)

    def _delete_node(self, link, node) -> None:
        """Delete node by link
        If there is no node with current link
        raise ValueError"""
        # init previous node
        previous_node = None
        # iterate through list
        while node:
            if link == node:
                # if deleting node is not first
                # assign previous.pointer to next node after deleting
                if previous_node:
                    previous_node.pointer = node.pointer
                # if deleting node is first
                # assign first_node to next node
                else:
                    self.first_node = node.pointer
                break
            # assign previous and current nodes to next nodes
            previous_node = node
            node = node.pointer
        else:
            raise ValueError("ValueError: graph.delete(x): x not in tree")

    @staticmethod
    def _delete_edge(link: GraphNode, node: GraphNode) -> None:
        # iterate through all nodes
        while node:
            previous_edge = node
            edge = node.pointer_to_edge
            # iterate through edges
            while edge:
                if link is edge.pointer_to_node:
                    previous_edge.pointer_to_edge = edge.pointer_to_edge
                    break
                # assign edges to next edges
                previous_edge = edge
                edge = edge.pointer_to_edge
            # assign next node
            node = node.pointer

    def list(self):
        """just for check"""
        node = self.first_node
        while node:
            print(f"Node: name {node.node_name}, edge {node.pointer_to_edge}")
            if node.pointer_to_edge:
                edge = node.pointer_to_edge
                while edge:
                    print(f"\tEdge: {edge.node_name} node: {edge.pointer_to_node}, "
                          f"edge: {edge.pointer_to_edge}")
                    edge = edge.pointer_to_edge
            node = node.pointer


if __name__ == "__main__":

    # LINKED LIST
    linked_list = LinkedList(25)
    #
    # linked_list.prepend("r")
    # linked_list.prepend(-2.25)
    # linked_list.append(17)

    # print(linked_list.tail.value, linked_list.tail.value)
    #
    # print(linked_list.lookup(76))
    # print(linked_list.lookup(17))
    #
    # print("length", linked_list.length)
    # linked_list.insert("m", 0)
    # print(linked_list.lookup("m"))
    # print("length", linked_list.length)

    # print("len", linked_list.length)
    # linked_list.delete(1)
    # print(linked_list.lookup(17))
    # print(linked_list.tail.value)
    # linked_list.delete(0)
    # print(linked_list.lookup("m"), linked_list.lookup(-2.25))

    # # QUEUE
    # queue = Queue(10)
    # queue.enqueue(11)
    # queue.enqueue(12)
    # print(queue.peek())
    # while True:
    #     print(queue.dequeue())

    # # BINARY TREE
    # binary_search_tree = BinarySearchTree(50)
    # binary_search_tree.insert(25)
    # binary_search_tree.insert(75)
    # binary_search_tree.insert(30)
    # binary_search_tree.insert(200)
    # binary_search_tree.insert(False)
    #
    # left = binary_search_tree.root.left
    # right = binary_search_tree.root.right
    # print(binary_search_tree.root.value, left.value, right.value)
    #
    # print(binary_search_tree.lookup(25))
    #
    # binary_search_tree.delete(25)
    # print(binary_search_tree.lookup(2000))
    # left = binary_search_tree.root.left
    # right = binary_search_tree.root.right
    # print(binary_search_tree.root.value, left.value, right.value)

    # # HASH TABLE
    # hash_table = HashTable(7, "f")
    # hash_table.insert(1, "1")
    # hash_table.insert(9, "9")
    # hash_table.insert(6, "6")
    # hash_table.insert(0, "0")
    # hash_table.insert(True, "True")
    # hash_table.insert(False, "False")
    # hash_table.insert(55, "55")
    #
    # print(hash_table.lookup(True))
    #
    # # hash_table.delete(True)
    # for i in (7, 1, 55, True, ):
    #     hash_table.delete(i)
    # hash_table.li()
    # print(hash_table.lookup(True))
    # print(hash_table.head.key)

    # graph = Graph("a")
    # graph.insert("b", ("a",))
    # graph.insert("c", ("a", "b"))
    # graph.insert("d", ("b", "c"))
    # graph.insert("e", ("a", "b", "c"))
    # graph.insert("f", ("a", "e", "c", "d"))
    #
    # graph.list()
    #
    # print(graph.lookup("d"))
    # print(graph.lookup("a"))
    #
    # graph.delete(graph.lookup("f"))
    # graph.list()
