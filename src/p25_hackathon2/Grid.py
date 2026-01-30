
GRID_SIZE = 30
GRASS_COVERAGE = 0.3

class Grid:
    def __init__(self, size):
        self.size = size
        self.cells = [['.' for _ in range(size)] for _ in range(size)]

    def set_cell(self, size):
        self.cells = [random.choices(['.', '#'], weights=[GRASS_COVERAGE,1-GRASS_COVERAGE], k = size) for _ in range(size)]
        L2 = []
        for i in range(size):
            L2.append([])
            for j in range(size):
                if self.cells[i][j] == 1:
                    L2[i].append(j)
        return L2

    def update_grid(self, updates):


    def get_cell(self, x, y):
        if 0 <= x < self.width and 0 <= y < self.height:
            return self.cells[y][x]
        else:
            raise IndexError("Cell position out of bounds")

    def display(self):
        for row in self.cells:
            print(" ".join(str(cell) for cell in row))
    
