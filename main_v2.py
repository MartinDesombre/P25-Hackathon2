import random
import numpy as np
import matplotlib.pyplot as plt

GRID_SIZE = 30
GRASS_COVERAGE = 0.3

# Initialize the grass grid

vectorized_repousse = np.vectorize(lambda herbe: herbe.repousse())

# Directions for movement
dxdy = [(1, 0), (0, 1), (-1, 0), (0, -1)]

class Herbe:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.tps_depuis_mort = -1 if random.random() <= GRASS_COVERAGE else random.randint(0, 7)

    def mangee(self):
        self.tps_depuis_mort = 0

    def repousse(self):
        if self.tps_depuis_mort == -1:
            pass  # Grass is already alive
        else:
            self.tps_depuis_mort += 1
            if random.random() < 0.08 or self.tps_depuis_mort >= 7:
                self.tps_depuis_mort = -1  # Grass regrows

class Loup:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.vivant = True
        self.age = 0
        self.energie = 40
        self.seuil = 80
        self.limite = 40

    def vieillir(self):
        if self.vivant:
            self.age += 1

    def perte_energie(self):
        if self.vivant:
            self.energie -= 2

    def mort(self):
        if self.vivant and (self.age > self.limite or self.energie <= 0):
            self.vivant = False

    def reproduction(self):
        if self.vivant and self.energie > self.seuil:
            for dx, dy in dxdy:
                nx, ny = self.x + dx, self.y + dy
                if 0 <= nx < GRID_SIZE and 0 <= ny < GRID_SIZE and libre(nx, ny):
                    self.energie -= 20
                    return Loup(nx, ny)
        return None

    def trouve_mouton(self):
        for dx, dy in dxdy:
            nx, ny = self.x + dx, self.y + dy
            if 0 <= nx < GRID_SIZE and 0 <= ny < GRID_SIZE:
                for mouton in moutons:
                    if mouton.x == nx and mouton.y == ny and mouton._en_vie:
                        return (True, nx, ny)
        return (False, 0, 0)

    def deplacement(self):
        if self.vivant:
            mv = self.trouve_mouton()
            if mv[0]:
                self.x, self.y = mv[1], mv[2]
                self.energie += 30
            else:
                dx, dy = random.choice(dxdy)
                nx, ny = self.x + dx, self.y + dy
                if 0 <= nx < GRID_SIZE and 0 <= ny < GRID_SIZE and libre(nx, ny):
                    self.x, self.y = nx, ny

class Mouton:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self._age = 0
        self._energie = 20
        self._en_vie = True

    def vieillir(self):
        self._age += 1

    def trouve_herbe(self):
        for dx, dy in dxdy:
            nx, ny = self.x + dx, self.y + dy
            if 0 <= nx < GRID_SIZE and 0 <= ny < GRID_SIZE:
                if grille_herbe[nx][ny].tps_depuis_mort == -1:
                    return (True, dx, dy)
        return (False, 0, 0)

    def direction_aleatoire(self):
        dx, dy = random.choice(dxdy)
        nx, ny = self.x + dx, self.y + dy
        if 0 <= nx < GRID_SIZE and 0 <= ny < GRID_SIZE and libre(nx, ny):
            return (dx, dy)
        return (0, 0)

    def deplace(self, dxdy):
        dx, dy = dxdy
        nx, ny = self.x + dx, self.y + dy
        if 0 <= nx < GRID_SIZE and 0 <= ny < GRID_SIZE:
            self.x, self.y = nx, ny

    def manger(self):
        self._energie += 10

    def reproduction(self):
        if self._energie > 50:
            for dx, dy in dxdy:
                nx, ny = self.x + dx, self.y + dy
                if 0 <= nx < GRID_SIZE and 0 <= ny < GRID_SIZE and libre(nx, ny):
                    self._energie -= 20
                    moutons.append(Mouton(nx, ny))
                    break

    def mort(self):
        if self._energie <= 0 or self._age > 50:
            self._en_vie = False


import random as rd
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
        if self.vivant and self.energie > self.seuil :
            i = rd.randint(0,3)
            dx = dxdy[i][0]
            dy = dxdy [i][1]
            c = 0
            while c<4 and not(libre(dx,dy)):
                c = c+1
                i = (i+1)%4
                dx = dxdy[i][0]
                dy = dxdy[i][1]
            if c<4:
                petit = Loup(self.x+dx,self.y+dy)
                self.energie -= 20
                loups.append(petit)
        
    def mouton_voisin (self):
        for (dx, dy) in dxdy:
            if grid.is_mouton(self.x+dx, self.y+dy):
                ix = self.x + dx
                igrec = self.y + dy
                for elem in moutons:
                    if (elem.x,elem.y) == (ix,igrec):
                        return True, ix, igrec, elem
        return False,0,0,Mouton(0,0) #memoriellement sous-optimal car on fait pop un mouton pour le tuer s'il n'y en a pas
        
    def deplacement(self):
        """se deplace et mange le cas echeant"""
        if self.vivant :
            mv = self.mouton_voisin()
            if mv[0]: 
                self.x = mv[1]
                self.y = mv[2]
                self.energie += 30
            else :
                i = rd.randint(0,3)
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
            return mv[3]
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



class Grid:
    def __init__(self, size):
        self.size = size
        self.cells = np.full((size, size), '.')


    def is_mouton(self, x,y):
        return self.cells[x][y] == 'M'


    def update(self):
        self.cells = np.full((GRID_SIZE, GRID_SIZE), '.')

        # Update grass
        for x in range(GRID_SIZE):
            for y in range(GRID_SIZE):
                if grille_herbe[x][y].tps_depuis_mort == -1:
                    self.cells[x][y] = '#'

        # Update sheep
        for mouton in moutons:
            if mouton._en_vie:
                self.cells[mouton.x][mouton.y] = 'M'

        # Update wolves
        for loup in loups:
            if loup.vivant:
                self.cells[loup.x][loup.y] = 'W'

def libre(x, y):
    for loup in loups:
        if loup.x == x and loup.y == y and loup.vivant:
            return False
    for mouton in moutons:
        if mouton.x == x and mouton.y == y and mouton._en_vie:
            return False
    return True

# Initialize the grid
grid = Grid(GRID_SIZE)


grille_herbe = np.array([[Herbe(x, y) for y in range(GRID_SIZE)] for x in range(GRID_SIZE)])
# Initialize sheep and wolves
moutons = [Mouton(1, 1), Mouton(5, 5), Mouton(10, 10)]
loups = [Loup(2, 2), Loup(8, 8)]

# Simulation loop
nb_tours = 0
while nb_tours < 100:
    # Update sheep
    for mouton in moutons:
        if mouton._en_vie:
            mouton.vieillir()
            herbe_trouvee = mouton.trouve_herbe()
            if herbe_trouvee[0]:
                mouton.deplace(herbe_trouvee[1:3])
                grille_herbe[mouton.x][mouton.y].mangee()
                mouton.manger()
            else:
                mouton.deplace(mouton.direction_aleatoire())
            mouton.reproduction()
            mouton.mort()
            mouton._energie -= 1

    # Update wolves
        for loup in loups :

            loup.vieillir()
            loup.perte_energie()
            loup.deplacement().vivant = False
            loup.reproduction()
            loup.mort()
            
            grid.update()
    


    # Update grass
    vectorized_repousse(grille_herbe)

    # Update grid
    grid.update()

    nb_tours += 1


    print(np.array(grid.cells))

print("Simulation terminée.")
