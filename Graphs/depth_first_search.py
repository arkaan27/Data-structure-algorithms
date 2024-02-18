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


def traversal_dfs_adj_list(vertex, graph, values, seen):
    values.append(vertex)
    seen[vertex] = True

    connections = graph[vertex]
    for connection in connections:
        if connection not in seen:
            traversal_dfs_adj_list(connection, graph, values, seen)


def traversal_dfs_adj_matrix(vertex, graph, values, seen):
    values.append(vertex)
    seen[vertex] = True

    connections = graph[vertex]
    for v in range(len(connections)):
        if connections[v] > 0 and v not in seen:
            traversal_dfs_adj_matrix(v, graph, values, seen)


if __name__ == "__main__":
    values = []
    traversal_dfs_adj_list(0, adjacency_list, values, {})
    print(values)
    traversal_dfs_adj_matrix(0, adjacency_matrix, values=[], seen={})
    print(values)
