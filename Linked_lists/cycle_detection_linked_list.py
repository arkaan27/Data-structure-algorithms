"""
Given the head of a linked list, return the node
where the cycle begins. If there is no cycle, return null.

There is a cycle in a linked list if there is some node in
the list that can be reached again by continuously
following the next pointer. Internally, pos is used to denote the index of the node
that tail's next pointer is connected to (0-indexed).
It is -1 if there is no cycle. Note that pos is not passed as a parameter.

Do not modify the linked list.


"""


def findCycleFloydsMethod(head):
    # Time : O(N)
    # Space: O(1)
    tortoise = head
    hare = head
    if hare is None or hare.next is None:
        return None
    while True:
        hare = hare.next
        tortoise = tortoise.next
        if hare is None or hare.next is None:
            return False
        else:
            hare = hare.next
        if tortoise is hare:
            break
    p1 = head
    p2 = hare
    while p1 is not p2:
        p1 = p1.next
        p2 = p2.next
    return p1


def findCycle(head):
    # Time: O(N)
    # Space: O(N)
    if head is None:
        return None
    currentNode = head
    seenNodes = {}
    p1 = 0
    while currentNode:
        if currentNode in seenNodes:
            return currentNode
        else:
            seenNodes[currentNode] = p1
            currentNode = currentNode.next
            p1 += 1
        return None
    return currentNode
