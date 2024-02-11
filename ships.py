import numpy as np

class Ships:
    '''This class is used to create the ships for the game. The ships are created with the following parameters:
    
    length: the length of the ship
    x_init: the x coordinate of the initial position of the ship
    y_init: the y coordinate of the initial position of the ship
    orientation: the orientation of the ship, it can be either 'vertical' or 'horizontal'
    superposition: allows to create a ship on top of another ship, it can be either True or False
    super_pos_orientation: the orientation of the ship that is going to be superimposed, it can be either 'vertical' or 'horizontal'
    super_posx: the x coordinate of the initial position of the ship that is going to be superimposed
    super_posy: the y coordinate of the initial position of the ship that is going to be superimposed
    
    Returns: a list with the positions of the ship
    '''
    def __init__(self, length, x_init, y_init, orientation, superposition = False, super_pos_orientation = None, super_posx = 0, super_posy = 0):
        self.length = length
        self.x_init = x_init
        self.y_init = y_init
        self.orientation = orientation
        self.superposition = superposition
        self.super_pos_orientation = super_pos_orientation
        self.super_posx = super_posx
        self.super_posy = super_posy
        
    def Ship(self):
        positions = []
        
        if self.orientation == 'vertical':
            for i in range(0, self.length):
                vertical = [i + self.y_init, self.x_init]
                positions.append(vertical)
        if self.orientation == 'horizontal':
            for i in range(0, self.length):
                horizontal = [self.y_init, i + self.x_init]
                positions.append(horizontal)
                
                
        if self.superposition == True:
            super_pos = []
            if self.super_pos_orientation == 'vertical':
                for i in range(0, self.length):
                    vertical = [i + self.super_posy, self.super_posx]
                    super_pos.append(vertical)
            if self.super_pos_orientation == 'horizontal':
                for i in range(0, self.length):
                    horizontal = [self.super_posy, i + self.super_posx]
                    super_pos.append(horizontal)

            return [positions, super_pos]
        
        return positions
            
            
            