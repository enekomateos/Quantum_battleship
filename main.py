
# Main code for the game

# Import block

import numpy as np
from board import Board
from ships import Ships
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
    


def create_ships(possible_ships, amount_of_ships, board):
    
    """
    Create the ships for the player.
    
    Args:
        possible_ships: dictionary with the possible ships and their lengths
        amount_of_ships: dictionary with the possible ships and the amount of ships of that type that can be created

    Returns:
        list of the positions of the ships
    """
    all_ships = []
    for ship in possible_ships:
        print("Create the ships for the player.")
        print("The ship is", ship, "and it has", possible_ships[ship], "positions.")
        print("You can create", amount_of_ships[ship], "ships of this type.")
        for i in range(amount_of_ships[ship]):
            print("Create the ship number", i+1)
            while True:
                try:
                    x = int(input("Enter the x coordinate of the initial position of the ship: "))
                    y = int(input("Enter the y coordinate of the initial position of the ship: "))
                except:
                    print("Invalid input. Please enter a number.")
                try:
                    orientation = input("Enter the orientation of the ship. It can be either 'vertical' or 'horizontal': ")
                    superposition = input("Do you want to create a ship on top of another ship? (y/n)")
                except:
                    print("Invalid input. Please enter either 'vertical' or 'horizontal' for orientation or 'y' or 'n' for superposition.")
                if superposition == "y":
                    try:
                        super_posx = int(input("Enter the x coordinate of the initial position of the ship that is going to be superimposed: "))
                        super_posy = int(input("Enter the y coordinate of the initial position of the ship that is going to be superimposed: "))
                    except:
                        print("Invalid input. Please enter a number.")
                    try:
                        super_pos_orientation = input("Enter the orientation of the ship that is going to be superimposed. It can be either 'vertical' or 'horizontal': ")
                    except:
                        print("Invalid input. Please enter either 'vertical' or 'horizontal' for orientation.")
                    ship = Ships(possible_ships[ship], x, y, orientation, True, super_pos_orientation, super_posx, super_posy)
                    all_ships.append(ship)
                    board.add_ship(ship)
                    os.system('cls' if os.name == 'nt' else "printf '\033c'")
                else:
                    ship = Ships(possible_ships[ship], x, y, orientation)
                    all_ships.append(ship)
                    board.add_ship(ship)
                    os.system('cls' if os.name == 'nt' else "printf '\033c'")
    return all_ships
                
 

def single_player_game(board1, board2):
    pass



def two_players_game(board_1, board_2):
        # Create ships for the two players of the game. In the future we may be able to change the amount of the ships.
    # For now we will use the standard amount of ships.

    # Remove everything from screen
    os.system('cls' if os.name == 'nt' else "printf '\033c'")

    possible_ships = {"Carrier": 5}#, "Battleship": 4, "Cruiser": 3, "Submarine": 3, "Destroyer": 2}
    amount_of_ships = {"Carrier": 1}#, "Battleship": 1, "Cruiser": 1, "Submarine": 1, "Destroyer": 1}

    # Create ships for player 1
    ships1 = create_ships(possible_ships, amount_of_ships, board1)
    # Create ships for player 2
    ships2 = create_ships(possible_ships, amount_of_ships, board2)


    # Print the boards to the players
    board_1.print_board(True)
    board_2.print_board(False)
    
    # while True:
    #     # Player 1 turn
    #     print("Player 1 turn")
    #     pass
    #     # Player 2 turn
    #     print("Player 2 turn")
    #     pass






###############################################################
    ######################################################
###############################################################


# Start main code

def main():
    global board1, board2

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
        single_player_game(board1, board2)
    else:
        two_players_game(board1, board2)






if __name__ == "__main__":
    main()