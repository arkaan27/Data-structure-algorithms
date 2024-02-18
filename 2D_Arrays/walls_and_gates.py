"""

Given a 2D array containing -1's (walls), 0's (gates) and INF's (empty room).
Fill each empty room with the number of steps to the nearest gate.

If it is impossible to reach a gate, leave INF as the value. INFq is equal to 2147483647
"""


INF = 2147483647

test_matrix = [
    [INF, -1, 0, INF],
    [INF, INF, INF, 0],
    [INF, -1, INF, -1],
    [0, -1, INF, INF]
]

WALL = -1
GATE = 0
EMPTY = INF
directions = [
    (-1, 0),  # up
    (0, 1),  # right
    (1, 0),  # down
    (0, -1)  # left
]


def dfs(matrix, row, col, count):
    if row < 0 or row >= len(matrix) or col < 0 or col >= len(matrix[0]) or count > matrix[row][col]:
        return
    matrix[row][col] = count
    for direction in directions:
        next_row, next_col = row + direction[0], col + direction[1]
        dfs(matrix, next_row, next_col, count + 1)


def walls_and_gates(rooms):
    for row in range(len(rooms)):
        for col in range(len(rooms[0])):
            if rooms[row][col] == GATE:
                dfs(rooms, row, col, 0)


if __name__ == "__main__":
    walls_and_gates(test_matrix)
    for row in test_matrix:
        print(row)
