# A class to store a BST node
class Node:
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right
 
 
# Function to perform inorder traversal on the BST
def inorder(root):
 
    if root is None:
        return
 
    inorder(root.left)
    print(root.data, end=' ')
    inorder(root.right)
 
 
# Function to find the maximum value node in the subtree rooted at `ptr`
def maximumKey(ptr):
 
    while ptr.right:
        ptr = ptr.right
    
    return ptr
 
 
# Recursive function to insert a key into a BST
def insert(root, key):
 
    # if the root is None, create a new node and return it
    if root is None:
        print("{} has been added as a new node of the tree".format(key))
        return Node(key)
 
    # if the given key is less than the root node, recur for the left subtree
    if key < root.data:
        print("{} has been inserted to the left subtree.".format(key))
        root.left = insert(root.left, key)
 
    # if the given key is more than the root node, recur for the right subtree
    else:
        print("{} has been inserted to the right subtree.".format(key))
        root.right = insert(root.right, key)
 
    return root
 
 
# Function to delete a node from a BST
def deleteNode(root, key):
 
    # base case: the key is not found in the tree
    if root is None:
        print("[!]Element not found on Tree.")
        return root

    # if the given key is less than the root node, recur for the left subtree
    if key < root.data:
        print("[-] Deleting Node from left.")
        print("[-] {} element deleted.".format(key))
        root.left = deleteNode(root.left, key)
        

    # if the given key is more than the root node, recur for the right subtree
    elif key > root.data:
        print("[-] Deleting Node from right.")
        print("[-] {} element deleted.".format(key))
        root.right = deleteNode(root.right, key)
 
    # key found
    else:
 
        # Case 1: node to be deleted has no children (it is a leaf node)
        if root.left is None and root.right is None:
            # update root to None
            print("[#]Node has no children.")
            return None
 
        # Case 2: node to be deleted has two children
        elif root.left and root.right:
            print("[#]Node has children on both sides.")
            # find its inorder predecessor node
            predecessor = maximumKey(root.left)
 
            # copy value of the predecessor to the current node
            root.data = predecessor.data
 
            # recursively delete the predecessor. Note that the
            # predecessor will have at most one child (left child)
            root.left = deleteNode(root.left, predecessor.data)
            print("[-] Deleting Node.")
        # Case 3: node to be deleted has only one child
        else:
            print("[#]Node has children.")
            # choose a child node
            child = root.left if root.left else root.right
            root = child
 
    return root
 
 
if __name__ == '__main__':
 
    keys = [15, 10, 20, 8, 12, 25]
 
    root = None
    
    for key in keys:
        root = insert(root, key)
 
    root = deleteNode(root, 12)
    inorder(root)