from collections import deque

adjacency_list = [
    [1, 3],
    [0],
    [3, 8],
    [0, 2, 4, 5],
    [3, 6],
    [3],
    [4, 7],
    [6],
    [2]
]


def traversal_bfs_graph(graph):
    queue = deque([0])
    values = []
    seen = set()

    while queue:
        vertex = queue.popleft()
        if vertex not in seen:
            values.append(vertex)
            seen.add(vertex)

            for connection in graph[vertex]:
                if connection not in seen:
                    queue.append(connection)

    return values


if __name__ == "__main__":
    print(traversal_bfs_graph(adjacency_list))
