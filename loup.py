import random as rd
class Loup() :
    def __init__(self,id,x,y):
        self.id = id
        self.vivant = True
        self.x = x#on s'en fout, on admet que dès qu'on créera un loup, on modifiera la position immédiatement après
        self.y = y#idem
        self.age = 0
        self.energie = 40
        self.seuil = 80 #seuil pour la reproduction
        self.limite = 40 #limite d'age*

    def vieillir(self):
        if self.vivant :
            self.age += 1
    def perte_energie(self):
        if self.vivant :
            self.energie -= 2
    def mort(self):
        if self.vivant and (self.age>self.limite or self.energie)<0 :
            self.vivant = False
    def reproduction(self):
        if self.vivant and energie>seuil :
        if self.vivant and energie>seuil :
            while not(libre(x+dx,y+dy):
                dx = rd.randint(0,1)
                dx = 2*(dx-0.5)
                dy= rd.randint(0,1)
                dy = 2*(dx-0.5)
            id = #à compléter avec le prochain id disponible
            petit = Loup(id,x,y)
            return petit
    def deplacement(self):
        if self.vivant :
            if: ##definir une condition en fonction de l'implementation des moutons
            #definir une action en fonction de l'imlplementation des moutons
            else :
                while not(libre(x+dx,y+dy)):
                        dx = rd.randint(0,1)
                        dx = 2*(dx-0.5)
                        dy= rd.randint(0,1)
                        dy = 2*(dx-0.5)
            self.x += dx
            self.y += dy

