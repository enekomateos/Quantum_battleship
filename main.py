
# Main code for the game

# Import block

import numpy as np
from board import Board
from ships import Ships
import descriptions as desc
import os

# Functions

def introduction():

    """
    Print the introduction of the game.
    """

    # Welcome message
    desc.print_game_description()
    os.system('cls' if os.name == 'nt' else "printf '\033c'")

    tutorial = input("Do you need a tutorial? (y/n)")
    if tutorial == "y":
        desc.tutorial()

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
    for ship_name in possible_ships:
        os.system('cls' if os.name == 'nt' else "printf '\033c'")
        board.print_board(True)
        print("")
        print("Create the ships.")
        print("The ship is", ship_name, "and it has", possible_ships[ship_name], "positions.")
        print("You can create", amount_of_ships[ship_name], "ships of this type.")
        i=1
        while i<=amount_of_ships[ship_name]:
            print("Create the ship number", i)
            while True:
                try:
                    x = int(input("Enter the vertical coordinate of the initial position of the ship: "))
                    y = int(input("Enter the horizontal coordinate of the initial position of the ship: "))
                    break
                except:
                    print("Invalid input. Please enter a number.")
            while True:
                try:
                    orientation = input("Enter the orientation of the ship. It can be either 'vertical' or 'horizontal': ")
                    break
                except:
                    print("Invalid input. Please enter either 'vertical' or 'horizontal' for orientation.")
            superposition = input("Do you want to create a superposition of the ship? (y/n)")
            if superposition == "y" or superposition == "Y" or superposition == "yes" or superposition == "Yes" or superposition == "YES":
                print("SUPERPOSITION")
                while True:
                    invalid = False
                    try:
                        super_posx = int(input("Enter the vertical coordinate of the initial position of the ship that is going to be superimposed: "))
                        super_posy = int(input("Enter the horizontal coordinate of the initial position of the ship that is going to be superimposed: "))
                        super_pos_orientation = input("Enter the orientation of the ship that is going to be superimposed. It can be either 'vertical' or 'horizontal': ")
                    except:
                        print("Invalid input. Please enter a number and correct orientation.")
                    pos_sup = []
                    if super_pos_orientation == "vertical":
                        for j in range(possible_ships[ship_name]):
                            pos_sup.append((super_posy, super_posx+j))
                    else:
                        for j in range(possible_ships[ship_name]):
                            pos_sup.append((super_posy+j, super_posx))
                    print(pos_sup)
                    pos = []
                    if orientation == "vertical":
                        for j in range(possible_ships[ship_name]):
                            pos.append((y, x+j))
                    else:
                        for j in range(possible_ships[ship_name]):
                            pos.append((y+j, x))
                    print(pos)
                    for j in pos:
                        if j in pos_sup:
                            print("Invalid position for the superposition. Please choose another position.")
                            invalid = True
                    if invalid:
                        continue
                    break

                ship = Ships(possible_ships[ship_name], y, x, orientation, True, super_pos_orientation, super_posy, super_posx)
                all_ships.append(ship)
                if board.check_valid_position(ship):
                    board.add_ship(ship)
                else:
                    print("Invalid position for the ship. Please choose another position.")
                    continue
                
                input("Press enter to continue")
            else:
                ship = Ships(possible_ships[ship_name], y, x, orientation)
                all_ships.append(ship)
                if board.check_valid_position(ship):
                    board.add_ship(ship)
                else:
                    print("Invalid position for the ship. Please choose another position.")
                    continue
            i +=1
            input("Press enter to continue")
    print("All the ships are created. The board looks like this:")
    board.print_board(True)
    return all_ships
                

def pass_computer():

    """
    Very repeating code so this function is for legibility.
    """
    os.system('cls' if os.name == 'nt' else "printf '\033c'")
    input("Pass the computer to the other player. Press enter to continue.")
    os.system('cls' if os.name == 'nt' else "printf '\033c'")

def situation(player):
    if player==1:
        print("Your situation is:")
        print("Your board:")
        print("")
        board1.print_board(True)
        print("Your opponent's board:")
        print("")
        board2.print_board(False)
    else:
        print("Your situation is:")
        print("Your board:")
        print("")
        board2.print_board(True)
        print("Your opponent's board:")
        print("")
        board1.print_board(False)
    input("Press enter to continue")
 

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
    pass_computer()
    # Create ships for player 2
    ships2 = create_ships(possible_ships, amount_of_ships, board2)
    pass_computer()


    # Print the boards to the players
    print("The boards are ready. Let's play!")

    while True:
        situation(1)
        # Player 1 turn
        print("Player 1 turn\n")
        print("Choose the position to shoot.")
        while True:
            try:
                x = int(input("Enter the vertical coordinate: "))
                y = int(input("Enter the horizontal coordinate: "))
                break
            except:
                print("Invalid input. Please enter a number.")
        os.system('cls' if os.name == 'nt' else "printf '\033c'")
        position = (x, y)
        board2.update_board(position)

        # Check if the game is over
        if board2.check_game_over():
            print("Player 1 wins!")
            break

        # Print the boards to the players
        situation(1)
        pass_computer()

        # Player 2 turn
        situation(2)
        print("Player 2 turn\n")
        print("Choose the position to shoot.")
        while True:
            try:
                x = int(input("Enter the vertical coordinate: "))
                y = int(input("Enter the horizontal coordinate: "))
                break
            except:
                print("Invalid input. Please enter a number.")
        position = (x, y)
        os.system('cls' if os.name == 'nt' else "printf '\033c'")
        board1.update_board(position)

        # Check if the game is over
        if board1.check_game_over():
            print("Player 2 wins!")
            break

        # Check if the game is over
        if board2.check_game_over():
            print("Player 1 wins!")
            break

        # Print the boards to the players
        situation(2)
        pass_computer()






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