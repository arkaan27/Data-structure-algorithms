"""

Given a doubly linked list, list nodes also have
a child property that can point to a separate doubly
linked list. These child lists can also have one or
more child doubly linked lists of their own, and so on.

Return the list as a single level flattened doubly linked list.

# Multi Level Doubly Linked List class without child property:

class ListNode{
    value: any
    prev: ListNode
    next: ListNode
}

# Multi Level Doubly Linked List class with child property

class ListNode{
    value: any
    prev: ListNode
    next: ListNode
    child: ListNode
}

# Visual Representation of Doubly Linked List

null<= 1 <=> 2 <=> 3 => null
            ||
     null <= 4 <=> 5 <=> 6 => null
                   ||
            null<= 7 => null

# Constraints:

    1. Can a doubly linked list have multiple child list nodes?
            Yes every list node can have multiple level of children.
    2. What do we do with child properties after flattening?
            Just set the child property value to null.

"""

# Test cases:

# 1. Doubly Linked List given: Best case test case
#   1  - 2 - 3 - 4 - 5 - 6
#        |           |
#        7 - 8 - 9   12 - 13
#            |
#            10 - 11

# Solution:
#  1 - 2 - 7 - 8 - 10 - 11 - 9 - 3 - 4 - 5 - 12 - 13 - 6

# 2. Doubly Linked List given:
# null

# Solution:
# null

# 3. Doubly Linked List given:
# 8

# Solution:
# 8


def flatten_multi_level_doubly_linked_list(head):
    # Space: O(1)
    # Time: O(N)
    if head is None:
        return head
    current_node = head
    while current_node is not None:
        if current_node.child is None:
            current_node = current_node.next
        else:
            tail = current_node.child
            while tail.next is not None:
                tail = tail.next
            tail.next = current_node.next
            if tail.next is not None:
                tail.next.prev = tail
            current_node.next = current_node.child
            current_node.next.prev = current_node
            current_node.child = None

    return head
