from collections import deque

test_matrix = [
    [1, 2, 3, 4, 5],
    [6, 7, 8, 9, 10],
    [11, 12, 13, 14, 15],
    [16, 17, 18, 19, 20]
]

directions = [
    [-1, 0],  # up
    [0, 1],  # right
    [1, 0],  # down
    [0, -1]  # left
]


def traversal_bfs(matrix):
    seen = [[False for _ in row] for row in matrix]
    values = []
    queue = deque([(0, 0)])  # Start from the top-left corner

    while queue:
        row, col = queue.popleft()

        if row < 0 or row >= len(matrix) or col < 0 or col >= len(matrix[0]) or seen[row][col]:
            continue

        seen[row][col] = True
        values.append(matrix[row][col])

        for direction in directions:
            next_row, next_col = row + direction[0], col + direction[1]
            queue.append((next_row, next_col))

    return values


if __name__ == "__main__":
    print(traversal_bfs(test_matrix))
