import random as rd
dxdy = [(1,0),(0,1),(-1,0),(0,-1)]
class Loup :
    def __init__(self,x,y,id):
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
            if Grid.is_mouton(self.x+dx,self.y+dy):
                ix = self.x + dx
                igrec = self.y + dy
                for elem in moutons:
                    if (elem.x,elem.y) = (ix,igrec)
                        return True, x, y, elem
        return False,0,0,Mouton(0,0) #memoriellement sous-optimal car on fait pop un mouton pour le tuer s'il n'y en a pas
        
    def deplacement(self):
        """se deplace et mange le cas echeant"""
        if self.vivant :
            mv = mouton_voisin(self)
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