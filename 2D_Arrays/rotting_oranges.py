"""

Given a 2D array containing 0's (empty cell), 1's (fresh orange) and 2's (rotten orange).
Every minute, all fresh orange immediately adjacent (4 directions) to rotten oranges will rot.

How many minutes must pass until all oranges are rotten?

Verify Constraints:

What do we return if there are no oranges?
Return 0 if there are no oranges.
"""
from collections import deque

test_matrix = [
    [2, 1, 1, 0, 0],
    [1, 1, 1, 0, 0],
    [0, 1, 1, 1, 1],
    [0, 1, 0, 0, 1]
]

test_matrix_null_case = [
    [1, 1, 0, 0, 0],
    [2, 1, 0, 0, 0],
    [0, 0, 0, 1, 2],
    [0, 1, 0, 0, 1]
]

empty_matrix = []

empty_matrix_2 = [
    [],
    []
]

directions = [
    [-1, 0],  # up
    [0, 1],  # right
    [1, 0],  # down
    [0, -1]  # left
]

rotten = 2
fresh = 1
empty = 0


def rotten_oranges(matrix):
    if not matrix or not matrix[0]:
        return 0
    q = deque()
    fresh_oranges = 0
    # Sequential traverse to get fresh oranges & rotten oranges coordinates in to queue
    rows, cols = len(matrix), len(matrix[0])

    for row in range(rows):
        for col in range(cols):
            if matrix[row][col] == rotten:
                q.append([row, col])
            if matrix[row][col] == fresh:
                fresh_oranges += 1

    # Rot the oranges adjacent using BFS and add to the queue tracking the queue length & reducing the fresh oranges
    minutes_passed = 0
    while q and fresh_oranges > 0:
        for _ in range(len(q)):
            curr_orange_row, curr_orange_col = q.popleft()
            for delta_row, delta_col in directions:
                adj_row, adj_col = curr_orange_row + delta_row, curr_orange_col + delta_col
                if 0 <= adj_row < rows and 0 <= adj_col < cols and matrix[adj_row][adj_col] == 1:
                    matrix[adj_row][adj_col] = 2
                    fresh_oranges -= 1
                    q.append([adj_row, adj_col])
        minutes_passed += 1

    return minutes_passed if fresh_oranges == 0 else -1


if __name__ == '__main__':
    print(rotten_oranges(test_matrix))
    print(rotten_oranges(test_matrix_null_case))
    print(rotten_oranges(empty_matrix))
    print(rotten_oranges(empty_matrix_2))