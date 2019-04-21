class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

def inorder(node):
    if node:
        inorder(node.left)
        print(node.key, end=" ")
        inorder(node.right)

def insert(node, key):
    if node is None:
        return Node(key)

    if key < node.key:
        node.left = insert(node.left, key)
    else:
        node.right = insert(node.right, key)

    return node

def bstCheck(node):

    if node is None:
        return True

    if node.right is None:
        if node.key < node.left.key:
            return False


    elif node.left is None:
        if node.key > node.right.key:
            return False

    else:
        c1 = bstCheck(node.left)
        c2 = bstCheck(node.right)

        if c1 is False or c2 is False:
            return False

    return True

root = Node(5)
insert(root, 10)
insert(root, 40)
insert(root, 1)
insert(root, 2)
insert(root, 23)

inorder(root)
print()
print(bstCheck(root))

