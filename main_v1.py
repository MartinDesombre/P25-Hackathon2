import random
import numpy as np
from herbe import Herbe


GRID_SIZE = 30
GRASS_COVERAGE = 0.3

grille_herbe = np.array([[Herbe(x, y) for y in range(30)] for x in range(30)])
vectorized_repousse = np.vectorize(lambda herbe: herbe.repousse())


class Herbe():
    def __init__(self,x,y):
        self.x = x
        self.y = y
        self.tps_depuis_mort = -1 if random.random() <= 0.3 else random.randint(0,7)
        # si tps_depuis_mort = -1, l'herbe est vivante
        # si tps_depuis_mort = 0, l'herbe vient d'être mangée
        # si tps_depuis_mort > 0, tps_depuis_mort represente le nombre de tours depuis la mort
    
    def mangee(self):
        self.tps_depuis_mort = -1

    def repousse(self):
        if grid.cells[self.x][self.y] == 'M':
            pass  # Ne rien faire s'il y a un mouton
        else:
            if self.tps_depuis_mort == -1:
                pass  # L'herbe est deja vivante, ne rien faire
            else:
                self.tps_depuis_mort += 1  # on actualise le tps depuis la mort
                # Vérifier si l'herbe doit repousser
                if random.random() < 0.08 or self.tps_depuis_mort >= 7:
                    self.tps_depuis_mort = -1  # Réinitialiser le temps depuis la mort


dxdy = [(1,0),(0,1),(-1,0),(0,-1)]
class Loup :

    def __init__(self,x,y):
        self.vivant = True
        self.x = x
        self.y = y
        self.age = 0
        self.energie = 40
        self.seuil = 80 #seuil pour la reproduction
        self.limite = 40 #limite d'age

    def vieillir(self):
        if self.vivant :
            self.age += 1

    def perte_energie(self):
        if self.vivant :
            self.energie -= 2

    def mort(self):
        if self.vivant and (self.age>self.limite or self.energie<0) :
            self.vivant = False

    def reproduction(self):
        if self.vivant and energie>seuil :
            i = random.randint(0,3)
            dx = dxdy[i][0]
            dy = dxdy [i][1]
            c = 0
            while c<4 and not(libre(dx,dy)):
                c = c+1
                i = (i+1)%4
                dx = dxdy[i][0]
                dy = dxdy[i][1]
            if c<4:
            
                petit = Loup(self.x+dx,self.y+dy,id)
                self.energie -= 20
                return petit
        
    def mouton_voisin (self):
        if Grid.is_mouton(self.x,self.y)[0] :
            return Grid.is_mouton[1:2]
        
    def deplacement(self):
        """se deplace et mange le cas echeant"""
        if self.vivant :
            mv = mouton_voisin(self.x,self.y)
            if mv[0]: 
                self.x = mv[1]
                self.y = mv[2]
                self.energie += 30
            else :
                i = random.randint(0,3)
            dx = dxdy[i][0]
            dy = dxdy [i][1]
            c = 0
            while c<4 and not(libre(dx,dy)):
                c = c+1
                i = (i+1)%4
                dx = dxdy[i][0]
                dy = dxdy[i][1]
            if c <4:
                self.x += dx
                self.y += dy

def libre (x,y):
    for loup in loups:
        if loup.x == x :
            if loup.y == y :
                return False
    for mouton in moutons:
        if mouton.x == x :
            if mouton.y == y :
                return False
    return True





class Mouton(): 
    def __init__ (self, x, y) : 
        self._x = x
        self._y = y
        self._age = 0    
        self._energie = 20
        self._en_vie = True
    
    def vieillir (self) :
        self._age += 1
    
    def trouve_herbe (self) :
        if Grid.cells[self._x+1][self._y] == '#' : 
            return (True, 1, 0)
        if Grid.cells[self._x][self._y+1] == '#' : 
            return (True, 0, 1)
        if Grid.cells[self._x-1][self._y] == '#' : 
            return (True, -1, 0)
        if Grid.cells[self._x][self._y-1] == '#' : 
            return (True, 0, -1)
        return (False,0,0)
    
    def direction_aleatoire (self):
        a = random.randint (1,4)
        if (a == 1 and self._x + 1 <=30):
            return (1,0)
        elif (a == 2 and self._y + 1 <= 30) :
            return (0,1)
        elif (a == 3 and self._x -1 >=0):
            return(-1,0)
        elif (a == 4 and self._y -1 >=0):
            return (0,-1)

    def deplace (self,dx,dy) :
        self._x += dx
        self._y += dy
        
    
    def manger (self) :
        self._energie += 10

    def reproduction (self) : 
        if (self._energie > 50 and Grid.case_vide(self._x,self._y)[0]):
            self._energie += -20
            dx,dy = Grid.case_vide(self._x,self._y)[1:2]
            moutons[len(moutons)]= Mouton(self._x + dx, self._y + dy)

    def mort (self) :
        if self._energie <= 0 :
            self._en_vie = False
        if self._age > 50 :
            self._en_vie = False


        

    
    



class Grid:
    def __init__(self, size):
        self.size = size
        self.cells = np.array([["#"]*10 for _ in range(10)])
        
       

    def update_grid(self, updates):
        for i in range(len(grille_herbe)):
            for j in range(len(grille_herbe)):
                if grille_herbe[i][j].tps_depuis_mort == -1:
                    self.cells[i][j] = '#'
                else:
                    self.cells[i][j] = '.'

        for mouton in moutons:
            x, y = mouton.x, mouton.y
            if mouton._en_vie =='True':
                self.cells[x][y] = 'M'
            
        for loup in loups:
            x, y = loup.x, loup.y
            if loup._en_vie =='True':
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

    

grid = Grid((10,10))
            


moutons = [Mouton(1,1),Mouton(5,5),Mouton(10,10)]

  




def trouver_mouton(x,y):
    for mouton in moutons:
        if mouton.x == x and mouton.y == y:
            return mouton

nb_tours = 0
while nb_tours < 50:
    # Update sheep
    for mouton in moutons:
        if mouton._en_vie:
            mouton.vieillir()

            herbe_trouvee = mouton.trouve_herbe()
            if herbe_trouvee[0]:
                mouton.deplace(herbe_trouvee[1:3])  # Assuming [x, y] coordinates
                grille_herbe[mouton.x][mouton.y].mangee()
                mouton.manger()
            else:
                mouton.deplace(direction_aleatoire)

            if mouton.energie > 50:
                mouton.reproduction()
            mouton.energie -= 1



    # Update grid and herbs
    vectorized_repousse(grille_herbe)
    Grid.update()

    nb_tours += 1

print("fin")


"""    # Update wolves
    for loup in loups:
        loup.vieillir()
        loup.perte_energie()

        if loup.trouve_mouton():
            mouton = loup.trouve_mouton()  # Assuming this returns the mouton object
            mouton._en_vie = False

        if loup.energie <= 0:
            loup.mort()

        loup.reproduction()"""