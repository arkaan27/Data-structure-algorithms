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
def knight_p(n, k, row, column):
    if k == 0:
        return 1
    if row < 0 or row >= n or column < 0 or column >= n:
        return 0

    result = 0

    for i in range(len(DIRECTIONS)):
        d = DIRECTIONS[i]
        result += knight_p(n, k - 1, row + d[0], column + d[1]) / 8

    return result


if __name__ == "__main__":
    n = 6
    k = 3
    row = 2
    column = 2
    print(knight_p(n, k , row, column))
