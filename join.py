board = []
for n in range(0,5):    
    board.append(["O"]*5)

def print_board(board):
    for n in board:
        print " ".join(n)
        
        
print_board(board)
