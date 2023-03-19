#big_board
#board_num_1 1 through 9 is small board


def print_board(board):
    print("   |   |")
    print(" {} | {} | {}".format(board[0], board[1], board[2]))
    print("___|___|___")
    print("   |   |")
    print(" {} | {} | {}".format(board[3], board[4], board[5]))
    print("___|___|___")
    print("   |   |")
    print(" {} | {} | {}".format(board[6], board[7], board[8]))
    print("   |   |")

def get_move(player, big_board, board_num_1, board_num_2, board_num_3, board_num_4, board_num_5, board_num_6, board_num_7, board_num_8, board_num_9):
    while True:
        board_select = input("Player {}, would you like to inspect a board?(Y or N): ".format(player))
        if board_select == "Y":
            board_choice = input("Player {}, enter a number between 1 and 9 to inspect a board: ".format(player))
            try:
                board_choice = int(board_choice) - 1
            except ValueError:
                print("Invalid input, please enter a number.")
                continue
            if board_choice < 0 or board_choice > 8:
                print("Invalid selection, please enter a number between 1 and 9.")
                continue
            elif board_choice == 0:
                print("Now inspecting board 1")
                print_board(board_num_1)
            elif board_choice == 1:
                print("Now inspecting board 2")
                print_board(board_num_2)
            elif board_choice == 2:
                print("Now inspecting board 3")
                print_board(board_num_3)
            elif board_choice == 3:
                print("Now inspecting board 4")
                print_board(board_num_4)
            elif board_choice == 4:
                print("Now inspecting board 5")
                print_board(board_num_5)
            elif board_choice == 5:
                print("Now inspecting board 6")
                print_board(board_num_6)
            elif board_choice == 6:
                print("Now inspecting board 7")
                print_board(board_num_7)
            elif board_choice == 7:
                print("Now inspecting board 7")
                print_board(board_num_8)
            elif board_choice == 8:
                print("Now inspecting board 9")
                print_board(board_num_9)
            continue
        elif board_select == "N":
            board_choice = input("Player {}, enter a number between 1 and 9 to select your game: ".format(player))
            try:
                board_choice = int(board_choice) - 1
            except ValueError:
                print("Invalid input, please enter a number.")
                continue
            if board_choice < 0 or board_choice > 8:
                print("Invalid move, please enter a number between 1 and 9.")
                pass
            elif board_choice == 0:
                play_board(board_num_1, player, board_choice, big_board)
                return
            elif board_choice == 1:
                play_board(board_num_2, player, board_choice, big_board)
                return
            elif board_choice == 2:
                play_board(board_num_3, player, board_choice, big_board)
                return
            elif board_choice == 3:
                play_board(board_num_4, player, board_choice, big_board)
                return
            elif board_choice == 4:
                play_board(board_num_5, player, board_choice, big_board)
                return
            elif board_choice == 5:
                play_board(board_num_6, player, board_choice, big_board)
                return
            elif board_choice == 6:
                play_board(board_num_7, player, board_choice, big_board)
                return
            elif board_choice == 7:
                play_board(board_num_8, player, board_choice, big_board)
                return
            elif board_choice == 8:
                play_board(board_num_9, player, board_choice, big_board)
                return
        else:
            continue


    
def play_board(board, player, board_choice, big_board):
        pos_choice = input("Player {}, enter a number between 1 and 9 to make a move: ".format(player))
        try:
            pos_choice = int(pos_choice) - 1
        except ValueError:
            print("Invalid input, please enter a number.")
        if pos_choice < 0 or pos_choice > 8:
            print("Invalid selection, please enter a number between 1 and 9.")
        if board[pos_choice] != ' ':
            print("That space is already taken.")
        board[pos_choice] = player
        if check_win(board):
            big_board[board_choice] = player
            print_board(board)
            print("Player {} wins board {}!".format(player, board_choice))
        if ' ' not in board:
            print_board(board)
            print("Tie game in board {}!".format(board_choice))
    

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

def introduction():
    for i in range(2):
            print(" ")
    print("TTTTTTTTT  IIIIIIII  CCCCCC       TTTTTTTTT    AAAA       CCCCCC       TTTTTTTTT  OOOOOOOO   EEEEEEEE")
    print("   TTT       III    CC               TTT      AA  AA    CC                TTT    OO      OO  EE      ")
    print("   TTT       III    CC        ==     TTT     AAAAAAAA  CC          ==     TTT    OO      OO  EEEEE   ")
    print("   TTT       III    CC               TTT    AA      AA  CC                TTT    OO      OO  EE      ")
    print("   TTT     IIIIIIII  CCCCCC          TTT   AA        AA   CCCCCC          TTT     OOOOOOOO   EEEEEEEE")
    print("                                                                                      -Cody Skinner  ")
    for i in range(2):
            print(" ")
    print("Welcome to Tic-Tac-Toe^2, the game where players play Tic-Tac-Toe on 9 smaller boards to win positions on a single large board.")
    for i in range(2):
            print(" ")
    print("This is how the board is arranged:")
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
    big_board = [' '] * 9
    board_num_1 = [' '] * 9
    board_num_2 = [' '] * 9
    board_num_3 = [' '] * 9
    board_num_4 = [' '] * 9
    board_num_5 = [' '] * 9
    board_num_6 = [' '] * 9
    board_num_7 = [' '] * 9
    board_num_8 = [' '] * 9
    board_num_9 = [' '] * 9
    player = 'X'
    while True:
        print_board(big_board)
        get_move(player, big_board, board_num_1, board_num_2, board_num_3, board_num_4, board_num_5, board_num_6, board_num_7, board_num_8, board_num_9)
        if check_win(big_board):
            print("Player {} wins the game!".format(player))
            return
        player = 'O' if player == 'X' else 'X'
        for i in range(3):
            print(" ")


introduction()