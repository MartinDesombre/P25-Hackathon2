import random as rd
class Loup :
    vivant = True
    x = 0#on s'en fout, on admet que dès qu'on créera un loup, on modifiera la position immédiatement après
    y = 0#idem
    age = 0
    energie = 40
    seuil = 80 #seuil pour la reproduction
    limite = 40 #limite d'age
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
            while not(libre(x+dx,y+dy)):
                dx = rd.randint(0,1)
                dx = 2*(dx-0.5)
                dy= rd.randint(0,1)
                dy = 2*(dx-0.5)
            petit = loup()
            petit.x = self.x+dx
            petit.y = self.y+dy
            return petit
        
    def mouton_voisin (self):
        if Grid.is_mouton(self.x,self.y)[0] :
            return Grid.is_mouton[1:2]
        
    def deplacement(self):
        if self.vivant :
            mv = mouton_voisin(self.x,self.y)
            if mv[0]: 
                self.x = mv[1]
                self.y = mv[2]
            else :
                while not(libre(x+dx,y+dy):
                        dx = rd.randint(0,1)
                        dx = 2*(dx-0.5)
                        dy= rd.randint(0,1)
                        dy = 2*(dx-0.5)
            self.x += dx
            self.y += dy

    

    