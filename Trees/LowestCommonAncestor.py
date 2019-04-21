"""
Lowest Common Ancestor in a Binary Search Tree.
Given values of two values n1 and n2 in a Binary Search Tree, find the Lowest Common Ancestor (LCA). You may assume that both the values exist in the tree.
BST_LCA

              50
           /      \
          30      70
         /  \    /  \
       20   40  60   80

LCA of 20 and 70 is 50
LCA of 40 and 30 is 30
"""


class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

def lowestCommonAncestor(root, key1, key2):

    if root is None:
        return None

    if key1 < root.key and key2 < root.key :
        return lowestCommonAncestor(root.left, key1, key2)

    if key1 > root.key and key2 > root.key :
        return lowestCommonAncestor(root.right, key1, key2)

    return root

if __name__ == '__main__':
    root = Node(20)
    root.left = Node(8)
    root.right = Node(22)
    root.left.left = Node(4)
    root.left.right = Node(12)
    root.left.right.left = Node(10)
    root.left.right.right = Node(14)

    n1 = 10
    n2 = 14
    t = lowestCommonAncestor(root, n1, n2)
    print("LCA of %d and %d is %d" % (n1, n2, t.key))

    n1 = 14;
    n2 = 8
    t = lowestCommonAncestor(root, n1, n2)
    print("LCA of %d and %d is %d" % (n1, n2, t.key))

    n1 = 10;
    n2 = 22
    t = lowestCommonAncestor(root, n1, n2)
    print("LCA of %d and %d is %d" % (n1, n2, t.key))
