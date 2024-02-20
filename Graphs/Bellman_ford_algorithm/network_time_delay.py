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


def network_delay_time(times, N, k):
    distances = [float('inf')] * N
    distances[k - 1] = 0

    for _ in range(N - 1):
        count = 0
        for source, target, weight in times:
            if distances[source - 1] + weight < distances[target - 1]:
                distances[target - 1] = distances[source - 1] + weight
                count += 1

        if count == 0:
            break

    ans = max(distances)
    return -1 if ans == float('inf') else ans


if __name__ == '__main__':
    times = [[1, 4, 2], [1, 2, 9], [4, 2, -4], [2, 5, -3], [4, 5, 6], [3, 2, 3], [5, 3, 7], [3, 1, 5]]

    print(network_delay_time(times, 5, 1))
