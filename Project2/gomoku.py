"""ESC180 Project 2
By: Vlad Surdu and Seok-Gyu (Brian) Kang
Due: 11/15/2022"""

def is_empty(board):
    for row in board:
        for sq in row:
            if sq != " ":
                return False

    return True
    
def is_bounded(board, y_end, x_end, length, d_y, d_x):
    open_rating = 0
    end_border = (y_end + d_y, x_end + d_x)
    start_border = (y_end-d_y*length,x_end-d_x*length)

    if (end_border[0] >= 0 and end_border[0] < len(board)):
        if (end_border[1] >= 0 and end_border[1] < len(board)):
            if (board[end_border[0]][end_border[1]] == " "):
                open_rating+=1
    
    if (start_border[0] >= 0 and start_border[0] < len(board)):
        if (start_border[1] >= 0 and start_border[1] < len(board)):
            if (board[start_border[0]][start_border[1]] == " "):
                open_rating+=1
    
    if open_rating == 2:
        return "OPEN"
    if open_rating == 1:
        return "SEMIOPEN"
    if open_rating == 0:
        return "CLOSED"
    
def detect_row(board, col, y_start, x_start, length, d_y, d_x):
    num_open = 0
    num_semi_open = 0
    type = ""
    max = max_range(board,y_start, x_start, d_y, d_x)
    
    i = 0
    while (i < max):
        j = i
        while (board[y_start+j*d_y][x_start+j*d_x] == col and j < max - 1):
            j += 1  

        if (j == max - 1 and board[y_start+j*d_y][x_start+j*d_x] == col):
            j += 1

        if j-i == length:
            j -= 1
            type = is_bounded(board,y_start+j*d_y,x_start+j*d_x,length,d_y,d_x)
            if type == "OPEN":
                num_open += 1
            elif type == "SEMIOPEN":
                num_semi_open += 1

        i = j
        i += 1
    
    return (num_open,num_semi_open)

def detect_row2(board, col, y_start, x_start, length, d_y, d_x):
    num_open = 0
    num_semi_open = 0
    num_closed = 0
    type = ""
    max = max_range(board,y_start, x_start, d_y, d_x)
    
    i = 0
    while (i < max):
        j = i
        while (board[y_start+j*d_y][x_start+j*d_x] == col and j < max - 1):
            j += 1  

        if (j == max - 1 and board[y_start+j*d_y][x_start+j*d_x] == col):
            j += 1

        if j-i == length:
            j -= 1
            type = is_bounded(board,y_start+j*d_y,x_start+j*d_x,length,d_y,d_x)
            if type == "OPEN":
                num_open += 1
            elif type == "SEMIOPEN":
                num_semi_open += 1
            elif type == "CLOSED":
                num_closed += 1

        i = j
        i += 1
    
    return (num_open,num_semi_open,num_closed)

def max_range(board,y_start, x_start, d_y, d_x):
    if d_y == 0 and d_x == 0:
        return 0

    y_max = len(board)
    x_max = len(board)

    if d_y == 1:
        y_max = len(board)-y_start
    elif d_y == -1:
        y_max = y_start + 1
        
    if d_x == 1:
        x_max = len(board)-x_start
    elif d_x == -1:
        x_max = x_start + 1

    return min(y_max,x_max)
    
def detect_rows(board, col, length):
    open_seq_count, semi_open_seq_count = 0, 0
    detected = (0, 0)

    for size in range(len(board)):
        detected = detect_row(board, col, size, 0, length, 0, 1) # at each row check all the columns (0, 1)
        open_seq_count += detected[0]
        semi_open_seq_count += detected[1]

        detected = detect_row(board, col, 0, size, length, 1, 0) # at each column check all the rows (1, 0)
        open_seq_count += detected[0]
        semi_open_seq_count += detected[1]

        if size >= length: 

            #Left to right diagonal checks
            #starts from bottom left corner
            detected = detect_row(board, col, len(board) - size, 0, length, 1, 1)
            open_seq_count += detected[0]
            semi_open_seq_count += detected[1]

            #starts from top right corner
            detected = detect_row(board, col, 0, len(board) - size, length, 1, 1) 
            open_seq_count += detected[0]
            semi_open_seq_count += detected[1]

            #Right to left checks
            #starts from bottom right corner
            detected = detect_row(board, col, len(board) - 1, len(board) - size, length, -1, 1) 
            open_seq_count += detected[0]
            semi_open_seq_count += detected[1]

            #starts from top left corner
            detected = detect_row(board, col, 0, size-1, length, 1, -1) 
            open_seq_count += detected[0]
            semi_open_seq_count += detected[1]

    detected = detect_row(board, col, 0, 0, length, 1, 1)
    open_seq_count += detected[0]
    semi_open_seq_count += detected[1]

    detected = detect_row(board, col, 0, 7, length, 1, -1) 
    open_seq_count += detected[0]
    semi_open_seq_count += detected[1]

    return open_seq_count, semi_open_seq_count

def detect_rows2(board, col, length):
    open_seq_count, semi_open_seq_count, closed_seq_count = 0, 0, 0
    detected = (0, 0, 0)

    for size in range(len(board)):
        detected = detect_row2(board, col, size, 0, length, 0, 1) # at each row check all the columns (0, 1)
        open_seq_count += detected[0]
        semi_open_seq_count += detected[1]
        closed_seq_count += detected[2]

        detected = detect_row2(board, col, 0, size, length, 1, 0) # at each column check all the rows (1, 0)
        open_seq_count += detected[0]
        semi_open_seq_count += detected[1]
        closed_seq_count += detected[2]

        if size >= length: 

            #Left to right diagonal checks
            #starts from bottom left corner
            detected = detect_row2(board, col, len(board) - size, 0, length, 1, 1)
            open_seq_count += detected[0]
            semi_open_seq_count += detected[1]
            closed_seq_count += detected[2]

            #starts from top right corner
            detected = detect_row2(board, col, 0, len(board) - size, length, 1, 1) 
            open_seq_count += detected[0]
            semi_open_seq_count += detected[1]
            closed_seq_count += detected[2]

            #Right to left checks
            #starts from bottom right corner
            detected = detect_row2(board, col, len(board) - 1, len(board) - size, length, -1, 1) 
            open_seq_count += detected[0]
            semi_open_seq_count += detected[1]
            closed_seq_count += detected[2]

            detected = detect_row2(board, col, 0, size-1, length, 1, -1) 
            open_seq_count += detected[0]
            semi_open_seq_count += detected[1]
            closed_seq_count += detected[2]

    detected = detect_row2(board, col, 0, 0, length, 1, 1)
    open_seq_count += detected[0]
    semi_open_seq_count += detected[1]
    closed_seq_count += detected[2]

    detected = detect_row2(board, col, 0, 7, length, 1, -1) 
    open_seq_count += detected[0]
    semi_open_seq_count += detected[1]
    closed_seq_count += detected[2]

    return open_seq_count, semi_open_seq_count, closed_seq_count

def search_max(board):
    move_y, move_x = -1, -1 #placeholders assuming there will be a place that is empty and has a score above 0
    max_score = 0

    for y_test in range(len(board)):
        for x_test in range(len(board[0])):
            if board[y_test][x_test] == " ": # if there is no stone already at the location
                board[y_test][x_test] = "b"

                if max_score < score(board): # if score at this location is higher than previous highest score
                    max_score = score(board)
                    move_y, move_x = y_test, x_test
                
                board[y_test][x_test] = " "

    return move_y, move_x
    
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
    
def is_win(board):
    white = detect_rows2(board, "w", 5)
    black = detect_rows2(board, "b", 5)
    
    if (white[0] + white[1] + white[2]) > 0:
        return("White won")
    elif (black[0] + black[1] + black[2]) > 0:
        return("Black won")
    else:
        for y_test in range(len(board)):
            for x_test in range(len(board[0])):
                if board[y_test][x_test] == " ":
                    return("Continue playing")
        return("Draw")

def print_board(board):
    
    s = "*"
    for i in range(len(board[0])-1):
        s += str(i%10) + "|"
    s += str((len(board[0])-1)%10)
    s += "*\n"
    
    for i in range(len(board)):
        s += str(i%10)
        for j in range(len(board[0])-1):
            s += str(board[i][j]) + "|"
        s += str(board[i][len(board[0])-1]) 
    
        s += "*\n"
    s += (len(board[0])*2 + 1)*"*"
    
    print(s) 

def make_empty_board(sz):
    board = []
    for i in range(sz):
        board.append([" "]*sz)
    return board

def analysis(board):
    for c, full_name in [["b", "Black"], ["w", "White"]]:
        print("%s stones" % (full_name))
        for i in range(2, 6):
            open, semi_open = detect_rows(board, c, i);
            print("Open rows of length %d: %d" % (i, open))
            print("Semi-open rows of length %d: %d" % (i, semi_open))    
    
def play_gomoku(board_size):
    board = make_empty_board(board_size)
    board_height = len(board)
    board_width = len(board[0])
    
    while True:
        print_board(board)
        if is_empty(board):
            move_y = board_height // 2
            move_x = board_width // 2
        else:
            move_y, move_x = search_max(board)
            
        print("Computer move: (%d, %d)" % (move_y, move_x))
        board[move_y][move_x] = "b"
        print_board(board)
        analysis(board)
        
        game_res = is_win(board)
        if game_res in ["White won", "Black won", "Draw"]:
            return game_res
        
        print("Your move:")
        move_y = int(input("y coord: "))
        move_x = int(input("x coord: "))
        board[move_y][move_x] = "w"
        print_board(board)
        analysis(board)
        
        game_res = is_win(board)
        if game_res in ["White won", "Black won", "Draw"]:
            return game_res
          
            
def put_seq_on_board(board, y, x, d_y, d_x, length, col):
    for i in range(length):
        board[y][x] = col        
        y += d_y
        x += d_x

def test_is_empty():
    board  = make_empty_board(8)
    if is_empty(board):
        print("TEST CASE for is_empty PASSED")
    else:
        print("TEST CASE for is_empty FAILED")

def test_is_bounded():
    board = make_empty_board(8)
    x = 5; y = 1; d_x = 0; d_y = 1; length = 3
    put_seq_on_board(board, y, x, d_y, d_x, length, "w")
    print_board(board)
    
    y_end = 3
    x_end = 5

    if is_bounded(board, y_end, x_end, length, d_y, d_x) == 'OPEN':
        print("TEST CASE for is_bounded PASSED")
    else:
        print("TEST CASE for is_bounded FAILED")

def test_detect_row():
    board = make_empty_board(8)
    x = 5; y = 1; d_x = 0; d_y = 1; length = 3
    put_seq_on_board(board, y, x, d_y, d_x, length, "w")
    print_board(board)
    if detect_row(board, "w", 0,x,length,d_y,d_x) == (1,0):
        print("TEST CASE for detect_row PASSED")
    else:
        print("TEST CASE for detect_row FAILED")

def test_detect_rows():
    board = make_empty_board(8)
    x = 5; y = 1; d_x = 0; d_y = 1; length = 3; col = 'w'
    put_seq_on_board(board, y, x, d_y, d_x, length, "w")
    print_board(board)
    if detect_rows(board, col,length) == (1,0):
        print("TEST CASE for detect_rows PASSED")
    else:
        print("TEST CASE for detect_rows FAILED")

def test_search_max():
    board = make_empty_board(8)
    x = 5; y = 0; d_x = 0; d_y = 1; length = 4; col = 'w'
    put_seq_on_board(board, y, x, d_y, d_x, length, col)
    x = 6; y = 0; d_x = 0; d_y = 1; length = 4; col = 'b'
    put_seq_on_board(board, y, x, d_y, d_x, length, col)
    print_board(board)
    if search_max(board) == (4,6):
        print("TEST CASE for search_max PASSED")
    else:
        print("TEST CASE for search_max FAILED")

def easy_testset_for_main_functions():
    test_is_empty()
    test_is_bounded()
    test_detect_row()
    test_detect_rows()
    test_search_max()

def some_tests():
    board = make_empty_board(8)

    board[0][5] = "w"
    board[0][6] = "b"
    y = 5; x = 2; d_x = 0; d_y = 1; length = 3
    put_seq_on_board(board, y, x, d_y, d_x, length, "w")
    print_board(board)
    analysis(board)
    
    # Expected output:
    #       *0|1|2|3|4|5|6|7*
    #       0 | | | | |w|b| *
    #       1 | | | | | | | *
    #       2 | | | | | | | *
    #       3 | | | | | | | *
    #       4 | | | | | | | *
    #       5 | |w| | | | | *
    #       6 | |w| | | | | *
    #       7 | |w| | | | | *
    #       *****************
    #       Black stones:
    #       Open rows of length 2: 0
    #       Semi-open rows of length 2: 0
    #       Open rows of length 3: 0
    #       Semi-open rows of length 3: 0
    #       Open rows of length 4: 0
    #       Semi-open rows of length 4: 0
    #       Open rows of length 5: 0
    #       Semi-open rows of length 5: 0
    #       White stones:
    #       Open rows of length 2: 0
    #       Semi-open rows of length 2: 0
    #       Open rows of length 3: 0
    #       Semi-open rows of length 3: 1
    #       Open rows of length 4: 0
    #       Semi-open rows of length 4: 0
    #       Open rows of length 5: 0
    #       Semi-open rows of length 5: 0
    
    y = 3; x = 5; d_x = -1; d_y = 1; length = 2
    
    put_seq_on_board(board, y, x, d_y, d_x, length, "b")
    print_board(board)
    analysis(board)
    
    # Expected output:
    #        *0|1|2|3|4|5|6|7*
    #        0 | | | | |w|b| *
    #        1 | | | | | | | *
    #        2 | | | | | | | *
    #        3 | | | | |b| | *
    #        4 | | | |b| | | *
    #        5 | |w| | | | | *
    #        6 | |w| | | | | *
    #        7 | |w| | | | | *
    #        *****************
    #
    #         Black stones:
    #         Open rows of length 2: 1
    #         Semi-open rows of length 2: 0
    #         Open rows of length 3: 0
    #         Semi-open rows of length 3: 0
    #         Open rows of length 4: 0
    #         Semi-open rows of length 4: 0
    #         Open rows of length 5: 0
    #         Semi-open rows of length 5: 0
    #         White stones:
    #         Open rows of length 2: 0
    #         Semi-open rows of length 2: 0
    #         Open rows of length 3: 0
    #         Semi-open rows of length 3: 1
    #         Open rows of length 4: 0
    #         Semi-open rows of length 4: 0
    #         Open rows of length 5: 0
    #         Semi-open rows of length 5: 0
    #     
    
    y = 5; x = 3; d_x = -1; d_y = 1; length = 1
    put_seq_on_board(board, y, x, d_y, d_x, length, "b");
    print_board(board);
    analysis(board);
    
    #        Expected output:
    #           *0|1|2|3|4|5|6|7*
    #           0 | | | | |w|b| *
    #           1 | | | | | | | *
    #           2 | | | | | | | *
    #           3 | | | | |b| | *
    #           4 | | | |b| | | *
    #           5 | |w|b| | | | *
    #           6 | |w| | | | | *
    #           7 | |w| | | | | *
    #           *****************
    #        
    #        
    #        Black stones:
    #        Open rows of length 2: 0
    #        Semi-open rows of length 2: 0
    #        Open rows of length 3: 0
    #        Semi-open rows of length 3: 1
    #        Open rows of length 4: 0
    #        Semi-open rows of length 4: 0
    #        Open rows of length 5: 0
    #        Semi-open rows of length 5: 0
    #        White stones:
    #        Open rows of length 2: 0
    #        Semi-open rows of length 2: 0
    #        Open rows of length 3: 0
    #        Semi-open rows of length 3: 1
    #        Open rows of length 4: 0
    #        Semi-open rows of length 4: 0
    #        Open rows of length 5: 0
    #        Semi-open rows of length 5: 0
 
if __name__ == '__main__':
    easy_testset_for_main_functions()
    some_tests()