def is_solved(board):  
    #check rows
    for i in range(0,3):
        if board[i][0] == 1 and board[i][1] == 1 and board[i][2] == 1:
            return 1
        if board[i][0] == 2 and board[i][1] == 2 and board[i][2] == 2:
            return 1
    #check coluns
    for i in range(0,3):
        if board[0][i] == 1 and board[1][i] == 1 and board[2][i] == 1:
            return 1
        if board[0][i] == 2 and board[1][i] == 2 and board[2][i] == 2:
            return 1
    #check draw and not finished 
    for i in board:
        for j in i:
            if(j == 0):
                return -1
    return 0
    
board = [['[1,2,0]', '[0,1,2]', '[0,0,1]']]

# # not yet finished
# board = [[0, 0, 1],
#          [0, 1, 2],
#          [2, 1, 0]]
# print(is_solved(board) == -1)

# # winning row
# board = [[1, 1, 1],
#          [0, 2, 2],
#          [0, 0, 0]]
# print(is_solved(board) == 1)

# # winning column
# board = [[2, 1, 2],
#          [2, 1, 1],
#          [1, 1, 2]]
# print(is_solved(board) == 1)

# # draw
# board = [[2, 1, 2],
#          [2, 1, 1],
#          [1, 2, 1]]
# print(is_solved(board) == 0)