import random as rd
class Loup :
    def __init__(self,x,y,id)
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
            while not(libre(self.x+dx,self.y+dy)):#a resoudre pour eviter boucle infini
                dx = rd.randint(0,1)
                dx = 2*(dx-0.5)
                dy= rd.randint(0,1)
                dy = 2*(dx-0.5)
            id = #a revoir
            petit = Loup(self.x+dx,self.y+dy,id)
            self.energie -= 20
            return petit
    def deplacement(self):
        """se deplace et mange le cas echeant"""
        if self.vivant :
            mv = mouton_voisin(self.x,self.y)
            if mv[0]: 
                self.x = mv[1]
                self.y = mv[2]
                self.energie += 30
            else :
                while not(libre(self.x+dx,self.y+dy)):
                        dx = rd.randint(0,1)
                        dx = 2*(dx-0.5)
                        dy= rd.randint(0,1)
                        dy = 2*(dx-0.5)
            self.x += dx
            self.y += dy
def mouton_voisin(x,y):
    for elem in moutons:
        if abs(x-elem.x) = 1 :
            if abs(y-elem.y) = 1:
                return True, elem.x, elem.y
    return False,0,0
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