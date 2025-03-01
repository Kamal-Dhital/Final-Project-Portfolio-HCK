# Name = Kamal Dhital
# University ID = 2407046


# Importing random, os.path and json module
import random
import os.path
import json

# Setting the value of random in default
random.seed()

# Viewing the content inside the import module
# print(dir(random))
# print(dir(os.path))
# print(dir(json))


def draw_board(board):
    # develop code to draw the board
    # Using for loop to draw the board
    """
    #! Draws the game board.

    Parameters:
    board (list): The game board represented as a list of lists.

    Returns:
    None

    """
    for draw in board:
        print(" " + "-" * 11 + " ")
        print("| " + " | ".join(draw) + " |")
    # Printing this outside the loop just to execute at the end
    print(" " + "-" * 11 + " ")


def welcome(board):
    # prints the welcome message
    """
    #! Prints the welcome message and displays the game board.

    Parameters:
    board (list): The game board represented as a list of lists.

    Returns:
    None
    """
    print('Welcome to the "Unbeatable Noughts and Crosses" game.')
    print('The board layout is shown below:')
    # display the board by calling draw_board(board)
    draw_board(board)
    print("When prompted, enter the number corresponding to the square you want.")


def initialise_board(board):
    # develop code to set all elements of the board to one space ' '
    """
    #! Initializes the game board.

    Parameters:
    board (list): The game board represented as a 2D list.

    Returns:
    list: The initialized game board.

    """
    board.clear()
    for i in range(3):
        board.append([" "]*3)
    return board


def get_player_move(board):
    # develop code to ask the user for the cell to put the X in,
    # and return row and col
    """
    Ask the user for the cell to put the X in and return the row and column.

    Parameters:
    - board (list): The game board.

    Returns:
    - tuple: The row and column of the chosen cell.

    Raises:
    - ValueError: If the user input is not a valid integer.
    - Exception: If there is an error in the function.

    """
    print("Player's Move")
    try:
        #! Asking for user Input
        display = """\t\t    1 2 3\n\t\t    4 5 6\n"""
        position = int(input(f'{display}Choose your square: 7 8 9 : ')) - 1

        # * // provide quotient and % provide remainder
        row = position // 3
        col = position % 3
        if 0 <= row <= 2 and 0 <= col <= 2 and board[row][col] == ' ':
            return row, col
        else:
            print("Invalid move. Try Again!")
            return get_player_move(board)
    except ValueError as err_mesg:
        print("Error in Player input", err_mesg)
        return get_player_move(board)
    except Exception as err_mesg:
        print("Error in get_player_move", err_mesg)
        return get_player_move(board)


def choose_computer_move(board):
    # develop code to let the computer chose a cell to put a nought in
    # and return row and col
    """
    Choose a computer move for the Tic-Tac-Toe game.

    This function randomly selects an empty cell on the board and returns the row and column indices of that cell.

    Parameters:
    board (list of lists): The current state of the Tic-Tac-Toe board.

    Returns:
    tuple: A tuple containing the row and column indices of the selected cell.

    """
    print("Computer's Move")
    while True:
        #! Asking for Computer Input
        position = random.randint(1, 9)
        row = (position - 1) // 3
        col = (position - 1) % 3
        if 0 <= row <= 2 and 0 <= col <= 2 and board[row][col] == ' ':
            return row, col


def check_for_win(board, mark):
    # develop code to check if either the player or the computer has won
    # return True if someone won, False otherwise
    """
    #! Check if either the player or the computer has won the game.

    Parameters:
    - board (list of lists): The game board.
    - mark (str): The mark ('X' or 'O') to check for.

    Returns:
    - bool: True if the specified mark has won, False otherwise.
    """
    for row in range(3):
        if all([cell == mark for cell in board[row]]):
            return True

    for col in range(3):
        if all([board[row][col] == mark for row in range(3)]):
            return True

    if board[0][0] == board[1][1] == board[2][2] == mark:
        return True
    if board[0][2] == board[1][1] == board[2][0] == mark:
        return True
    return False


def check_for_draw(board):
    # develop cope to check if all cells are occupied
    # return True if it is, False otherwise
    """
    #! Check if the game board is in a draw state.

    Parameters:
    board (list): The game board represented as a list of lists.

    Returns:
    bool: True if all cells are occupied, False otherwise.
    """
    for row in board:
        if " " in row:
            return False
    return True


def play_game(board):
    """
    #! Function to play the game

    Parameters:
    - board (list): The game board represented as a 2D list.

    Returns:
    - int: The score of the game. 1 if the player wins, 0 if there is a draw, -1 if the computer wins.

    """
    # develop code to play the game
    # star with a call to the initialise_board(board) function to set
    # the board cells to all single spaces ' '
    initialise_board(board)
    # then draw the board
    draw_board(board)
    # then in a loop, get the player move, update and draw the board
    while True:
        row, col = get_player_move(board)
        board[row][col] = 'X'
        draw_board(board)
    # check if the player has won by calling check_for_win(board, mark),
    # if so, return 1 for the score
        if check_for_win(board, 'X'):
            print("Congratulation, Player Wins the Game.")
            return 1
    # if not check for a draw by calling check_for_draw(board)
    # if drawn, return 0 for the score
        elif check_for_draw(board):
            print("Game is draw")
            return 0
    # if not, then call choose_computer_move(board)
    # to choose a move for the computer
    # update and draw the board
        row, col = choose_computer_move(board)
        board[row][col] = 'O'
        draw_board(board)
    # check if the computer has won by calling check_for_win(board, mark),
    # if so, return -1 for the score
        if check_for_win(board, 'O'):
            print("Be Careful, AI want to dominate us and start by this win.")
            return -1
    # if not check for a draw by calling check_for_draw(board)
        elif check_for_draw(board):
            # if drawn, return 0 for the score
            print("Game is draw")
            return 0
    # repeat the loop


def menu():
    """
    #! Function to displays a menu and prompts the user to choose a valid option.

    The function continuously loops until a valid option is chosen. Once a valid option is chosen, it is returned as a string.

    Parameters:
    None

    Returns:
    - choice (str): The chosen option as a string ('1', '2', '3', or 'q')

    """
    while True:
        print("Enter one of the following options:")
    # 1 - Play the game
        print("\t1 - Play the game")
    # 2 - Save score in file 'leaderboard.txt'
        print("\t2 - Save your score in the leaderboard")
    # 3 - Load and display the scores from the 'leaderboard.txt'
        print("\t3 - Load and display the leaderboard")
    # q - End the program
        print("\tq - End the program")
    # get user input of either '1', '2', '3' or 'q'
        choice = input("1,2,3 or q? ")
        if (choice in ("1", "2", "3", "q")):
            return choice
        else:
            print("Invalid choice. Try agaiin.")


def load_scores():
    # develop code to load the leaderboard scores
    # from the file 'leaderboard.txt'
    # return the scores in a Python dictionary
    # with the player names as key and the scores as values
    # return the dictionary in leaders
    """
    #! Load the leaderboard scores from the file 'leaderboard.txt' and return them as a Python dictionary.

    Returns:
        dict: A dictionary with player names as keys and scores as values. If the file does not exist or cannot be decoded, an empty dictionary is returned.
    """
    try:
        if os.path.isfile('leaderboard.txt'):
            with open('leaderboard.txt', 'r') as file:
                leaders = json.load(file)
                return leaders
        else:
            leaders = {}
    except json.decoder.JSONDecodeError:
        print("Error decoding JSON. Returning empty dictionary")
        leaders = {}
    except FileNotFoundError:
        print("File not found. Returning empty dictionary.")
        leaders = {}
    return leaders


def save_score(score):
    # develop code to ask the player for their name
    # and then save the current score to the file 'leaderboard.txt'
    """
    #! Save the current score to the leaderboard file.

    This function prompts the player for their name and saves the current score to the file 'leaderboard.txt'. If the player's name already exists in the leaderboard, the score is added to the existing score. If the player's name does not exist, a new entry is created with the player's name and score.

    Parameters:
        score (int): The current score to be saved.

    Returns:
        None

    Raises:
        Any exception that occurs while saving the data into the file.
    """
    try:
        name = input("Enter your name:")
        leaderboard = load_scores()
        if name in leaderboard:
            leaderboard[name] += score
        else:
            leaderboard[name] = score

        with open('leaderboard.txt', 'w') as file:
            json.dump(leaderboard, file)
        print("Score Saved")
        return
    except Exception as err_mesg:
        print("Error while saving the data into file", err_mesg)


def display_leaderboard(leaders):
    # develop code to display the leaderboard scores
    # passed in the Python dictionary parameter leader
    """
    #! Display the leaderboard scores.

    Parameters:
        leaders (dict): A dictionary containing the names and scores of the leaderboard.

    Returns:
        None
    """
    print("Leaderboard:")
    if (leaders):
        for name, score in leaders.items():
            print(f"{name}: {score}")
    else:
        print("No Score Available")
