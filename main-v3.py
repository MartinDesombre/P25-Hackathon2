import random
import numpy as np
import matplotlib.pyplot as plt

GRID_SIZE = 20
GRASS_COVERAGE = 0.3
vectorized_repousse = np.vectorize(lambda herbe: herbe.repousse())
# Directions pour le loup de Joseph
dxdy = [(1, 0), (0, 1), (-1, 0), (0, -1)]

class Herbe:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.tps_depuis_mort = -1 if random.random() <= GRASS_COVERAGE else random.randint(0, 7)

    def mangee(self):
        self.tps_depuis_mort = 0

    def repousse(self):
        if grid.is_mouton(self.x,self.y) or self.tps_depuis_mort == -1:
            pass  # Grass is already alive
        else:
            self.tps_depuis_mort += 1
            if random.random() < 0.08 or self.tps_depuis_mort >= 7:
                self.tps_depuis_mort = -1  # Grass regrows

class Loup :
    def __init__(self,x,y):
        self.vivant = True
        self.x = x
        self.y = y
        self.age = 0
        self.energie = 60
        self.seuil = 70 #seuil pour la reproduction
        self.limite = 50 #limite d'age
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
                if self.x+dx<GRID_SIZE and self.y+dy<GRID_SIZE and self.x+dx>=0 and self.y+dy>=0:

                    petit = Loup(self.x+dx,self.y+dy)
                    self.energie -= 20
                    loups.append(petit)
        
    def mouton_voisin (self):
        random.shuffle(dxdy)
        for (dx, dy) in dxdy:
            if self.x+dx<GRID_SIZE and self.y+dy<GRID_SIZE and self.x+dx>=0 and self.y+dy>=0:
                if grid.is_mouton(self.x+dx, self.y+dy):
                    ix = self.x + dx
                    igrec = self.y + dy
                    for elem in moutons:
                        if (elem.x,elem.y) == (ix,igrec):
                            return True, ix, igrec, elem
        return False,0,0,None #memoriellement sous-optimal car on fait pop un mouton pour le tuer s'il n'y en a pas
        
    def deplacement(self):
        """se deplace et mange le cas echeant"""
        if self.vivant :
            mv = self.mouton_voisin()
            if mv[0]: 
                self.x = mv[1]
                self.y = mv[2]
                self.energie += 40
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
                    if self.x+dx<GRID_SIZE and self.y+dy<GRID_SIZE and self.x+dx>=0 and self.y+dy>=0:
                        
                        self.x += dx
                        self.y += dy
            return mv[3]

class Mouton:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self._age = 0
        self._energie = 10
        self._en_vie = True

    def vieillir(self):
        self._age += 1

    def trouve_herbe(self):
        random.shuffle(dxdy)
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

    def deplace(self, pos):
        dx, dy = pos
        nx, ny = self.x + dx, self.y + dy
        if 0 <= nx < GRID_SIZE and 0 <= ny < GRID_SIZE:
            self.x, self.y = nx, ny

    def manger(self):
        self._energie += 5

    def reproduction(self):
        if self._energie > 50:
            for dx, dy in dxdy:
                nx, ny = self.x + dx, self.y + dy
                if 0 <= nx < GRID_SIZE and 0 <= ny < GRID_SIZE and libre(nx, ny):
                    self._energie -= 20
                    moutons.append(Mouton(nx, ny))
                    break

    def mort(self):
        if self._energie <= 0 or self._age > 20:
            self._en_vie = False

def libre(x, y):
    for loup in loups:
        if loup.x == x and loup.y == y and loup.vivant:
            return False
    for mouton in moutons:
        if mouton.x == x and mouton.y == y and mouton._en_vie:
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


grid = Grid(GRID_SIZE)
grille_herbe = np.array([[Herbe(x, y) for y in range(GRID_SIZE)] for x in range(GRID_SIZE)])



def visualize_grid(grid, nb_tours):
    colors = {
        '.': 'white',
        '#': 'green',
        'M': 'blue',
        'W': 'red'
    }

    color_grid = np.zeros((grid.size, grid.size, 3), dtype=float)
    for x in range(grid.size):
        for y in range(grid.size):
            color_grid[x, y] = plt.cm.colors.to_rgb(colors[grid.cells[x, y]])

    plt.clf()  # Clear the current figure
    plt.imshow(color_grid, interpolation='nearest')
    plt.title(f"Simulation at Tour {nb_tours}")
    plt.xticks([]), plt.yticks([])
    plt.draw()
    plt.pause(0.1)  # Pause briefly to allow the plot to update


moutons = [Mouton(1, 1), Mouton(5, 5), Mouton(10, 10), Mouton(15,13),Mouton(5, 15), Mouton(10, 18), Mouton(19,13)]
loups = [Loup(2, 2), Loup(8, 8), Loup(4, 4), Loup(6, 6),Loup(15,15),Loup(5,5),Loup(15,15),Loup(10,10),Loup(15,15),Loup(8,13),Loup(17,11)]

# Simulation
plt.ion()  # Turn on interactive mode
nb_tours = 0
while nb_tours < 50:

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

    # Update loup
    for loup in loups:
        if loup.vivant:
            mouton_mange = loup.deplacement()
            if isinstance(mouton_mange, Mouton):
                mouton_mange._en_vie = False

    for loup in loups:
        if loup.vivant:
            loup.vieillir()
            loup.perte_energie()
            mouton_mange = loup.deplacement()
            if isinstance(mouton_mange, Mouton):
                mouton_mange._en_vie = False
            loup.reproduction()
            loup.mort()

  
    vectorized_repousse(grille_herbe)

    grid.update()
    visualize_grid(grid, nb_tours)

    nb_tours += 1

plt.ioff()  
plt.show()  
