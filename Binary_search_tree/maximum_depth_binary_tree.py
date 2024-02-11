from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def max_depth(node: Optional[TreeNode], curr_depth):
    if node is None:
        return curr_depth
    curr_depth += 1
    return max(max_depth(node.left, curr_depth),
               max_depth(node.right, curr_depth))
