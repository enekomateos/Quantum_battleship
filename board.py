
# Here we define the board class

class Board:
    def __init__(self, size):
        self.size = size
        self.board = [[0 for i in range(size)] for j in range(size)]