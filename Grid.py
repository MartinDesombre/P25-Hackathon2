import random 
import numpy as np
from herbe import Herbe
from loup import Loup
from mouton import Mouton

GRID_SIZE = 30
GRASS_COVERAGE = 0.3

grille_herbe = np.array([[Herbe(x, y) for y in range(30)] for x in range(30)])
vectorized_repousse = np.vectorize(lambda herbe: herbe.repousse())


class Grid:
    def __init__(self, size):
        self.size = size
        self.cells = [random.choices(['.', '#'], weights=[GRASS_COVERAGE,1-GRASS_COVERAGE], k = size) for _ in range(size)]
       

    def update_grid(self, updates):
        for i in range(len(grille_herbe)):
            for j in range(len(grille_herbe)):
                if grille_herbe[i][j].tps_depuis_mort == -1:
                    self.cells[i][j] = '#'
                else:
                    self.cells[i][j] = '.'

        for mouton in moutons:
            x, y = mouton.x, mouton.y
            if mouton._en-vie =='True':
                self.cells[x][y] = 'M'
            
        for loup in loups:
            x, y = loup.x, loup.y
            if loup._en-vie =='True':
                self.cells[x][y] = 'W'
    
    def case_vide(self, x,y) :  ### renvoie un booléen qui indique s'il existe une case vide et la direction de la case vide
        if (self.cells[x+1][y] == "#" or self.cells[x+1][y] == ".") :
            return (True, 1, 0)
        if (self.cells[x][y+1] == "#" or self.cells[x][y+1] == ".") :
            return (True, 0, 1)
        if (self.cells[x-1][y] == "#" or self.cells[x-1][y] == ".") :
            return (True, -1, 0)
        if (self.cells[x][y-1] == "#" or self.cells[x][y-1] == ".") :
            return (True, 0, -1)
        return (False, 0, 0)

    

            

   
  
