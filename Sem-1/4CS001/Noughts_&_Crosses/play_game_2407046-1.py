# Name = Kamal Dhital
# University ID = 2407046


# Importing another file which contain function
from noughtsandcrosses_2407046 import *


def main():
    """ #! This is the main function for this game.

        #* This function initializes the game board, displays a welcome message, and allows the player to choose from various options.

        The player can choose to play a game, save their score, view the leaderboard, or quit the game.

        The function returns when the player chooses to quit the game.

        #! Parameters:
            None

        #! Returns:
            None
    """
    # Initializing the game board
    board = [['1', '2', '3'],
             ['4', '5', '6'],
             ['7', '8', '9']]
    # Welcome the player to the game using welcome function
    welcome(board)
    # Initializing the total score to 0
    total_score = 0
    # Starting the Main game loop
    while True:
        # Calling menu function to display the menu to the player and store the user choice to the identifier
        choice = menu()
        # This if statement runs if the user chooses to play a game
        #! Play Game
        if choice == '1':
            # Play the game and get the score
            score = play_game(board)
            # Add the score to the total score
            total_score += score
            # Display the current total score to the user
            print('Your current score is:', total_score)

        # This if statement runs if the user chooses to save their score
        #! Save the score
        if choice == '2':
            # Save the score
            save_score(total_score)
            # Using the above save_score without returning the reset value for total_score gives the wrong result if different player play the game in single start
            # total_score = save_score(total_score) and returning the value 0 from save_score function is the better way to manage different player in a single start

        # This if statement runs if the user chooses to view the leaderboard
        #! Display Leaderboard
        if choice == '3':
            # Load the scores from the leaderboard
            leader_board = load_scores()
            # Display the leaderboard
            display_leaderboard(leader_board)

        # This if statement runs if user want to quit the game
        #! Quit the Game
        if choice == 'q':
            print('Thank you for playing the "Unbeatable Noughts and Crosses" game.')
            print('Good bye')
            # Exiting the game loop
            return


# Program execution begins here
#! Magic Module to stop the program to run automatically when this program is imported to another program

if __name__ == '__main__':
    #! Calling the function to start the game
    main()
