"""
Doubly Linked List Implementation
In this lecture we will implement a Doubly Linked List
"""

class DoublyLinkedList:

    def __init__(self, value):
        self.value = value
        self.prev = None
        self.next = None


a = DoublyLinkedList(1)
b = DoublyLinkedList(2)
c = DoublyLinkedList(3)

a.next = b
b.prev = a

b.next = c
c.prev = b


