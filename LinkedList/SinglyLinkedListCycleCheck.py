"""
Singly Linked List Cycle Check

Problem

Given a singly linked list, write a function which takes in the first node in a singly
linked list and returns a boolean indicating if the linked list contains a "cycle".

A cycle is when a node's next point actually points back to a previous node in the list.
This is also sometimes known as a circularly linked list.



Solution

To solve this problem we will have two markers traversing through the list. marker1 and
marker2. We will have both makers begin at the first node of the list and traverse through
the linked list. However the second marker, marker2, will move two nodes ahead for every
one node that marker1 moves.

By this logic we can imagine that the markers are "racing" through the linked list, with
marker2 moving faster. If the linked list has a cylce and is circularly connected we will
have the analogy of a track, in this case the marker2 will eventually be "lapping" the
marker1 and they will equal each other.

If the linked list has no cycle, then marker2 should be able to continue on until the
very end, never equaling the first marker.

"""

import pytest


class Node(object):

    def __init__(self, value):
        self.value = value
        self.nextnode = None



def cycle_check(node):
    fast = node
    slow = node

    while fast != None and fast.nextnode !=None and fast.nextnode.nextnode != None:

        fast = fast.nextnode.nextnode
        slow = slow.nextnode

        if fast == slow:
            return True

    return False



"""
RUN THIS CELL TO TEST YOUR SOLUTION
"""

# CREATE CYCLE LIST
a = Node(1)
b = Node(2)
c = Node(3)

a.nextnode = b
b.nextnode = c
c.nextnode = a  # Cycle Here!

# CREATE NON CYCLE LIST
x = Node(1)
y = Node(2)
z = Node(3)

x.nextnode = y
y.nextnode = z


#############


class TestCycleCheck(object):

    def test(self):
        assert cycle_check(a) == True
        assert cycle_check(x) == False

        print("ALL TEST CASES PASSED")
