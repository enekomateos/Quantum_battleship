
# This file will include utility functions for the main game file but are better here so that the main
# file is not too long.

import os
import descriptions as desc
import numpy as np
from board import Board
from ships import Ships



def introduction():

    """
    Print the introduction of the game.
    """

    # Welcome message
    desc.print_game_description()

    tutorial = input("Do you need a tutorial? (y/n)")
    if tutorial == "y":
        desc.tutorial()

    os.system('cls' if os.name == 'nt' else "printf '\033c'")    



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
                orientation = input("Enter the orientation of the ship. It can be either 'vertical' or 'horizontal': ")
                if orientation == "vertical" or orientation == "horizontal" or orientation == "Vertical" or orientation == "Horizontal" or orientation == "VERTICAL" or orientation == "HORIZONTAL" or orientation == "v" or orientation == "h" or orientation == "V" or orientation == "H":
                    break
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
                    if super_pos_orientation != "vertical" or super_pos_orientation != "horizontal" or super_pos_orientation != "Vertical" or super_pos_orientation != "Horizontal" or super_pos_orientation != "VERTICAL" or super_pos_orientation != "HORIZONTAL" or super_pos_orientation != "v" or super_pos_orientation != "h" or super_pos_orientation != "V" or super_pos_orientation == "H":
                        print("Invalid input. Please enter a number and correct orientation.")
                        continue
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


def create_ships_computer(possible_ships, amount_of_ships, board):

    """
    Creates and places the ships for the computer.

    Args:
        possible_ships: dictionary with the possible ships and their lengths
        amount_of_ships: dictionary with the possible ships and the amount of ships of that type that can be created

    Returns:
        list of the positions of the ships
    """

    all_ships = []
    for ship_name in possible_ships:
        i=1
        while i<=amount_of_ships[ship_name]:
            x = np.random.randint(0, 10)
            y = np.random.randint(0, 10)
            orientation = np.random.choice(["vertical", "horizontal"])
            superposition = np.random.choice(["y", "n"])
            if superposition == "y":
                super_posx = np.random.randint(0, 10)
                super_posy = np.random.randint(0, 10)
                super_pos_orientation = np.random.choice(["vertical", "horizontal"])
                ship = Ships(possible_ships[ship_name], y, x, orientation, True, super_pos_orientation, super_posy, super_posx)
                all_ships.append(ship)
                if board.check_valid_position(ship):
                    board.add_ship(ship)
                else:
                    continue
            else:
                ship = Ships(possible_ships[ship_name], y, x, orientation)
                all_ships.append(ship)
                if board.check_valid_position(ship):
                    board.add_ship(ship)
                else:
                    continue
            i +=1

def pass_computer():

    """
    Very repeating code so this function is for legibility.
    """
    os.system('cls' if os.name == 'nt' else "printf '\033c'")
    input("Pass the computer to the other player. Press enter to continue.")
    os.system('cls' if os.name == 'nt' else "printf '\033c'")

def situation(player, board1, board2):
    if player==1:
        print("Your situation is:")
        print("")
        board1.print_board(True)
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
 