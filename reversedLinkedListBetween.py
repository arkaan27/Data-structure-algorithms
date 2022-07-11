"""
Given a linked list and numbers m and n, return it back
with only positions m to n in reverse

Assumptions:
    Will m and n always be within the bounds of the linked list
        Yes assume k =m <= n < = length of linked list
    Can we receive m and n values for the whole list?
        Yes, we can receive m= 1 and n = length of linked list

"""


def reversedLinkedListBetween(head, m, n):
    if m and n <= 1:
        return head
    position = 1
    currentNode = head
    start = head
    while position < m:
        start = currentNode
        currentNode = currentNode.next
        position += 1
    newList = None
    tail = currentNode
    while m <= position <= n:
        next = currentNode.next
        currentNode.next = newList
        newList = currentNode
        currentNode = next
        position += 1

    start.next = newList
    tail.next = currentNode

    return newList


def reverseBetween(head, m, n):
    if not head:
        return None
    currentNode = head
    prev = None
    while m > 1:
        prev = currentNode
        currentNode = currentNode.next
        m, n = m - 1, n - 1

    # The two pointers that will fix the final connections.
    tail = currentNode
    connectNode = prev

    # Iteratively reverse the nodes until n becomes 0.
    while n:
        third = currentNode.next
        currentNode.next = prev
        prev = currentNode
        currentNode = third
        n -= 1

    if connectNode:
        connectNode.next = prev
    else:
        head = prev
    tail.next = currentNode
    return head
