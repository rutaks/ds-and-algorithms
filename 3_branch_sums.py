"""
Given a binary tree,
determine the sum of individual branches
"""


# BST  NODE STUCTURE
class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None


def branch_sums(tree):
    sums = []
    sum_branches(tree, 0, sums)
    return sums


# Function recursively traverses a tree by starting
# from the left node, while keeping track of
# the current branche's value
    # If current node is empty, function terminates
def sum_branches(node, running_sum, sum_array):
    if node is None:
        return
    new_sum = running_sum + node.key
    if node.left is None and node.right is None:
        sum_array.append(new_sum)
        return
    sum_branches(node.left, new_sum, sum_array)
    sum_branches(node.right, new_sum, sum_array)


"""
FOLLOWING EXAMPLE NODE STRUCTURE
             12
          /      \
        /          \
        6           16
    /       \   /       \
    3        9  14      18
"""

root = Node(12)
root.left = Node(6)
root.left.left = Node(3)
root.left.right = Node(9)

root.right = Node(16)
root.right.left = Node(14)
root.right.right = Node(18)

print(branch_sums(root))
