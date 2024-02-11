"""

Given a Complete Binary Tree, Count the Number of nodes
"""
from typing import Optional
import math


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def count_nodes(node: Optional[TreeNode]):
    if not node:
        return
    height = get_tree_height(node)
    if height == 0:
        return 1
    upper_count = math.pow(2, height) - 1
    left = binary_search_traversal(node, 0, upper_count, height)

    return upper_count + left + 1


def get_tree_height(node: Optional[TreeNode]):
    height = 0
    while node.left is not None:
        height += 1
        node = node.left
    return height


def binary_search_traversal(node: Optional[TreeNode], left, right, height):
    while left <= right:
        idx_to_find = math.ceil((left + right) / 2)
        if node_exists(idx_to_find, height, node):
            left = idx_to_find
        else:
            right = idx_to_find - 1

    return left


def node_exists(element, height, node):
    left = 0
    right = math.pow(2, height) - 1
    count = 0
    while count < height:
        mid_of_node = math.ceil((left + right) / 2)
        if element >= mid_of_node:
            node = node.right
            left = mid_of_node
        else:
            node = node.left
            right = mid_of_node

        count += 1

    return node is not None
