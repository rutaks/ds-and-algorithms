"""
Given a binary search tree(BST) and a target node K. 
The task is to find the node with minimum absolute 
difference with given target value K.
BST ref: https://www.geeksforgeeks.org/binary-search-tree-data-structure/
"""


# TREE NODE STUCTURE
class node:
    def __init__(self, key):
        self.key = key
        self.right = None
        self.left = None


def find_closest_value(tree, target):
    return find_closest_value_helper(tree, target, tree.key)


# Function traverses in the tree
    # If the difference of the current closest value with target
    # is greater than current node's value, closest value changes
    # If current node is less than current node, will traverse left
    # If current node is great than current node, will traverse right
    # Will end and return closest value if next node is `None`
def find_closest_value_helper(tree, target, closest):
    current_node = tree
    while current_node is not None:
        if abs(target - closest) > abs(target - current_node.key):
            closest = current_node.key
        if target < current_node.key:
            current_node = current_node.left
        elif target > current_node.key:
            current_node = current_node.right
        else:
            break
    return closest


"""
FOLLOWING EXAMPLE NODE STRUCTURE
             12
          /      \
        /          \
        6           16
    /       \   /       \
    3        9  14      18
"""

root = node(12)
root.left = node(6)
root.left.left = node(3)
root.left.right = node(9)

root.right = node(16)
root.right.left = node(14)
root.right.right = node(18)

print(find_closest_value(root, 13))
