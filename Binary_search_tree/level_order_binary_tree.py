"""
Given a binary tree, return the level order traversal of the
nodes values as an array
"""
import queue
from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def level_order(node: Optional[TreeNode]):
    if node is None:
        return []
    curr_node = node
    array = []
    q = queue.SimpleQueue()
    q.put(curr_node)

    while not q.empty():
        length = q.qsize()
        count = 0
        curr_level_values = []
        while count < length:
            curr_node = q.get()
            curr_level_values.append(curr_node.value)
            if curr_node.left:
                q.put(curr_node.left)
            if curr_node.right:
                q.put(curr_node.right)
            count += 1
        array.append(curr_level_values)

    return array
