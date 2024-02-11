
# Here we define the board class

import numpy as np

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
        """

        self.size = size
        self.board = np.zeros((size, size))
        self.superposition_count = 1
    


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
            coords = ship.position
            for coord in coords:
                self.board[coord[0], coord[1]] = 1
        # If the ship is in superposition, place it in two positions and write 2 in the board to keep track of the superpositions
        else:
            self.superposition_count += 1
            coords1 = ship.position[0]
            coords2 = ship.position[1]
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

        hit, superposition = self.check_hit(position)

        # In the following if we collapse the superposition if there is one
        if hit:
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
            
        # Now we treat everything as a normal hit

            self.board[position[0], position[1]] = -2
        else:
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
            print("Your board is: ")
            print("  ", range(0,9), end=' ')
            for i in range(self.size):
                for j in range(self.size):
                    print(self.board[i, j], end='  ')
                print('\n')
        else:
            print("Your opponent's board is: ")
            for i in range(self.size):
                for j in range(self.size):
                    if self.board[i, j] >= 0:
                        print('O', end='  ')
                    elif self.board[i, j] == -1:
                        print('·', end='  ')
                    else:
                        print('X', end='  ')
                print("\n")