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
        vectorized_repousse(grille_herbe)
        for i in range(len(grille_herbe)):
            for j in range(len(grille_herbe)):
                if grille_herbe[i][j].tps_depuis_mort == -1:
                    self.cells[i][j] = '#'
                else:
                    self.cells[i][j] = '.'

        for list_mouton in Liste_mouton:
            for mouton in Liste_mouton:
                x, y = mouton[1], mouton[2]
                if mouton[0]=='alive':
                    self.cells[x][y] = 'M'
            
        for list_loup in Loup.list():
            for loup in list_loup:
                x, y = loup[1], loup[2]
                if loup[0]=='alive':
                    self.cells[x][y] = 'W'

    

            

   
  
