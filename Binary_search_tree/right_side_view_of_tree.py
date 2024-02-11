"""
Given a binary tree imagine you're standing to the right of the
tree. Return an array of the values of the nodes you can see
ordered from top to bottom

"""
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def right_side_view(root: Optional[TreeNode]):
    result = []
    traverse_inorder(root, result)
    return result


def traverse_inorder(node, array, level=0):
    if node is None:
        return
    if level >= len(array):
        array.append(node.value)
    if node.right:
        traverse_inorder(node.right, array, level + 1)
    if node.left:
        traverse_inorder(node.right, array, level + 1)
    return array
