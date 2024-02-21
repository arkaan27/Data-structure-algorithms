"""

On a given nxn chessboard, a knight piece will start at the r-th row and c-th column. The knight will attempt to make k
moves.

A knight can move in 8 possible ways. Each move will choose one of these 8 at random. The knight continues moving until
it finishes k moves, or it moves off the chessboard. Return the probability that the knight is on the chessboard after
it finishes moving.

"""

DIRECTIONS = [
    [-2, -1],
    [-2, 1],
    [-1, 2],
    [1, 2],
    [2, 1],
    [2, -1],
    [1, -2],
    [-1, -2]
]


# Recursive solution without dynamic programming
# Time: O(8^k) Space O(8^k)
def knight_p_recurs(n, k, row, column):
    if k == 0:
        return 1
    if row < 0 or row >= n or column < 0 or column >= n:
        return 0

    result = 0

    for i in range(len(DIRECTIONS)):
        d = DIRECTIONS[i]
        result += knight_p_recurs(n, k - 1, row + d[0], column + d[1]) / 8

    return result


# Applying dynamic programming to reduce time complexity:
# Time: O(N^2 x k) Space: O(N^2 x k)
def knight_p_dp(n, k, row, column):
    dp = [[[None for _ in range(k + 1)] for _ in range(n)] for _ in range(n)]
    return recurse(n, k, row, column, dp)


def recurse(n, k, row, column, dp):
    if k == 0:
        return 1
    if row < 0 or row >= n or column < 0 or column >= n:
        return 0

    if dp[row][column][k] is not None:
        return dp[row][column][k]

    response = 0
    for d in DIRECTIONS:
        response += recurse(n, k - 1, row + d[0], column + d[1], dp) / 8

    dp[row][column][k] = response
    return response


# Bottom up iterative solution

def knight_p_bu(n, k, row, column):
    dp = [[[0 for _ in range(n)] for _ in range(n)] for _ in range(k + 1)]
    dp[0][row][column] = 1

    for step in range(1, k + 1):
        for r in range(n):
            for c in range(n):
                for d in DIRECTIONS:
                    prev_row, prev_col = r + d[0], c + d[1]
                    if 0 <= prev_row < n and 0 <= prev_col < n:
                        dp[step][r][c] += (dp[step - 1][prev_row][prev_col]) / 8

    result = 0
    for i in range(n):
        for j in range(n):
            result += dp[k][i][j]
    return result


# Bottom up optimised solution with just two arrays in space.

def knight_p_optimised(n, k , r, c):
    prev_dp = [[0 for _ in range(n)] for _ in range(n)]
    next_dp = [[0 for _ in range(n)] for _ in range(n)]
    prev_dp[r][c] = 1

    for step in range(1, k + 1):
        for row in range(n):
            for col in range(n):
                for curr_dir in DIRECTIONS:
                    prev_row = row + curr_dir[0]
                    prev_col = col + curr_dir[1]
                    if 0 <= prev_row < n and 0 <= prev_col < n:
                        next_dp[row][col] += prev_dp[prev_row][prev_col] / 8

        prev_dp, next_dp = next_dp, [[0 for _ in range(n)] for _ in range(n)]

    result = 0

    result += sum(sum(row) for row in prev_dp)

    return result


if __name__ == "__main__":
    n = 6
    k = 3
    row = 2
    column = 2
    print(knight_p_recurs(n, k, row, column))
    print(knight_p_dp(n, k, row, column))
    print(knight_p_bu(n, k, row, column))
    print(knight_p_optimised(n, k, row, column))
