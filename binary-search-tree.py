class BinarySearchTreeNode:
    def __init__(self, data):
        self.left_child = None
        self.right_child = None
        self.data = data
        
    def __repr__(self):
        return f"Node containing data: {self.data}"
        
class BinarySearchTree:
    def __init__(self):
        self.root = None
        
    def insert(self, data, node=None):
        # on first loop of the recursive insert, set the starting node
        # to be the root of the tree
        if node is None:
            node = self.root
        # if there is no root (tree is empty), generate a new node with 
        # incoming data and set it as the root
        if self.root is None:
            self.root = BinarySearchTreeNode(data)
            return self.root
        elif node is None:
            node = BinarySearchTreeNode(data)
            return node
        # if there is a root (tree has nodes) check against values and
        # recursively decide whether new data is stored in left or right subtrees
        if data < node.data:
            if node.left_child is None:
                node.left_child = BinarySearchTreeNode(data)
                return node.left_child
            else:
                return self.insert(data, node.left_child)
        else:
            if node.right_child is None:
                node.right_child = BinarySearchTreeNode(data)
                return node.right_child
            else:
                return self.insert(data, node.right_child)
        
    def search(self, target, node=None):
        # In order to properly search without directly invoking the method with
        # the root as a parameter, the method must be broken down into a public
        # and private recursive method
        if node is None:
            node = self.root
        # if the target is in the root, return the root
        if node.data == target:
            return node
        else:
            # if target is not in the root, find the target recursively
            print(f"node is {node.data}")
            return self._search(target, node)
    
    def _search(self, target, node):
        # private method will execute recursively until target is found
        # or there are no more nodes on the correct path
        if node is None or node.data == target:
            return node
        # if target is smaller than current node's data, go left down the subtree
        # otherwise go right
        if target < node.data:
            return self._search(target, node.left_child)
        else:
            return self._search(target, node.right_child)
            
    def minimum(self, node=None):
        # initialize with the root node if no node is provided
        if node is None:
            node = self.root
        print(f"root is {node.data}")
        # iterate down the left side of the tree until reaching the terminal leaf
        # which will be the node with the minimum value
        while node.left_child is not None:
            print(f"next node on the left is {node.left_child.data}")
            node = node.left_child
        return node
    
    def maximum(self, node=None):
        # initialize with the root node if no node is provided
        if node is None:
            node = self.root
        print(f"root is {node.data}")
        # iterate down the right side of the tree until reaching the terminal leaf
        # which will be the node with the maximum value
        while node.right_child is not None:
            print(f"next node on the right is {node.right_child.data}")
            node = node.right_child
        return node
           
    def delete(self, target, node=None):
        # initialize with the root node
        if node is None:
            node = self.root
        
        if node is None:
            # if the tree is empty then there is nothing to delete
            return None
        
        if target < node.data:
            # If target is less than the current node's data then 
            # the data we want to delete is in the left subtree
            node.left_child = self.delete(target, node.left_child)
        elif target > node.data:
            # If target is greater than the current node's data then 
            # the data we want to delete is in the right subtree
            node.right_child = self.delete(target, node.right_child)
        else:
            # Otherwise, the current node contains the data we want to delete
            # Case 1: the current node is a leaf and has no children
            if node.left_child is None and node.right_child is None:
                node = None
            # Case 2: the current node has only one child
            elif node.left_child is None:
                # If the current node only has a right child then replace it with the right child
                node = node.right_child
            elif node.right_child is None:
                # If the current node only has a left child then replace it with the left child
                node = node.left_child
            # Case 3: node has two children
            else:
                # Find the node with the minimum value in the current node's right subtree
                min_node = self.minimum(node.right_child)
                # Replace the current node node's data with the minimum value
                node.data = min_node.data
                # Delete the minimum node from the right subtree
                node.right_child = self.delete(min_node.data, node.right_child)
        return node
    
bst = BinarySearchTree()
bst.insert(7)
bst.insert(6)
bst.insert(9)
bst.insert(4)
bst.insert(3)
bst.insert(5)
bst.insert(8)
print(bst.minimum())
print(bst.maximum())
print(bst.search(8))
print(bst.search(20))
bst.delete(7)
print(bst.root)
print(bst.minimum())