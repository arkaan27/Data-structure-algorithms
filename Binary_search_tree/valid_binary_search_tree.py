"""

Given the root of a binary tree, determine if it is a valid binary search tree (BST)

A valid BST is defined as follows:

The left subtree of a node contains only nodes with keys less than the node's key.
The right subtree of a node contains only nodes with keys greater than the node's key.
Both the left and right subtrees must also be binary search trees.

Can there be duplicate values in the tree?

Yes, if you receive duplicate values the tree is not a valid binary search tree
"""
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def is_valid_bst(root: Optional[TreeNode]) -> bool:
    if root is None:
        return True
    return dfs(root, float('-inf'), float('inf'))


def dfs(node: Optional[TreeNode], min_val, max_val):
    if node.val <= min_val or node.val >= max_val:
        return False
    if node.left:
        if not dfs(node.left, min_val, node.val):
            return False
    if node.right:
        if not dfs(node.right, node.val, min_val):
            return False
