"""

Create a function that solves for any 9x9 sudoku puzzle given.

Each of the digits 1-9 must occur exactly once in each row.
Each of the digits 1-9 must occur exactly once in each column

Each of the digits 1-9 must occur exactly once in each of the 9 3x3 sub-boxes of the grid.


"""


def get_box_id(row, col):
    row_val = (row // 3) * 3
    col_val = col // 3
    return row_val + col_val


def is_valid(box, row, col, num):
    if num in box or num in row or num in col:
        return False
    return True


def solve_backtrack(board, boxes, rows, cols, r, c):
    if r == len(board) or c == len(board[0]):
        return True
    else:
        if board[r][c] == '.':
            for num in range(1, 10):
                num_val = str(num)
                board[r][c] = num_val

                box_id = get_box_id(r, c)
                box = boxes[box_id]
                row = rows[r]
                col = cols[c]

                if is_valid(box, row, col, num_val):
                    box[num_val] = True
                    row[num_val] = True
                    col[num_val] = True

                    if c == len(board[0]) - 1:
                        if solve_backtrack(board, boxes, rows, cols, r + 1, 0):
                            return True
                    else:
                        if solve_backtrack(board, boxes, rows, cols, r, c + 1):
                            return True

                    del box[num_val]
                    del row[num_val]
                    del col[num_val]

                board[r][c] = '.'
        else:
            if c == len(board[0]) - 1:
                if solve_backtrack(board, boxes, rows, cols, r + 1, 0):
                    return True
            else:
                if solve_backtrack(board, boxes, rows, cols, r, c + 1):
                    return True

    return False


def solve_sudoku(board):
    n = len(board)
    boxes = [{} for _ in range(n)]
    rows = [{} for _ in range(n)]
    cols = [{} for _ in range(n)]

    for r in range(n):
        for c in range(n):
            if board[r][c] != '.':
                box_id = get_box_id(r, c)
                val = board[r][c]
                boxes[box_id][val] = True
                rows[r][val] = True
                cols[c][val] = True

    solve_backtrack(board, boxes, rows, cols, 0, 0)


if __name__ == "__main__":
    board = [
        ['5', '3', '.', '.', '7', '.', '.', '.', '.'],
        ['6', '.', '.', '1', '9', '5', '.', '.', '.'],
        ['.', '9', '8', '.', '.', '.', '.', '6', '.'],
        ['8', '.', '.', '.', '6', '.', '.', '.', '3'],
        ['4', '.', '.', '8', '.', '3', '.', '.', '1'],
        ['7', '.', '.', '.', '2', '.', '.', '.', '6'],
        ['.', '6', '.', '.', '.', '.', '2', '8', '.'],
        ['.', '.', '.', '4', '1', '9', '.', '.', '5'],
        ['.', '.', '.', '.', '8', '.', '.', '7', '9'],
    ]

    new_board = [
        ['3', '.', '.', '.', '.', '9', '.', '.', '5'],
        ['.', '2', '5', '.', '.', '8', '.', '1', '.'],
        ['6', '.', '.', '.', '2', '.', '.', '.', '.'],
        ['.', '.', '.', '.', '.', '1', '4', '.', '.'],
        ['2', '.', '.', '.', '.', '.', '.', '.', '.'],
        ['.', '7', '9', '.', '8', '.', '.', '.', '6'],
        ['.', '.', '.', '9', '.', '.', '.', '6', '.'],
        ['.', '.', '3', '.', '.', '.', '.', '.', '.'],
        ['.', '5', '8', '.', '7', '.', '.', '.', '9'],
    ]

    solve_sudoku(new_board)

    for row in new_board:
        print(row)
