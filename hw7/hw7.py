import random
#==========================================
# Purpose: returns the collatz math theorem on a number
# Input Parameter(s): n, number that gets collatz
# Return Value(s): list of numbers prior to turning 1
#==========================================

def collatz(n):   
    list1 = [n]
    if n == 1:
        return list1
    if n % 2 == 0:
        n /= 2
        int(n)
    elif n % 2 != 0:
        n = n * 3 + 1
    x = int(n)
    if x != 1:
        list1 = list1 + collatz(x)
    if x == 1:
        list1= list1 + [1]
    return list1

#==========================================
# Purpose: Finds the minimum value in a list
# Input Parameter(s): num_list, list of numbers
# Return Value(s): returns the minimum value
#==========================================


def find_min(num_list):   
    if len(num_list) == 1:
        return num_list[0]
    else:
        min_val = find_min(num_list[1:])
        min_val2 = num_list[0]
        if min_val2 > min_val:
            min_val2 = min_val
        return min_val2

#==========================================
# Purpose: determines winner of game
# Input Parameter(s): board, tic tac toe board
# Return Value(s): returns the winner, O X D or -
#==========================================


def winner(board):
    wins = [[0,1,2],[3,4,5],[6,7,8],
            [0,3,6],[1,4,7],[2,5,8],
            [0,4,8],[2,4,6]]
    for win in wins:
        if board[win[0]] == board[win[1]] == board[win[2]] == 'X':
            return 'X'
        if board[win[0]] == board[win[1]] == board[win[2]] == 'O':
            return 'O'
    if '-' in board:
        return '-'
    return 'D'

#==========================================
# Purpose: shows the index of open slots
# Input Parameter(s): board, tic tac toe board
# Return Value(s): returns a list of the index of open slots
#==========================================


def open_slots(board):
    ret = []
    for i in range(len(board)):
        if board[i] == '-':
            ret.append(i)
    return ret

#==========================================
# Purpose: prints the board
# Input Parameter(s): board, tic tac toe board
# Return Value(s): none
#==========================================


def display_board(board):
    for i in range(3):
        print(' '.join(board[3*i:3*i+3]))
    print()

#==========================================
# Purpose: plays a game of tic tac toe with O AI simulated
# Input Parameter(s): none
# Return Value(s): winner of the game, X O or D
#==========================================


def tic_tac_toe():
    board = ['-']*9
    turn = 'X'
    x = 50
    
    while winner(board) == '-':
        slots = open_slots(board) 
        pick = random.choice(slots)
        if turn == 'X':
            board[pick] = 'X'
            turn = 'O'
        elif turn == 'O':
            best_state = 1000
            index = 0
            for slot in slots:
                 board2 = board[:]
                 board2[slot] = 'O'
                 x = force_win(board2)                 
                 if x < best_state:
                     best_state = x
                     index = slot
            board[index] = 'O'
            turn = 'X'
            
                
    return winner(board)

#==========================================
# Purpose: simulates a number of games
# Input Parameter(s): n, number of games to play
# Return Value(s): none
#==========================================


def play_games(n):
    winnars = []
    for i in range(n):
        game = tic_tac_toe()
        winnars.append(game)
    print("X wins:",winnars.count('X'))
    print("O wins:",winnars.count('O'))
    print("Draw:",winnars.count('D'))

#==========================================
# Purpose: forces a win or a draw 
# Input Parameter(s): board, tic tac toe board
# Return Value(s): returns the best state of the board
#==========================================


def force_win(board):
    slots = len(open_slots(board))
    turn = 'X'
    if slots % 2 == 0:
        turn = 'O'
    win = winner(board)
    if win == 'X':
        return 1
    elif win == 'O':
        return -1
    elif win == 'D':
        return 0    

    if turn == 'X':
        best_state = -1
        for slot in open_slots(board):
            board2 = board[:]
            board2[slot] = 'X'
            cur_state = force_win(board2)
            if cur_state > best_state:
                best_state = cur_state
        return best_state
                       
    if turn == 'O':
        best_state = 1
        for slot in open_slots(board):
            board2 = board[:]
            board2[slot] = 'O'
            cur_state = force_win(board2)
            if cur_state < best_state:
                best_state = cur_state
        return best_state
        



