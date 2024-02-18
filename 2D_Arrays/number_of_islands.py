"""

Given a 2D array containing only 1's (land) and 0's (water), count the number of islands

An island is land connected horizontally or vertically

"""
from collections import deque

test_matrix = [
    [1, 1, 1, 1, 0],
    [1, 1, 0, 1, 0],
    [1, 1, 0, 0, 1],
    [0, 0, 0, 1, 1]
]

directions = [
    [-1, 0],  # up
    [0, 1],  # right
    [1, 0],  # down
    [0, -1]  # left
]


# BFS is a better solution in this case due to it not using a stack or recursive nature. This means the space complexity
# is lower and hence a better approach.

def number_of_islands_bfs(matrix):
    if not matrix or not matrix[0]:
        return 0

    island_count = 0
    rows, cols = len(matrix), len(matrix[0])

    for row in range(rows):
        for col in range(cols):
            if matrix[row][col] == 1:
                island_count += 1
                matrix[row][col] = 0
                queue = deque([(row, col)])

                while queue:
                    current_row, current_col = queue.popleft()
                    for dr, dc in directions:
                        next_row, next_col = current_row + dr, current_col + dc
                        if 0 <= next_row < rows and 0 <= next_col < cols and matrix[next_row][next_col] == 1:
                            queue.append((next_row, next_col))
                            matrix[next_row][next_col] = 0

    return island_count


def dfs(matrix, current_row, current_col):
    if current_row < 0 or current_row >= len(matrix) or current_col < 0 or current_col >= len(matrix[0]) or \
            matrix[current_row][current_col] == 0:
        return

    if matrix[current_row][current_col] == 1:
        matrix[current_row][current_col] = 0

    for dr, dc in directions:
        dfs(matrix, current_row + dr, current_col + dc)


def number_of_islands_dfs(matrix):
    if not matrix or not matrix[0]:
        return 0

    island_count = 0
    for row in range(len(matrix)):
        for col in range(len(matrix[0])):
            if matrix[row][col] == 1:
                island_count += 1
                dfs(matrix, row, col)
    return island_count
