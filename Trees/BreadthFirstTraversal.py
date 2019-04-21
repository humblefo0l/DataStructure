"""
Level Order Tree Traversal
Level order traversal of a tree is breadth first traversal for the tree.

Level order traversal of the above tree is 1 2 3 4 5

METHOD 2 (Use Queue)

Algorithm:
For each node, first the node is visited and then it’s child nodes are put in a
FIFO queue.

printLevelorder(tree)
1) Create an empty queue q
2) temp_node = root /*start from root*/
3) Loop while temp_node is not NULL
    a) print temp_node->data.
    b) Enqueue temp_node’s children (first left then right children) to q
    c) Dequeue a node from q and assign it’s value to temp_node
Implementation:
Here is a simple implementation of the above algorithm. Queue is implemented using an array with maximum size of 500. We can implement queue as linked list also.

"""


class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right= None

def printLevelOrder(root):

    if root is None:
        return 0

    queue = []

    queue.append(root)

    while queue:
        node = queue[0]
        queue.pop(0)

        print(node.key, end=" ")

        if node.left:
            queue.append(node.left)

        if node.right:
            queue.append(node.right)


if __name__ == '__main__':
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)


    # "Level order traversal of binary tree is -"
    printLevelOrder(root)
