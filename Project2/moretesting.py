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

def put_seq_on_board(board, y, x, d_y, d_x, length, col):
    for i in range(length):
        board[y][x] = col        
        y += d_y
        x += d_x

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

# def detect_rows(board, col, length):
#     open_seq_count, semi_open_seq_count = 0, 0
#     detected = (0, 0)

#     for size in range(len(board)):
#         detected = detect_row(board, col, size, 0, length, 0, 1) # at each row check all the columns (0, 1)
#         open_seq_count += detected[0]
#         semi_open_seq_count += detected[1]

#         detected = detect_row(board, col, 0, size, length, 1, 0) # at each column check all the rows (1, 0)
#         open_seq_count += detected[0]
#         semi_open_seq_count += detected[1]

#         if size >= length: 
#             detected = detect_row(board, col, (len(board) - size), 0, length, 1, 1) # (1, 1)
#             open_seq_count += detected[0]
#             semi_open_seq_count += detected[1]

#             detected = detect_row(board, col, 0, (size - 1), length, 1, -1) # (1, -1)
#             open_seq_count += detected[0]
#             semi_open_seq_count += detected[1]

#             if (len(board) - size) > 0: #should not overlap in the "corner" with code outside
#                 detected = detect_row(board, col, 0, (len(board) - size), length, 1, 1) # (1, 1)
#                 open_seq_count += detected[0]
#                 semi_open_seq_count += detected[1]

#             if (size - 1) < (len(board) - 1):  #should not overlap in the "corner" with code outside
#                 detected = detect_row(board, col, (size - 1), (len(board) - 1), length, 1, -1) # (1, -1)
#                 open_seq_count += detected[0]
#                 semi_open_seq_count += detected[1]

#     return open_seq_count, semi_open_seq_count

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

    # put_seq_on_board(board, 5, 1, 1, 1, 3, "b")
    # put_seq_on_board(board, 4, 1, 1, 1, 3, "b")
    # put_seq_on_board(board, 3, 1, 1, 1, 3, "b")
    # put_seq_on_board(board, 2, 1, 1, 1, 3, "b")
    # put_seq_on_board(board, 1, 1, 1, 1, 3, "b")
    # put_seq_on_board(board, 1, 2, 1, 1, 3, "b")
    # put_seq_on_board(board, 1, 3, 1, 1, 3, "b")
    # put_seq_on_board(board, 1, 4, 1, 1, 3, "b")
    # put_seq_on_board(board, 1, 5, 1, 1, 3, "b")

    # put_seq_on_board(board, 5, 0, 1, 1, 3, "b")
    # put_seq_on_board(board, 4, 0, 1, 1, 3, "b")
    # put_seq_on_board(board, 3, 0, 1, 1, 3, "b")
    # put_seq_on_board(board, 2, 0, 1, 1, 3, "b")
    # put_seq_on_board(board, 1, 0, 1, 1, 3, "b")
    # put_seq_on_board(board, 0, 0, 1, 1, 3, "b")
    # put_seq_on_board(board, 0, 1, 1, 1, 3, "b")
    # put_seq_on_board(board, 0, 2, 1, 1, 3, "b")
    # put_seq_on_board(board, 0, 3, 1, 1, 3, "b")
    # put_seq_on_board(board, 0, 4, 1, 1, 3, "b")
    # put_seq_on_board(board, 0, 5, 1, 1, 3, "b")

    put_seq_on_board(board, 1, 1, 0, 1, 3, "b")
    put_seq_on_board(board, 2, 1, 0, 1, 3, "b")
    put_seq_on_board(board, 3, 1, 0, 1, 3, "b")

    print_board(board)

    # print(detect_row(board, "b", 1, 1, 3, 1, 0))
    print(detect_rows(board, 'b', 3))