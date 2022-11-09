import gomoku
    
def score(board):
    MAX_SCORE = 100000
    
    open_b = {}
    semi_open_b = {}
    open_w = {}
    semi_open_w = {}
    
    for i in range(2, 6):
        open_b[i], semi_open_b[i] = detect_rows(board, "b", i)
        open_w[i], semi_open_w[i] = detect_rows(board, "w", i)
        
    
    if open_b[5] >= 1 or semi_open_b[5] >= 1:
        return MAX_SCORE
    
    elif open_w[5] >= 1 or semi_open_w[5] >= 1:
        return -MAX_SCORE
        
    return (-10000 * (open_w[4] + semi_open_w[4])+ 
            500  * open_b[4]                     + 
            50   * semi_open_b[4]                + 
            -100  * open_w[3]                    + 
            -30   * semi_open_w[3]               + 
            50   * open_b[3]                     + 
            10   * semi_open_b[3]                +  
            open_b[2] + semi_open_b[2] - open_w[2] - semi_open_w[2])

def wipe(board):
    for row in range(len(board)):
        for col in range(len(board)):
            board[row][col] = " "
         
if __name__ == '__main__':
    board = [[' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
            [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
            [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
            [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
            [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
            [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
            [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
            [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']]

    print(gomoku.search_max(board))

    board_2 = [[' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
            [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
            [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
            [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
            [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
            [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
            [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
            [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']]

    gomoku.put_seq_on_board(board_2, y=0, x=0, d_y=1, d_x=1, length=2, col="b")
    gomoku.print_board(board_2)
    print(gomoku.detect_row(board_2, col = "b", y_start=0, x_start=0, length=2, d_y=1, d_x=1))
    #Output: (0,1)

    gomoku.put_seq_on_board(board_2, y=3, x=3, d_y=1, d_x=1, length=3, col="b")
    gomoku.print_board(board_2)
    print(gomoku.detect_row(board_2, col = "b", y_start=0, x_start=0, length=3, d_y=1, d_x=1))
    #Output: (1,0)

    board_2[2][2] = "w"
    board_2[6][6] = "w"
    gomoku.print_board(board_2)
    print(gomoku.detect_row(board_2, col = "b", y_start=0, x_start=0, length=3, d_y=1, d_x=1))
    #Output: (0,0)

    gomoku.put_seq_on_board(board_2, y=3, x=5, d_y=1, d_x=-1, length=3, col="b")
    gomoku.put_seq_on_board(board_2, y=0, x=2, d_y=1, d_x=-1, length=3, col="b")
    gomoku.put_seq_on_board(board_2, y=3, x=5, d_y=1, d_x=0, length=3, col="b")
    gomoku.put_seq_on_board(board_2, y=3, x=2, d_y=0, d_x=1, length=4, col="b")
    gomoku.print_board(board_2)
    print(gomoku.detect_row(board_2, col = "b", y_start=0, x_start=0, length=3, d_y=1, d_x=1))
    #Output: (0,0)

    print(gomoku.detect_rows(board_2,"b",3))

    wipe(board_2)

    gomoku.put_seq_on_board(board_2, y=4, x=3, d_y=1, d_x=1, length=2, col="b")
    gomoku.print_board(board_2)
    print(gomoku.detect_row(board_2, col = "b", y_start=1, x_start=0, length=2, d_y=1, d_x=1))
    #Output: (1,0)

    gomoku.put_seq_on_board(board_2, y=0, x=7, d_y=1, d_x=-1, length=2, col="w")
    gomoku.print_board(board_2)
    print(gomoku.detect_row(board_2, col = "w", y_start=0, x_start=7, length=2, d_y=-1, d_x=1), "-> wrong row direction of d_y=-1,d_x=1")
    #Output: (0,0)

    print(gomoku.detect_row(board_2, col = "w", y_start=0, x_start=7, length=2, d_y=1, d_x=-1))
    #Output: (1,0)

    wipe(board_2)

    gomoku.put_seq_on_board(board_2, y=5, x=0, d_y=1, d_x=1, length=2, col="w")
    gomoku.print_board(board_2)
    print(gomoku.detect_row(board_2, col = "w", y_start=5, x_start=0, length=2, d_y=1, d_x=1))
    print(gomoku.detect_row(board_2, col = "w", y_start=6, x_start=1, length=2, d_y=-1, d_x=-1))
    #Output: (0,1)\n(0,1)

    board_2[7][2] = "b"
    gomoku.print_board(board_2)
    print(gomoku.detect_row(board_2, col = "w", y_start=5, x_start=0, length=2, d_y=1, d_x=1))
    print(gomoku.detect_row(board_2, col = "w", y_start=6, x_start=1, length=2, d_y=-1, d_x=-1))
    #Output: (0,0)\n(0,0)











