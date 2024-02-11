
# Main code for the game

# Import block

import numpy as np
from board import Board


# Functions


# Start main code

def main():

    # Welcome message
    print("Welcome to the Battleship game!")
    print("But, what would happen if the ships were really small and governed by the laws of quantum mechanics?")
    print("It is not the common Battleship game, it is a quantum version of it!")

    # Create boards for the two players of the game, with standard size 10 (10x10). In the future we may be able to 
    # change the size of the board.
    size = 10

    board1 = Board(size)
    board2 = Board(size)

    # Create ships for the two players of the game. In the future we may be able to change the amount of the ships.
    # For now we will use the standard amount of ships.

    possible_ships = {"Carrier": 5, "Battleship": 4, "Cruiser": 3, "Submarine": 3, "Destroyer": 2}
    amount_of_ships = {"Carrier": 1, "Battleship": 1, "Cruiser": 1, "Submarine": 1, "Destroyer": 1}

    # Create ships for player 1

    # Create ships for player 2

    # Start the game

    while True:
        # Player 1 turn
        print("Player 1 turn")
        pass
        # Player 2 turn
        pass





if __name__ == "__main__":
    main()