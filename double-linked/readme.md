# Singly Linked List Implementation in Python

## Overview
This project involves the implementation of a singly linked list in Python, supporting basic operations such as insertion, deletion, and traversal.

## Objectives
1. **Task 1**: Implement the `Node` class to represent individual nodes in the linked list.
2. **Task 2**: Implement the `SinglyLinkedList` class with methods for insertion, deletion, and traversal.
3. **Task 3**: Test the implemented functionality by performing various operations on the linked list.

## Task 1: Node Class
The `Node` class represents individual nodes in the linked list. Each node contains data and a reference to the next node.

### Node Class Implementation
```python
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
