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

adjacency_matrix = [
    [0, 1, 0, 1, 0, 0, 0, 0, 0],
    [1, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 1, 0, 0, 0, 0, 1],
    [1, 0, 1, 0, 1, 1, 0, 0, 0],
    [0, 0, 0, 1, 0, 0, 1, 0, 0],
    [0, 0, 0, 1, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 1, 0, 0, 1, 0],
    [0, 0, 0, 0, 0, 0, 1, 0, 0],
    [0, 0, 1, 0, 0, 0, 0, 0, 0]
]


def traversal_bfs_adj_list(graph):
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


def traversal_bfs_adj_matrix(graph):
    queue = deque([0])
    values = []
    seen = set()

    while queue:
        vertex = queue.popleft()

        if vertex not in seen:
            values.append(vertex)
            seen.add(vertex)

            for v in range(len(graph[vertex])):
                if graph[vertex][v] > 0 and v not in seen:
                    queue.append(v)

    return values


if __name__ == "__main__":
    print(traversal_bfs_adj_list(adjacency_list))
    print(traversal_bfs_adj_matrix(adjacency_matrix))
