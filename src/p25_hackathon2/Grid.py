import random 

GRID_SIZE = 30
GRASS_COVERAGE = 0.3

grille_herbe = np.array([[Herbe(x, y) for y in range(30)] for x in range(30)])
vectorized_repousse = np.vectorize(lambda herbe: herbe.repousse())
vectorized_repousse(grille_herbe)

class Grid:
    def __init__(self, size):
        self.size = size
        self.cells = [random.choices(['.', '#'], weights=[GRASS_COVERAGE,1-GRASS_COVERAGE], k = size) for _ in range(size)]

    def update_grid(self, updates):
        for list_mouton in Sheep.list():
            for sheep in list_mouton:
                x, y = sheep[1], sheep[2]
                if sheep[0]=='alive':
                    self.cells[x][y] = 'M'
            
        for list_loup in Wolf.list():
            for wolf in list_loup:
                x, y = wolf[1], wolf[2]
                if wolf[0]=='alive':
                    self.cells[x][y] = 'W'

            

    def update_herbe():
        grille_herbe = np.array([[Herbe(x, y) for y in range(30)] for x in range(30)])
        vectorized_repousse = np.vectorize(lambda herbe: herbe.repousse())
        vectorized_repousse(grille_herbe)
        
  
