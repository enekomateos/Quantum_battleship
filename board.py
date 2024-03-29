
# Here we define the board class

import numpy as np
import descriptions as desc

class Board:
    def __init__(self, size):
        """
        Initialize the board. The board is a square with size x size. The negative values represent places
        where there has already been a shot. The positive values represent the ships. Superpositions are represented
        by numbers greater than 1.

        For negative values, if -1 then there was a shot but there was no ship. If -2 then there was a shot 
        and there was a ship.
        
        Args:
            size (int): Size of the board. It will be a square board.

        Returns:
            None

        Creates:
            self.size (int): Size of the board.
            self.board (numpy array): Board with zeros in all positions.
            self.superposition_count (int): Count of superpositions in the board. Start at 1 so then we can distinguish superpositions
        
        Functions:
            add_ship: Add a ship to the board.
            check_valid_position: Check if a position is valid for a ship.
            check_hit: Check if a position is a hit.
            update_board: Update the board after a hit.
            print_board: Print the board.
            check_game_over: Check if the game is over.
        
        """

        self.size = size
        self.board = np.zeros((size, size), dtype=int)
        self.superposition_count = 1
    
    def check_valid_position(self, ship):

        """
        Check if a ship can be placed in the board.

        Args:
            ship (Class): Ship to be added to the board.


        Returns:
            valid (bool): True if the position is valid, False otherwise.
        """

        valid = True
        coords = ship.define_position()
        superposition = ship.superposition
        if superposition:
            coords_1 = coords[0]
            coords_2 = coords[1]
            for coord in coords_1:
                if coord[0] < 0 or coord[0] >= self.size or coord[1] < 0 or coord[1] >= self.size:
                    valid = False
                    print("The range of the ship goes outside the board.")
                elif self.board[coord[0], coord[1]] > 0:
                    valid = False
                    print("The ship is overlapping with another ship.")
            for coord in coords_2:
                if coord[0] < 0 or coord[0] >= self.size or coord[1] < 0 or coord[1] >= self.size:
                    valid = False
                    print("The range of the ship goes outside the board.")
                elif self.board[coord[0], coord[1]] > 0:
                    valid = False
                    print("The ship is overlapping with another ship.")
        else:
            for coord in coords:
                if coord[0] < 0 or coord[0] >= self.size or coord[1] < 0 or coord[1] >= self.size:
                    valid = False
                    print("The range of the ship goes outside the board.")
                elif self.board[coord[0], coord[1]] > 0:
                    valid = False
                    print("The ship is overlapping with another ship.")
        return valid


    def add_ship(self, ship):

        """
        Add ship to the board.

        Args:
            ship (Class): Ship to be added to the board.
                Ship.superposition. If false place the ship normally. If true, place the ship at two positions.
                Ship.position is a list containing tuples with the x and y coordinates of the ship. For example:
                [(0, 0), (0, 1)] for a ship of size 2 placed horizontally in the first row.

        Returns:
            None
        """

        superposition = ship.superposition

        # If the ship is not in superposition, place it normally
        if not superposition:
            coords = ship.define_position()
            for coord in coords:
                self.board[coord[0], coord[1]] = 1
        # If the ship is in superposition, place it in two positions and write 2 in the board to keep track of the superpositions
        else:
            self.superposition_count += 1
            coords1 = ship.define_position()[0]
            coords2 = ship.define_position()[1]
            for coord in coords1:
                self.board[coord[0], coord[1]] = self.superposition_count*10+1
            for coord in coords2:
                self.board[coord[0], coord[1]] = self.superposition_count*10+2

    
    def check_hit(self, position):
        """
        Check if a position is a hit.

        Args:
            position (tuple): Tuple with the x and y coordinates of the position to be checked.

        Returns:
            hit (bool): True if the position is a hit, False otherwise.
            superposition (int): If the position is a superposition, return the superposition number. If not, return 0.
        """

        hit = False
        superposition = 0
        if self.board[position[0], position[1]] > 0:
            hit = True
            if self.board[position[0], position[1]] > 1:
                superposition = self.board[position[0], position[1]]

        return hit, superposition
    


    def update_board(self, position):
        """
        Update the board after a hit. If there is a superposition, collapse it.

        Args:
            position (tuple): Tuple with the x and y coordinates of the position to be updated.

        Returns:
            None
        """

        # First apply wave-particle duality. The particle has a probability of being in an adjacent position

        if np.random.rand() > 0.8:
            print("Oh no! The particle did not go to where it was shot due to the wave-particle duality of the cannonball!")
            print("The particle went to an adjacent position!")
            ans = input("Would you like to know more about the wave-particle duality? (y/n)")
            if ans == "y" or ans == "Y" or ans == "yes" or ans == "Yes" or ans == "YES":
                desc.wave_particle_dual()
            if np.any(position)==0:
                possible_positions = [(position[0]+1,position[1]+1), (position[0],position[1]+1),
                                  (position[0]+1,position[1])]
                position = possible_positions[np.random.randint(0, 3)]
            elif np.any(position)==9:
                possible_positions = [(position[0]-1,position[1]-1), (position[0],position[1]-1),
                                  (position[0]-1,position[1])]
                position = possible_positions[np.random.randint(0, 3)]
            else:
                possible_positions = [(position[0]-1,position[1]-1), (position[0]-1,position[1]+1),
                                  (position[0]+1,position[1]-1), (position[0]+1,position[1]+1),
                                  (position[0],position[1]-1), (position[0],position[1]+1),
                                  (position[0]+1,position[1]), (position[0]-1,position[1])]
                position = possible_positions[np.random.randint(0, 7)]

        # Now proceed with the hit

        hit, superposition = self.check_hit(position)

        # In the following if we collapse the superposition if there is one
        if hit:
            print("HIT!")
            if superposition > 0:
                real_hit = np.random.rand() > 0.5

                ship_position1 = np.where(self.board == superposition)
                if str(superposition)[-1] == '1':
                    ship_position2 = np.where(self.board == superposition+1)
                else:
                    ship_position2 = np.where(self.board == superposition-1)
                
                if real_hit:
                    self.board[ship_position1] = 1
                    self.board[ship_position2] = 0
                else:
                    self.board[ship_position1] = 0
                    self.board[ship_position2] = 1
                    print("Oh no! The ship was in superposition and it collapsed to the other position!")
                    self.board[position[0], position[1]] = -1
                    return
            
        # Now we treat everything as a normal hit

            self.board[position[0], position[1]] = -2
        else:
            if self.board[position[0], position[1]] == 0:
                self.board[position[0], position[1]] = -1

    
    def print_board(self, player):
        """
        Print the board. For the player's board, we can see the ships.
        For the opponent's board, we can only see the shots and wether it was a hit or not.

        Args:
            player (bool): If True, print the board of the player.
              If False, print the board as the player sees the opponent's board.
              O is not shot, X is shot and hit, · is shot and miss.

        Returns:
            None
        """


        if player:
            print("Your board is: \n")
            print("     0  1  2  3  4  5  6  7  8  9", end=' ')
            print("\n   ----------------------------")
            text_board = ""
            for i in range(self.size):
                for j in range(self.size):
                    if j == 0:
                        if len(str(self.board[i, j]))==1:
                            text_board += f"{i} |  {self.board[i, j]} "
                        else:
                            text_board += f"{i} | {self.board[i, j]} "
                    else:
                        if len(str(self.board[i, j]))==1:
                            text_board += f" {self.board[i, j]} "
                        else:
                            text_board += f"{self.board[i, j]} "
                text_board += "\n"
            print(text_board)
        else:
            print("Your opponent's board is: ")
            print("     0  1  2  3  4  5  6  7  8  9", end=' ')
            print("\n  -----------------------------")
            text_board = ""
            for i in range(self.size):
                for j in range(self.size):
                    if j == 0:
                        text_board += f"{i} |  "
                    if self.board[i, j] == -1:
                        text_board += "O  "
                    elif self.board[i, j] == -2:
                        text_board += "X  "
                    else:
                        text_board += "·  "
                text_board += "\n"
            print(text_board)
    

    def check_game_over(self):
        """
        Check if the game is over.

        Returns:
            game_over (bool): True if the game is over, False otherwise.
        """

        game_over = False
        if np.all(self.board <= 0):
            game_over = True
        return game_over