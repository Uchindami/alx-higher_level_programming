#!/usr/bin/python3
"""Create a NODE and LSS class"""


class Node:
    """show a node in an SLL."""

    def __init__(self, data, next_node=None):
        """
        create a new Node.
        Args:
            data (int): data  for our new Node.
            next_node (Node): Some sort of Pointer to the next Node.
        """
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        """Getter for Node data."""
        return self.__data

    @data.setter
    def data(self, value):
        """Setter for Node data."""
        if not isinstance(value, int):
            raise TypeError("data must be an integer")
        self.__data = value

    @property
    def next_node(self):
        """Getter for next_node."""
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        """Setter for next_node."""
        if value is not None and not isinstance(value, Node):
            raise TypeError("next_node must be a Node object")
        self.__next_node = value


class SinglyLinkedList:
    def __init__(self):
        """Creates a new SLL."""
        self.head = None

    def sorted_insert(self, value):
        """
        Places a new Node into the SLL.
        Args:
            value (int): new data to place.
        """
        new_node = Node(value)
        if not self.head or self.head.data > value:
            new_node.next_node = self.head
            self.head = new_node
        else:
            current = self.head
            while current.next_node and current.next_node.data < value:
                current = current.next_node
            new_node.next_node = current.next_node
            current.next_node = new_node

    def __str__(self):
        """Define representation of an SLL."""
        values = []
        current = self.head
        while current:
            values.append(str(current.data))
            current = current.next_node
        return '\n'.join(values)
