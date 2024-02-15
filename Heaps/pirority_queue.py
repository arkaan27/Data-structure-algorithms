import heapq


class PriorityQueue:
    def __init__(self, comparator=lambda a, b: a < b):
        self.heap = []
        self.comparator = comparator

    def size(self):
        return len(self.heap)

    def peek(self):
        return self.heap[0] if self.heap else None

    def is_empty(self):
        return not self.heap

    def push(self, value):
        # Invert value for max heap, if the comparator is for a max heap
        value = (value, value) if self.comparator(0, 1) else (-value, value)
        heapq.heappush(self.heap, value)
        return self.size()

    def pop(self):
        if self.heap:
            value = heapq.heappop(self.heap)
            return value[1] if self.comparator(0, 1) else -value[0]


# Example usage
pq = PriorityQueue(lambda a, b: a > b)  # Max heap
pq.push(15)
pq.push(12)
pq.push(50)
pq.push(7)
pq.push(40)
pq.push(22)

while not pq.is_empty():
    print(pq.pop())
