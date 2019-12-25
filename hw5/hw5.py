import random 

#==========================================
# Purpose: returns a list of every name that appears in each list
# Input Parameter(s): grades, life, sleep are all lists of names
# Return Value(s): a list of each name that appears in all 3 parameter lists 
#==========================================


def wizards(grades, life, sleep):
    list = []
    for x in range(len(grades)):
        if life.count(grades[x]) == 1:
            if sleep.count(grades[x]) == 1:
                list.append(grades[x])
    return list

#==========================================
# Purpose: returns a list with the indexes of open spots on board
# Input Parameter(s): takes in a list that is filled with xs and os and -s
# Return Value(s): a list of indexes of open spots
#==========================================

 
def open_slots(board):
    list = [] 
    for x in range(len(board)):
        if board[x] == '-':
            list.append(x)
    return list

#==========================================
# Purpose: checks to see if there is a winner
# Input Parameter(s): board - tic tac toe board filled with xs and os and -s
# Return Value(s): the winner X or O or D or -
#==========================================



def winner(board):
    if board[0] == 'X' and board[1] == 'X' and board[2] == 'X':
        return 'X'
    elif board[3] == 'X' and board[4] == 'X' and board[5] == 'X':
        return 'X'
    elif board[6] == 'X' and board[7] == 'X' and board[8] == 'X':
        return 'X'
    elif board[0] == 'X' and board[3] == 'X' and board[6] == 'X':
        return 'X'
    elif board[1] == 'X' and board[4] == 'X' and board[7] == 'X':
        return 'X'
    elif board[2] == 'X' and board[5] == 'X' and board[8] == 'X':
        return 'X'
    elif board[0] == 'X' and board[4] == 'X' and board[8] == 'X':
        return 'X'
    elif board[2] == 'X' and board[4] == 'X' and board[6] == 'X':
        return 'X'

    elif board[0] == 'O' and board[1] == 'O' and board[2] == 'O':
        return 'O'
    elif board[3] == 'O' and board[4] == 'O' and board[5] == 'O':
        return 'O'
    elif board[6] == 'O' and board[7] == 'O' and board[8] == 'O':
        return 'O'
    elif board[0] == 'O' and board[3] == 'O' and board[6] == 'O':
        return 'O'
    elif board[1] == 'O' and board[4] == 'O' and board[7] == 'O':
        return 'O'
    elif board[2] == 'O' and board[5] == 'O' and board[8] == 'O':
        return 'O'
    elif board[0] == 'O' and board[4] == 'O' and board[8] == 'O':
        return 'O'
    elif board[2] == 'O' and board[4] == 'O' and board[6] == 'O':
        return 'O'

    i = 0
    for x in range(0,9):
        if board[x] == '-':
            return '-'
        i += 1

    if i == 9:
        return 'D'

#==========================================
# Purpose: plays a random game of tic tac toe 
# Input Parameter(s): none
# Return Value(s): returns the winner of the game of tic tac toe
#==========================================


def tic_tac_toe():
    board = ['-','-','-','-','-','-','-','-','-']
    x = 0
    y = 0
    i = 0
    while winner(board) == '-':
        x = random.choice(open_slots(board))
        board[x] = 'X'
        if i < 4:
            y = random.choice(open_slots(board))
            board[y] = 'O'
        i += 1
    
    return winner(board)

#==========================================
# Purpose: simulates the winner and loser of the game over a period of games
# Input Parameter(s): n, the amount of games you want to simulate
# Return Value(s): nothing gets returned
#==========================================


def play_games(n):
    x = 0
    o = 0
    d = 0
    
    for n in range(1, n + 1):
        z = tic_tac_toe()
        if z == 'X':
            x += 1
        elif z == 'O':
            o += 1
        else:
            d += 1
    print("X wins: ", x)
    print("O wins: ", o)
    print("Draws: ", d)
            
    
        
