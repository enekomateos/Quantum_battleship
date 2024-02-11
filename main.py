
# Main code for the game. THis is the file to be executed
# Authors: Eneko Mateos and Mateusz Molenda

# Import block

import numpy as np
from board import Board
import os
from utilities_main import introduction, create_ships, pass_computer, situation, create_ships_computer

# Functions

def single_player_game(board1, board2):
    # Remove everything from screen
    os.system('cls' if os.name == 'nt' else "printf '\033c'")

    possible_ships = {"Carrier": 5}#, "Battleship": 4, "Cruiser": 3, "Submarine": 3, "Destroyer": 2}
    amount_of_ships = {"Carrier": 1}#, "Battleship": 1, "Cruiser": 1, "Submarine": 1, "Destroyer": 1}

    ships1 = create_ships(possible_ships, amount_of_ships, board1)
    input("Press enter to continue, the computer will create its ships.")
    ships2 = create_ships_computer(possible_ships, amount_of_ships, board2)

    os.system('cls' if os.name == 'nt' else "printf '\033c'")
    input("The boards are ready. Let's play!")

    while True:
        situation(1, board1, board2)
        # Player 1 turn
        print("Player 1 turn\n")
        print("Choose the position to shoot.")
        while True:
            try:
                x = int(input("Enter the vertical coordinate: "))
                y = int(input("Enter the horizontal coordinate: "))
                if x < 0 or x > 9 or y < 0 or y > 9:
                    print("Invalid input. Please enter a number between 0 and 9.")
                    continue
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

        # Computer turn
        print("Computer turn\n")
        x = np.random.randint(0, 10)
        y = np.random.randint(0, 10)
        position = (x, y)
        print(f"The computer chose the position {position} to shoot.")
        board1.update_board(position)

        # Check if the game is over
        if board1.check_game_over():
            print("Computer wins!")
            break




def two_players_game(board1, board2):
        # Create ships for the two players of the game. In the future we may be able to change the amount of the ships.
        # For now we will use the standard amount of ships.

    # Remove everything from screen
    os.system('cls' if os.name == 'nt' else "printf '\033c'")

    possible_ships = {"Carrier": 5, "Battleship": 4, "Cruiser": 3, "Submarine": 3, "Destroyer": 2}
    amount_of_ships = {"Carrier": 1, "Battleship": 1, "Cruiser": 1, "Submarine": 1, "Destroyer": 1}

    # Create ships for player 1
    ships1 = create_ships(possible_ships, amount_of_ships, board1)
    pass_computer()
    # Create ships for player 2
    ships2 = create_ships(possible_ships, amount_of_ships, board2)
    pass_computer()


    # Print the boards to the players
    print("The boards are ready. Let's play!")

    while True:
        situation(1, board1, board2)
        # Player 1 turn
        print("Player 1 turn\n")
        print("Choose the position to shoot.")
        while True:
            try:
                x = int(input("Enter the vertical coordinate: "))
                y = int(input("Enter the horizontal coordinate: "))
                if x < 0 or x > 9 or y < 0 or y > 9:
                    print("Invalid input. Please enter a number between 0 and 9.")
                    continue
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
        situation(1, board1, board2)
        pass_computer()

        # Player 2 turn
        situation(2, board1, board2)
        print("Player 2 turn\n")
        print("Choose the position to shoot.")
        while True:
            try:
                x = int(input("Enter the vertical coordinate: "))
                y = int(input("Enter the horizontal coordinate: "))
                if x < 0 or x > 9 or y < 0 or y > 9:
                    print("Invalid input. Please enter a number between 0 and 9.")
                    continue
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
        situation(2, board1, board2)
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
    game_mode = input("Choose the game mode. Press 1 for single player mode and 2 for two players mode: (1/2) ")

    # Create boards for the two players of the game, with standard size 10 (10x10). In the future we may be able to 
    # change the size of the board.
    size = 10

    board1 = Board(size)
    board2 = Board(size)

    if game_mode == "1":
        input("You chose single player mode.")
        single_player_game(board1, board2)
    else:
        print("You chose two players mode.")
        two_players_game(board1, board2)






if __name__ == "__main__":
    main()