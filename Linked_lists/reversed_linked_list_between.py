"""
Given a linked list and numbers m and n, return it back
with only positions m to n in reverse

Assumptions:
    Will m and n always be within the bounds of the linked list
        Yes assume k =m <= n < = length of linked list
    Can we receive m and n values for the whole list?
        Yes, we can receive m= 1 and n = length of linked list

"""


def reversed_linked_list_between(head, m, n):
    if m and n <= 1:
        return head
    position = 1
    current_node = head
    start = head
    while position < m:
        start = current_node
        current_node = current_node.next
        position += 1
    new_list = None
    tail = current_node
    while m <= position <= n:
        next = current_node.next
        current_node.next = new_list
        new_list = current_node
        current_node = next
        position += 1

    start.next = new_list
    tail.next = current_node

    return new_list


def reverse_between(head, m, n):
    if not head:
        return None
    current_node = head
    prev = None
    while m > 1:
        prev = current_node
        current_node = current_node.next
        m, n = m - 1, n - 1

    # The two pointers that will fix the final connections.
    tail = current_node
    connect_node = prev

    # Iteratively reverse the nodes until n becomes 0.
    while n:
        third = current_node.next
        current_node.next = prev
        prev = current_node
        current_node = third
        n -= 1

    if connect_node:
        connect_node.next = prev
    else:
        head = prev
    tail.next = current_node
    return head
