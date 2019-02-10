"""
Singly Linked List Implementation
In this lecture we will implement a basic Singly Linked List.

Remember, in a singly linked list, we have an ordered list of items as individual
Nodes that have pointers to other Nodes.
"""

class Node:

    def __init__(self, value):
        self.value = value
        self.nextnode = None


a = Node(1)
b = Node(2)
c = Node(3)
d = Node(4)
a.nextnode = b
b.nextnode = c
c.nextnode = d

x = a
while(True):
    print(x.value)
    if x.nextnode == None:
        x = x.nextnode
        break
    x = x.nextnode


