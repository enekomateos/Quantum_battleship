
# In this file we define the descriptions we want about the quantum aspects of the game.

# The first function is the one that prints the description of the game. It is called in the main.py file.

def print_game_description():
    """
    Print the description of the game.
    """

    print("Welcome to the Battleship game!")
    print("But, what would happen if the ships were really small and governed by the laws of quantum mechanics?")
    print("It is not the common Battleship game, it is a quantum version of it!")
    print("Let's play!")

def tutorial():
    print("The game is played in turns. In each turn you will have to choose a position to shoot in the board of the other player.")
    print("The game ends when all the ships of one of the players are destroyed.")
    print("In the beggining the ships are placed in the board. You will have to guess where the opponent's ships are.")
    print("The ships are governed by the laws of quantum mechanics. They can be in superposition, so they can be in two places at the same time.")
    print("When you shoot a ship in a superposition, the ship will collapse to one of the positions, and you will know if you hit the ship or not.")
    print("The game is over when all the ships of one of the players are destroyed.")
    print("Good luck!")
    input("Press enter to continue")

def superposition():
    print("The ships are governed by the laws of quantum mechanics. They can be in superposition, so they can be in two places at the same time.")
    print("When you shoot a ship in a superposition, the ship will collapse to one of the positions, and you will know if you hit the ship or not.")
    input("Press enter to continue")