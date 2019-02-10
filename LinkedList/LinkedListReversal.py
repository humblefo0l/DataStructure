"""
Linked List Reversal

Problem
Write a function to reverse a Linked List in place. The function will take in the head of
the list as input and return the new head of the list.


Solution
Since we want to do this in place we want to make the funciton operate in O(1) space,
meaning we don't want to create a new list, so we will simply use the current nodes!
Time wise, we can perform the reversal in O(n) time.

We can reverse the list by changing the next pointer of each node. Each node's next
pointer should point to the previous node.

In one pass from head to tail of our input list, we will point each node's next pointer
to the previous element.

Make sure to copy current.next_node into next_node before setting current.next_node
to previous. Let's see this solution coded out:

"""


class Node:

    def __init__(self, value):
        self.value = value
        self.nextnode = None


def reverse(node):
    current = node
    previous = None
    next = None

    while current:

        next = current.nextnode

        current.nextnode = previous

        previous = current

        current = next

    return previous


a = Node(1)
b = Node(2)
c = Node(3)
d = Node(4)

a.nextnode = b
b.nextnode = c
c.nextnode = d

print(a.value)
print(a.nextnode.value)
print(b.nextnode.value)
print(c.nextnode.value)
print("*****")
reverse(a)
print(d.value)
print(d.nextnode.value)
