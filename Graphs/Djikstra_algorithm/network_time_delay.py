"""
There are n network nodes labelled 1 to N.

Given a times array, containing edges represented by arrays [u, v, w] where 'u' is the source node, 'v' is the target
node, and 'w' is the time taken to travel rom the source node to the target node.

Send a signal from node k, return how long it takes for all nodes to receive the signal. Return -1 if it's impossible.


Verify the constraints:

Can the graph be unconnected?
Yes, account for an unconnected graph

Can the time be negative integers?
No, the weight of edges is always positive

"""

import heapq  # Import the heapq module to use the heap queue (or priority queue) algorithm


class PriorityQueue:
    def __init__(self, comparator=lambda a, b: a < b):
        self.heap = []
        self.comparator = comparator

    def size(self):
        return len(self.heap)

    def peek(self):
        return self.heap[0] if self.heap else None

    def isEmpty(self):
        return not self.heap

    def push(self, value):
        heapq.heappush(self.heap, value)
        return self.size()

    def pop(self):
        return heapq.heappop(self.heap) if self.heap else None


def network_delay_time(times, N, k):
    distances = [float('inf')] * N
    adj_list = [[] for _ in range(N)]
    distances[k - 1] = 0

    heap = PriorityQueue(lambda a, b: distances[a] < distances[b])
    heap.push(k - 1)

    for source, target, weight in times:
        adj_list[source - 1].append((target - 1, weight))

    while not heap.isEmpty():
        current_vertex = heap.pop()

        for neighboring_vertex, weight in adj_list[current_vertex]:
            if distances[current_vertex] + weight < distances[neighboring_vertex]:
                distances[neighboring_vertex] = distances[current_vertex] + weight
                heap.push(neighboring_vertex)

    ans = max(distances)
    return -1 if ans == float('inf') else ans


if __name__ == '__main__':
    times = [[1, 2, 9], [1, 4, 2], [2, 5, 1], [4, 2, 4], [4, 5, 6], [3, 2, 3], [5, 3, 7], [3, 1, 5]]

    print(network_delay_time(times, 5, 1))
