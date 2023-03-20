def print_board(board_num_1, board_num_2, board_num_3, board_num_4, board_num_5, board_num_6, board_num_7, board_num_8, board_num_9):
    print(" ")
    print("   |   |     |     |   |     |     |   |   ")
    print(" {} | {} | {}   |   {} | {} | {}   |   {} | {} | {}   ".format(board_num_1[0], board_num_1[1], board_num_1[2], board_num_2[0], board_num_2[1], board_num_2[2], board_num_3[0], board_num_3[1], board_num_3[2]))
    print("___|___|___  |  ___|___|___  |  ___|___|___")
    print("   |   |     |     |   |     |     |   |   ")
    print(" {} | {} | {}   |   {} | {} | {}   |   {} | {} | {}   ".format(board_num_1[3], board_num_1[4], board_num_1[5], board_num_2[3], board_num_2[4], board_num_3[5], board_num_3[3], board_num_3[4], board_num_3[5]))
    print("___|___|___  |  ___|___|___  |  ___|___|___")
    print("   |   |     |     |   |     |     |   |   ")
    print(" {} | {} | {}   |   {} | {} | {}   |   {} | {} | {}   ".format(board_num_1[6], board_num_1[7], board_num_1[8], board_num_2[6], board_num_2[7], board_num_3[8], board_num_3[6], board_num_3[7], board_num_3[8]))
    print("   |   |     |     |   |     |     |   |   ")
    print("   |   |     |     |   |     |     |   |   ")
    print(" {} | {} | {}   |   {} | {} | {}   |   {} | {} | {}   ".format(board_num_4[0], board_num_4[1], board_num_4[2], board_num_5[0], board_num_5[1], board_num_5[2], board_num_6[0], board_num_6[1], board_num_6[2]))
    print("___|___|___  |  ___|___|___  |  ___|___|___")
    print("   |   |     |     |   |     |     |   |   ")
    print(" {} | {} | {}   |   {} | {} | {}   |   {} | {} | {}   ".format(board_num_4[3], board_num_4[4], board_num_4[5], board_num_5[3], board_num_5[4], board_num_5[5], board_num_6[3], board_num_6[4], board_num_6[5]))
    print("___|___|___  |  ___|___|___  |  ___|___|___")
    print("   |   |     |     |   |     |     |   |   ")
    print(" {} | {} | {}   |   {} | {} | {}   |   {} | {} | {}   ".format(board_num_4[6], board_num_4[7], board_num_4[8], board_num_5[6], board_num_5[7], board_num_5[8], board_num_6[6], board_num_6[7], board_num_6[8]))
    print("   |   |     |     |   |     |     |   |   ")
    print("   |   |     |     |   |     |     |   |   ")
    print(" {} | {} | {}   |   {} | {} | {}   |   {} | {} | {}   ".format(board_num_7[0], board_num_7[1], board_num_7[2], board_num_8[0], board_num_8[1], board_num_8[2], board_num_9[0], board_num_9[1], board_num_9[2]))
    print("___|___|___  |  ___|___|___  |  ___|___|___")
    print("   |   |     |     |   |     |     |   |   ")
    print(" {} | {} | {}   |   {} | {} | {}   |   {} | {} | {}   ".format(board_num_7[3], board_num_7[4], board_num_7[5], board_num_8[3], board_num_8[4], board_num_8[5], board_num_9[3], board_num_9[4], board_num_9[5]))
    print("___|___|___  |  ___|___|___  |  ___|___|___")
    print("   |   |     |     |   |     |     |   |   ")
    print(" {} | {} | {}   |   {} | {} | {}   |   {} | {} | {}   ".format(board_num_7[6], board_num_7[7], board_num_7[8], board_num_8[6], board_num_8[7], board_num_8[8], board_num_9[6], board_num_9[7], board_num_9[8]))
    print("   |   |     |     |   |     |     |   |   ")
    print(" ")

def get_move(player, big_board, board_num_1, board_num_2, board_num_3, board_num_4, board_num_5, board_num_6, board_num_7, board_num_8, board_num_9):
    while True:
        board_choice = input("Player {}, enter a number between 1 and 9 to select a board: ".format(player))
        board_list = (board_num_1, board_num_2, board_num_3, board_num_4, board_num_5, board_num_6, board_num_7, board_num_8, board_num_9)
        try:
            board_choice = int(board_choice) - 1
        except ValueError:
            print("Invalid input, please enter a number.")
            continue
        if board_choice < 0 or board_choice > 8:
            print("Invalid input, please enter a number between 1 and 9.")
            continue
        else:
            play_board((board_list[board_choice]), player, board_choice, big_board)
            return

def play_board(board, player, board_choice, big_board):
    while True:
        global pos_choice
        print("Your board is board {}".format((board_choice + 1)))
        pos_choice = input("Player {}, enter a number between 1 and 9 to make a move: ".format(player))
        try:
            pos_choice = int(pos_choice) - 1
        except ValueError:
            print("Invalid input, please enter a number.")
            continue
        if pos_choice < 0 or pos_choice > 8:
            print("Invalid input, please enter a number between 1 and 9.")
            continue
        if board[pos_choice] != ' ':
            print("That space is already taken.")
        else:
            board[pos_choice] = player
        if check_win(board):
            big_board[board_choice] = player
            print("╔═════════════════════════════╗")
            print("║   Player {} wins board {}!    ║".format(player, board_choice))
            print("╚═════════════════════════════╝")
        if ' ' not in board:
            print("╔═════════════════════════════╗")
            print("║   Tie game in board {}!        ║".format(board_choice))
            print("╚═════════════════════════════╝")
        return pos_choice
    
def check_win(board):
    # Check rows
    for i in range(0, 9, 3):
        if board[i] == board[i+1] == board[i+2] != ' ':
            return True
    # Check columns
    for i in range(3):
        if board[i] == board[i+3] == board[i+6] != ' ':
            return True
    # Check diagonals
    if board[0] == board[4] == board[8] != ' ':
        return True
    if board[2] == board[4] == board[6] != ' ':
        return True
    return False

def initiate():
    for i in range(2):
            print(" ")
    print("╔═══════════════════════════════════════════════════════════════════════════════════════════════════╗")
    print("║ TTTTTTTTT  IIIIIIII  CCCCCC     TTTTTTTTT    AAAA       CCCCCC     TTTTTTTTT  OOOOOOOO   EEEEEEEE ║")
    print("║    TTT       III    CC             TTT      AA  AA    CC              TTT    OO      OO  EE       ║")
    print("║    TTT       III    CC      ==     TTT     AAAAAAAA  CC        ==     TTT    OO      OO  EEEEE    ║")
    print("║    TTT       III    CC             TTT    AA      AA  CC              TTT    OO      OO  EE       ║")
    print("║    TTT     IIIIIIII  CCCCCC        TTT   AA        AA   CCCCCC        TTT     OOOOOOOO   EEEEEEEE ║")
    print("║                                          -Cody Skinner                                            ║")
    print("╚═══════════════════════════════════════════════════════════════════════════════════════════════════╝")

    for i in range(2):
            print(" ")
    print("╔══════════════════════════════════════════════════════════════════════╗")
    print("║   Welcome to Tic-Tac-Toe^2, the game where players play Tic-Tac-Toe  ║")
    print("║    on 9 smaller boards to win positions on a single large board.     ║")
    print("╚══════════════════════════════════════════════════════════════════════╝")
    for i in range(2):
            print(" ")
    print("This is how each board is arranged:")
    print(" ")
    print("   |   |")
    print(" 1 | 2 | 3")
    print("___|___|___")
    print("   |   |")
    print(" 4 | 5 | 6")
    print("___|___|___")
    print("   |   |")
    print(" 7 | 8 | 9")
    print("   |   |")
    for i in range(2):
            print(" ")
    while True:
        if input("Type Y to play: ") == "Y":
            play_game()
            return
        else:
            continue

def play_game():
    big_board, board_num_1, board_num_2, board_num_3, board_num_4, board_num_5, board_num_6, board_num_7, board_num_8, board_num_9 = ([' '] * 9), ([' '] * 9), ([' '] * 9), ([' '] * 9), ([' '] * 9), ([' '] * 9), ([' '] * 9), ([' '] * 9), ([' '] * 9), ([' '] * 9)
    player = 'O'
    print_board(board_num_1, board_num_2, board_num_3, board_num_4, board_num_5, board_num_6, board_num_7, board_num_8, board_num_9)
    get_move('X', big_board, board_num_1, board_num_2, board_num_3, board_num_4, board_num_5, board_num_6, board_num_7, board_num_8, board_num_9)
    while True:
        for i in range(3):
            print(" ")
        print_board(board_num_1, board_num_2, board_num_3, board_num_4, board_num_5, board_num_6, board_num_7, board_num_8, board_num_9)
        board_list = (board_num_1, board_num_2, board_num_3, board_num_4, board_num_5, board_num_6, board_num_7, board_num_8, board_num_9)
        if big_board[pos_choice] == ' ':
            play_board((board_list[pos_choice]), player, pos_choice, big_board)
        else:
            get_move(player, big_board, board_num_1, board_num_2, board_num_3, board_num_4, board_num_5, board_num_6, board_num_7, board_num_8, board_num_9)  
        if check_win(big_board):
            print("╔═════════════════════════════╗")
            print("║  Player {} wins the game!    ║".format(player,))
            print("╚═════════════════════════════╝")
            return
        player = 'O' if player == 'X' else 'X'

initiate()
