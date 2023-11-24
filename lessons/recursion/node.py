"""Node Class."""

from __future__ import annotations


class Node:
    """My Node class for linked lists."""
    
    data: int
    next: Node | None
    
    def __init__(self, data: int, next: Node | None):
        """Construct Node."""
        self.data = data
        self.next = next
        
    def __str__(self) -> str:
        """Produce a string visualization of the linked list."""
        if self.next is None:
            # base case (where it ends!)
            return f"{self.data} -> None"
        else:
            return f"{self.data} -> {self.next}"
        
    def head(self) -> int:
        """Return the data attribute for the first element in the linked list."""
        return self.data
    
    def tail(self) -> Node | None:
        """Return a linked list of every element minus the head."""
        if self.next is None:
            return None
        
        new_node: Node = Node(0, None)
        new_node.data = self.next.data
        new_node.next = self.next.next
        
        return new_node

    def last(self) -> int:
        """Return the data attribute of the last element in the linked list."""
        new__node1: Node = self

        while new__node1.next is not None:
            new__node1 = new__node1.next

        return new__node1.data