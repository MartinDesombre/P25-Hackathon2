import numpy as np

# Example Herbe class with an update method
class Herbe:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.tps_depuis_mort = 0

    def repousse(self):
        # Your logic for repousse
        pass

# Create a grid of Herbe instances


grille_herbe = np.array([[Herbe(x, y) for y in range(30)] for x in range(30)])

vectorized_repousse = np.vectorize(lambda herbe: herbe.repousse())

vectorized_repousse(grille_herbe)




def is_mouton(x,y):
    if grille[x][y] == 'M':
        return True
    return False
