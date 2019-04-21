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
    root = Node(50)
    root.left = Node(30)
    root.right = Node(70)
    root.left.left = Node(20)
    root.left.right = Node(40)
    root.right.left = Node(60)
    root.right.right = Node(80)
    key1 = 20
    key2 = 70
    lca = lowestCommonAncestor(root, key1, key2)
    print(lca.key)

    key1 = 20
    key2 = 40
    lca = lowestCommonAncestor(root, key1, key2)
    print(lca.key)

