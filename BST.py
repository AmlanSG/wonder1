# Data structure to store a Binary Search Tree node
class Node:
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right


# Recursive function to insert a key into BST
def insert(root, key):
    # if the root is None, create a node and return it
    if root is None:
        return Node(key)

    # if given key is less than the root node, recur for left subtree
    if key < root.data:
        root.left = insert(root.left, key)

    # if given key is more than the root node, recur for right subtree
    else:
        root.right = insert(root.right, key)

    return root


# Function to determine if given Binary Tree is a BST or not by keeping a
# valid range (starting from [-INFINITY, INFINITY]) and keep shrinking
# it down for each node as we go down recursively
def isBST(node, minKey, maxKey):
    # base case
    if node is None:
        return True

    # if node's value fall outside valid range
    if node.data < minKey or node.data > maxKey:
        return False

    # recursively check left and right subtrees with updated range
    return isBST(node.left, minKey, node.data) and \
           isBST(node.right, node.data, maxKey)


# Function to determine if given Binary Tree is a BST or not
def checkForBST(root):
    if isBST(root, float('-inf'), float('inf')):
        print("This is a BST.")
    else:
        print("This is NOT a BST")


def swap(root):
    left = root.left
    root.left = root.right
    root.right = left


if __name__ == '__main__':

    root = None
    keys = [15, 10, 20, 8, 12, 16, 25]

    for key in keys:
        root = insert(root, key)

    # swap left and right nodes
    swap(root)
    checkForBST(root)
