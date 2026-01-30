
GRID_SIZE = 30
GRASS_COVERAGE = 0.3

class Grid:
    def __init__(self, size):
        self.size = size
        self.cells = [['.' for _ in range(size)] for _ in range(size)]

    def set_cell(self, size):
        self.cells = [random.choices(['.', '#'], weights=[GRASS_COVERAGE,1-GRASS_COVERAGE], k = size) for _ in range(size)]

    def update_grid(self, updates):
        for sheep in Sheep.list():
            x, y = sheep[1], sheep[2]
            if sheep[0]=='alive':
                self.cells[x][y] = 'M'
            
        for wolf in Wolf.list():
            x, y = wolf[1], wolf[2]
            if wolf[0]=='alive':
                self.cells[x][y] = 'W'

            


  
