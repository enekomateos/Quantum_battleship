
# Main code for the game

# Import block

import numpy as np
from board import Board
import os

# Functions

def introduction():

    """
    Print the introduction of the game.
    """

        # Welcome message
    print("Welcome to the Battleship game!")
    print("But, what would happen if the ships were really small and governed by the laws of quantum mechanics?")
    print("It is not the common Battleship game, it is a quantum version of it!")
    print("Let's play!")
    os.system('cls' if os.name == 'nt' else "printf '\033c'")

    tutorial = input("Do you need a tutorial? (y/n)")
    if tutorial == "y":
        print("The game is played in turns. In each turn you will have to choose a position to shoot in the board of the other player.")
        print("The game ends when all the ships of one of the players are destroyed.")
        print("In the beggining the ships are placed in the board. You will have to guess where the opponent's ships are.")
        print("The ships are governed by the laws of quantum mechanics. They can be in superposition, so they can be in two places at the same time.")
        print("When you shoot a ship in a superposition, the ship will collapse to one of the positions, and you will know if you hit the ship or not.")
        print("The game is over when all the ships of one of the players are destroyed.")
        print("Good luck!")
        input("Press enter to continue")

    os.system('cls' if os.name == 'nt' else "printf '\033c'")

def select_game_mode():

    """
    Select the game mode.
    """

    print("This game is playable in single player mode or two players mode. In single player mode you will play against the computer.")
    input("Choose the game mode: 1 player or 2 players. (1/2)")

    if input == "1":
        print("You chose single player mode.")
        return 1
    else:
        print("You chose two players mode.")
        return 2
    


def create_ships(possible_ships, amount_of_ships):
    pass



def single_player_game():
    pass



def two_players_game():
        # Create ships for the two players of the game. In the future we may be able to change the amount of the ships.
    # For now we will use the standard amount of ships.

    possible_ships = {"Carrier": 5, "Battleship": 4, "Cruiser": 3, "Submarine": 3, "Destroyer": 2}
    amount_of_ships = {"Carrier": 1, "Battleship": 1, "Cruiser": 1, "Submarine": 1, "Destroyer": 1}

    # Create ships for player 1
    create_ships(possible_ships, amount_of_ships)
    # Create ships for player 2
    create_ships(possible_ships, amount_of_ships)

    
    while True:
        # Player 1 turn
        print("Player 1 turn")
        pass
        # Player 2 turn
        print("Player 2 turn")
        pass






###############################################################
    ######################################################
###############################################################


# Start main code

def main():

    # Print the introduction of the game
    introduction()
    # Select game mode
    game_mode = select_game_mode()

    # Create boards for the two players of the game, with standard size 10 (10x10). In the future we may be able to 
    # change the size of the board.
    size = 10

    board1 = Board(size)
    board2 = Board(size)

    if game_mode == 1:
        single_player_game()
    else:
        two_players_game()






if __name__ == "__main__":
    main()