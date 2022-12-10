board = [[],[],[],[]]
def create_board():
    for i in board:
        if board[i] == 0 or 1 or 2:
            board[i].append([],[],[])
        else:
            board[i].append([])

create_board()
print(board)