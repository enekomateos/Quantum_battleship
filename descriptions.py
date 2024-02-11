
# In this file we define the descriptions we want about the quantum aspects of the game.

import os


def print_game_description():
    """
    Print the description of the game.
    """

    print("Welcome to the Battleship game! \n")
    print("But, what would happen if the ships were really small and governed by the laws of quantum mechanics?")
    print("It is not the common Battleship game, it is a quantum version of it!")
    print("Let's play!")
    input("Press enter to continue")

def tutorial():
    print("The game is played in turns. In each turn you will have to choose a position to shoot in the board of the other player.")
    print("The game ends when all the ships of one of the players are destroyed.")
    print("Probably you have already played the normal version of the game, but this is a quantum version of it. So, there are some differences.")
    y = input("Would you like to know more about the quantum aspects of the game? If not, you will be able to get the descriptions when quantum events occur. (y/n)")
    if y == "y":
        superposition()
        os.system('cls' if os.name == 'nt' else "printf '\033c'")
        particle_wave_dual()
    input("Press enter to continue")

def superposition():
    print("The ships are governed by the laws of quantum mechanics. They can be in superposition, but what does it mean? Superposition is the property of a quantum system to be in many states simultaneously at the same time before the measurement.")
    print("In the game, it means that the ships can be in two places at the same time. When you shoot to a ship in a superposition, the ship will collapse to one of the possible positions when you hit it.")
    print("This is similar situation to meassuring a quantum system, after the mesurement the system will collapse to one of the possible states.")
    print("Superposition has many applications nowadays, for example, in quantum computing or quantum cryptography. It is a very important property of the quantum world.")
    print("As you can see this is a very peculiar property, that messes with our human intuition.")
    print("But, don't worry, you will get used to it!")
    print("If you would like more about the topic you can check the following link: https://quantumatlas.umd.edu/entry/superposition/")
    input("Press enter to continue")
    
def particle_wave_dual():
    print("The quantum realm has even more suprises for us. Our cannons won't be the normal ones. They will shoot quantum projectiles.")
    print("This means that they will behave as particles and as waves at the same time.")
    print("Upon a hit, there won't be a clear blast place, but rather the distribuiton of the possibilities of the hit.")
    print("So if we manage to reach a ship or not should be in principal impossible to determine with certainty.")
    print("Now if we think that we combine it with superimposed ships the game takes unexpected turn!")
    print("Just as the quantum physics, it will mess with our perception and show us that the world is not as we think it is.")
    print("Let's play now and see how it goes!")
    input("Press enter to continue")
    