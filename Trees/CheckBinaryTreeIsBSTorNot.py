"""
A program to check if a binary tree is BST or not
A binary search tree (BST) is a node based binary tree data structure which has
the following properties.
• The left subtree of a node contains only nodes with keys less than the node’s key.
• The right subtree of a node contains only nodes with keys greater than the node’s key.
• Both the left and right subtrees must also be binary search trees.

From the above properties it naturally follows that:
• Each node (item in the tree) has a distinct key.
"""

class Node:
    def __init__(self,key):
        self.key = key
        self.left = None
        self.right = None

def isBST(root):

    if root is None:
        return True

    if root.left or root.right:

        if root.key < root.left.key or root.key > root.right.key:
            return False

        return isBST(root.left) and isBST(root.right)
    else:
        return True



if __name__ == '__main__':
    if __name__ == '__main__':
        root = Node(3)
        root.left = Node(2)
        root.right = Node(5)
        root.right.left = Node(1)
        root.right.right = Node(4)
        # root.right.left.left = Node(40) 
        if (isBST(root)):
            print("Is BST")
        else:
            print("Not a BST")

        print()

        root = Node(4)
        root.left = Node(2)
        root.right = Node(5)
        root.left.left = Node(1)
        root.left.right = Node(3)

        if (isBST(root)):
            print("Is BST")
        else:
            print("Not a BST")
