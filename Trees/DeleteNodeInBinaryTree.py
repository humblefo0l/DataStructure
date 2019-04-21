"""
Binary Search Tree | Set 2 (Delete)
We have discussed BST search and insert operations. In this post, delete operation
is discussed. When we delete a node, three possibilities arise.
1) Node to be deleted is leaf: Simply remove from the tree.

              50                            50
           /     \         delete(20)      /   \
          30      70       --------->    30     70
         /  \    /  \                     \    /  \
       20   40  60   80                   40  60   80
2) Node to be deleted has only one child: Copy the child to the node and delete the
child

              50                            50
           /     \         delete(30)      /   \
          30      70       --------->    40     70
            \    /  \                          /  \
            40  60   80                       60   80
3) Node to be deleted has two children: Find inorder successor of the node. Copy contents
of the inorder successor to the node and delete the inorder successor. Note that inorder predecessor can also be used.

              50                            60
           /     \         delete(50)      /   \
          40      70       --------->    40    70
                 /  \                            \
                60   80                           80
The important thing to note is, inorder successor is needed only when right child is
not empty. In this part icular case, inorder successor can be obtained by finding the
minimum value in right child of the node.

Time Complexity:
The worst case time complexity of delete operation is O(h) where h is height of
Binary Search Tree. In worst case, we may have to travel from root to the deepest
leaf node. The height of a skewed tree may become n and the time complexity of
delete operation may become O(n)

"""


class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None


def insert(node, key):

    if node is None:
        return Node(key)

    if key < node.key:
        node.left = insert(node.left, key)
    else:
        node.right = insert(node.right, key)


    return node


def inorder(root):

    if root is not None:
        inorder(root.left)
        print(root.key, end=" ")
        inorder(root.right)

def minValueNode(node):

    while node.left is not None:
        node = node.left

    return node


def deleteNode(root, key):

    if root is None:
        return root


    if key < root.key:
        root.left = deleteNode( root.left, key)

    elif key > root.key:
        root.right = deleteNode(root.right, key)

    else:

        if root.left is None:
            temp = root.right
            root = None
            return temp

        elif root.right is None:
            temp = root.left
            root = None
            return temp

        temp = minValueNode(root.right)

        root.key = temp.key

        root.right = deleteNode(root.right, temp.key)

    return root

root = None
root = insert(root, 50)
root = insert(root, 30)
root = insert(root, 20)
root = insert(root, 40)
root = insert(root, 70)
root = insert(root, 60)
root = insert(root, 80)

print("Inorder traversal of the given tree")
inorder(root)

print("\nDelete 20")
root = deleteNode(root, 20)
inorder(root)

print("\nDelete 50")
root = deleteNode(root, 50)
inorder(root)
