"""
Given a linked list, return it in reverse.

1--> 2 --> 3--> 4 --> 5 --> null

5 --> 4 --> 3 --> 2 --> 1 --> null

"""


def reversed_linked_list(head):
    # Time: O(n)
    # Space: O(1)
    current_node = head
    prev = None
    while current_node is not None:
        next = current_node.next
        current_node.next = prev
        prev = current_node
        current_node = next

    return prev
