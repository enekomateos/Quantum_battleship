import numpy as np

class Ships:
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
            #for i in range(0, self.length):
             #   vertical = [i + self.super_posy, self.super_posx]
             #   super_pos.append(vertical)
            return [positions, super_pos]
        
        return positions
            
            
            
        
obj = Ships(3, 2, 2, 'vertical', True,'horizontal', 2, 1)
print(obj.Ship())