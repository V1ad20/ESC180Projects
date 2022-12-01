import gomoku

if __name__ == '__main__':
    board = [[' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
            [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
            [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
            [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
            [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
            [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
            [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
            [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']]
    # put_seq_on_board(board, y, x, d_y, d_x, length, col):
    # detect_row(board, col, y_start, x_start, length, d_y, d_x):


    gomoku.put_seq_on_board(board, 1, 1, 0, 1, 1, "w")
    gomoku.put_seq_on_board(board, 1, 2, 0, 1, 5, "b")
    gomoku.put_seq_on_board(board, 1, 7, 0, 1, 1, "w")

    gomoku.print_board(board)

    # print(detect_row(board, "b", 1, 1, 3, 1, 0))
    print(gomoku.detect_row(board, 'b', 1, 0, 5, 0, 1))
    print(gomoku.detect_row2(board, 'b', 1, 0, 5, 0, 1))
    print(gomoku.detect_rows(board, 'b', 5))
    print(gomoku.detect_rows2(board, 'b', 5))
    print(gomoku.detect_rows2(board, 'w', 5))

    print(gomoku.is_win(board))