# Function to print the board
def print_board(board):
    print(board[0], "|", board[1], "|", board[2])
    print("--+---+--")
    print(board[3], "|", board[4], "|", board[5])
    print("--+---+--")
    print(board[6], "|", board[7], "|", board[8])

# Main game function
def play_game():
    board = [' '] * 9  # Create an empty board with 9 spaces
    current_player = 'X'

    for turn in range(9):  # There are 9 turns at most (3x3 board)
        print_board(board)
        move = int(input(f"Player {current_player}, choose a spot (0-8): "))
        
        # Place the player's symbol on the chosen spot
        board[move] = current_player

        # Switch players
        current_player = 'O' if current_player == 'X' else 'X'

    print_board(board)  # Print final board after the game ends
    print("Game Over!")


play_game()
