import random as rd
class loup :
    vivant = True
    x = 0#on s'en fout, on admet que dès qu'on créera un loup, on modifiera la position immédiatement après
    y = 0#idem
    age = 0
    energie = 40
    seuil = 80 #seuil pour la reproduction
    limite = 40 #limite d'age
    def vieillir(self):
        self.age += 1
    def perte_energie(self):
        self.energie -= 2
    def mort(self):
        if self.age>self.limite or self.energie<0 :
            self.vivant = False
    def reproduction(self):
        if energie>seuil :
            while not(libre(x+dx,y+dy):
                dx = rd.randint(0,1)
                dx = 2*(dx-0.5)
                dy= rd.randint(0,1)
                dy = 2*(dx-0.5)
            petit = loup()
            petit.x = self.x+dx
            petit.y = self.y+dy
            return petit
    def deplacement(self):
        if: ##definir une condition en fonction de l'implementation des moutons
        #definir une action en fonction de l'imlplementation des moutons
        else :
             while not(libre(x+dx,y+dy):
                    dx = rd.randint(0,1)
                    dx = 2*(dx-0.5)
                    dy= rd.randint(0,1)
                    dy = 2*(dx-0.5)
        self.x += dx
        self.y += dy

