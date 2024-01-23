# ----- Global Variables -----
# https://www.youtube.com/watch?v=BHh654_7Cmw
#Game board
board = ["-","-","-",
         "-","-","-",
         "-","-","-",]

#if game is still going
game_still_going = True

# Who won or tie
winner = None

# Who's turn is it
current_player = "X"

def boardDisplay():
    print(board[0] + ' | ' + board[1] + ' | ' + board[2])
    print(board[3] + ' | ' + board[4] + ' | ' + board[5])
    print(board[6] + ' | ' + board[7] + ' | ' + board[8])

def turn_Handle():
    position = input("Choose a position from 1-9: ")
    position = int(position) - 1

    board[position] = 'X'
    boardDisplay()

def check_if_game_over():
    check_if_win()
    check_if_tie()

def check_if_win():
    # checkrows
    # checkcolumns
    # check diagonals
    return

def check_if_tie():
    return

# Switch players
def flip_player():
    return

# Game Runtime
def play_game():

    # Display initial board
    boardDisplay()

    while game_still_going:

        turn_Handle(current_player)

        check_if_game_over()

        flip_player()

    # The game has ended
    if winner == 'X' or winner == 'O':
        print(winner + ' won.')
    elif winner == None:
        print('Tie.')

    turn_Handle()

play_game()
