"""
Given a linked list, return it in reverse.

1--> 2 --> 3--> 4 --> 5 --> null

5 --> 4 --> 3 --> 2 --> 1 --> null

"""


def reversedLinkedList(head):
    # Time: O(n)
    # Space: O(1)
    currentNode = head
    prev = None
    while currentNode is not None:
        next = currentNode.next
        currentNode.next = prev
        prev = currentNode
        currentNode = next

    return prev