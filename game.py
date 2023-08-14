
def print_board(board):
    ''' use the loop to print the board '''
    for row in board:
        print(' | '.join(row))
        print('--*--*--')

def player_moves(board, player):
    ''' use the loop to get the player moves 
        and check if the move is valid or not'''
    while True:
        move = int(input("Enter a number from 1 to 9: "))
        if move in range(1, 10):
            row = (move - 1) // 3
            col = (move - 1) % 3
            if board[row][col] == '':
                board[row][col] = player
                break
            else:
                print("Blocked, choose another square.")
        else:
            print("Invalid input, Try again.")

def check_win(board, player):
    ''' chek rows, columns and diagonals'''
    # Check rows
    for row in board:
        if row.count(player) == 3:
            return True

    # Check columns
    if board[0][0] == board[1][0] == board[2][0] == player:
        return True
    if board[0][1] == board[1][1] == board[2][0] == player:
        return True
    if board[0][2] == board[1][2] == board[2][2] == player:
        return True
    
    # Check diagonals
    if board[0][0] == board[1][1] == board[2][2] == player:
        return True
    if board[0][2] == board[1][1] == board[2][0] == player:
        return True

    return False

def check_tie(board):
    for row in board:
        if '' in row:
            return False
    return True

def main_game():
    board = [['', '', ''],
            ['', '', ''],
            ['', '', '']]
    players = ['X','O']
    current_player = 0
    print("Welcome to Tic Tac Toe\n"+"Player 1 is X and Player 2 is O")
    print("The board is numbered from 1 to 9 as shown below:")
    print_board([['1', '2', '3'], ['4', '5', '6'], ['7', '8', '9']])
    print("Start the game!")
    while True:
        print_board(board)
        player = players[current_player]
        print(f"It's {player}'s turn")
        player_moves(board, player)

        if check_win(board, player):
            print_board(board)
            print(f"{player} wins")
            print(f"{players[1-current_player]} Game Over HAHAHAHAHAH")
            while True:
                play_again = input(f"{players[1-current_player]} Play Again?HAHAH (y/n)")
                if play_again == 'y':
                    board = [['', '', ''],
                            ['', '', ''],
                            ['', '', '']]
                    main_game()
                elif play_again == 'n':
                    print("Bye")
                    break
                else:
                    print("Invalid input")

        if check_tie(board):
            print_board(board)
            print("It's a tie")
            break

        current_player = 1 - current_player  # Switch players

main_game()