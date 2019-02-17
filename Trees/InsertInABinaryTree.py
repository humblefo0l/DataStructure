"""
Tree represents the nodes connected by edges. It is a non-linear data structure. It
has the following properties.

One node is marked as Root node.
Every node other than the root is associated with one parent node.
Each node can have an arbiatry number of chid node.
We create a tree data structure in python by using the concept os node discussed earlier.
We designate one node as root node and then add more nodes as child nodes.

Inserting into a Tree

The insert class compares the value of the node to the parent node and decides to add
it as a left node or a right node. Finally the PrintTree class is used to print the
tree.
"""

class Node:
    def __init__(self, data):
        self.data = data
        self.right = None
        self.left = None

    def insert(self, data):
        if self.data:
            if data < self.data:
                if self.left == None:
                    self.left = Node(data)
                else:
                    self.left.insert(data)
            else:
                if self.right == None:
                    self.right = Node(data)
                else:
                    self.right.insert(data)
        else:
            self.data =data


    def PrintTree(self):
        if self.left:
            self.left.PrintTree()
        print(self.data)
        if self.right:
            self.right.PrintTree()



b = Node(12)
b.insert(6)
b.insert(1)
b.insert(3)
b.insert(31)


b.PrintTree()
